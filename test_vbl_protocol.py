"""
VBL-VP 1.0 — acceptance tests (VBL-PROTOCOL §9).

Each test is named for the behavior it verifies — a fall without a
name repeats (L2). Run: python test_vbl_protocol.py (zero dependencies).

Test 13 is reconstructed: the protocol draft's §9 arrived truncated
mid-sentence ("…preserve the relevant"); the test asserts the §8
behavior stated earlier in the draft. ⚠ Reconstructed, marked.
"""

from __future__ import annotations

import unittest

from vbl_protocol import (
    INDEPENDENTLY_VERIFIED, INDEPENDENCE_UNESTABLISHED, CLOSED_VERIFIED,
    PARTIALLY_REMEDIED, ProtocolViolation, Incident, EvidenceRef, Finding,
    Pattern, scan_encoding_integrity, bytes_identical,
)


def incident(executor="executor-1"):
    inc = Incident("I-1", "reported deed", reporter="reporter-1",
                   executor=executor)
    return inc


class UnsupportedClaimTests(unittest.TestCase):
    def test_unsupported_claim_cannot_be_verified(self):
        """§9.1 — a claim without a supporting witness cannot receive
        verified status."""
        inc = incident()
        inc.record_finding(Finding(claim="the deed caused X",
                                  evidence_refs=[]))
        self.assertEqual(inc.findings[0].disposition, "UNVERIFIED")
        self.assertFalse(inc.findings[0].established())
        self.assertEqual(inc.established_findings(), [])
        with self.assertRaises(ProtocolViolation):
            inc.transition(INDEPENDENTLY_VERIFIED, actor="verifier-1")

    def test_claim_with_witness_can_be_established(self):
        inc = incident()
        ev = EvidenceRef(source="log", location="line 4",
                         excerpt="the deed caused X")
        inc.record_finding(Finding(claim="the deed caused X",
                                  evidence_refs=[ev],
                                  disposition="ESTABLISHED"))
        self.assertEqual(len(inc.established_findings()), 1)


class SelfVerificationTests(unittest.TestCase):
    def test_executor_cannot_self_verify(self):
        """§9.2 — an executor cannot independently certify their own
        remedy; a second signature from the same actor is not a second
        hand (§6)."""
        inc = incident(executor="executor-1")
        ev = EvidenceRef(source="fix", location="commit a1b2",
                         excerpt="remedy applied")
        inc.record_finding(Finding(claim="remedy executed",
                                  evidence_refs=[ev],
                                  disposition="ESTABLISHED"))
        with self.assertRaises(ProtocolViolation):
            inc.transition(INDEPENDENTLY_VERIFIED, actor="executor-1")
        # the honest state is available and named:
        rec = inc.verify(verifier="executor-1", scope="completion criteria",
                         evidence_examined=[ev], criteria_passed=[],
                         criteria_failed=["independence"], limitations="same actor")
        self.assertEqual(rec.decision, INDEPENDENCE_UNESTABLISHED)

    def test_separate_verifier_can_verify(self):
        inc = incident(executor="executor-1")
        inc.transition(INDEPENDENTLY_VERIFIED, actor="verifier-2")
        self.assertEqual(inc.state, INDEPENDENTLY_VERIFIED)


class FalseClosureTests(unittest.TestCase):
    def test_outstanding_remedy_prevents_closed_verified(self):
        """§9.3 — an outstanding mandatory remedy prevents CLOSED_VERIFIED;
        no missing step may be silently inferred from a later state."""
        inc = incident()
        inc.transition(INDEPENDENTLY_VERIFIED, actor="verifier-2")
        inc.define_remedy("R1", "restitution", mandatory=True)
        with self.assertRaises(ProtocolViolation):
            inc.transition(CLOSED_VERIFIED, actor="verifier-2")

    def test_payment_only_does_not_complete_remedy(self):
        """§9.5 — a payment record does not prove the full remedy was
        completed."""
        inc = incident()
        inc.transition(INDEPENDENTLY_VERIFIED, actor="verifier-2")
        pay = inc.define_remedy("R-pay", "payment", mandatory=True)
        rest = inc.define_remedy("R-rest", "restitution", mandatory=True)
        pay.record_evidence(
            EvidenceRef(source="bank", location="tx 7",
                         excerpt="payment sent"), by="executor-1")
        pay.satisfied = True
        # restitution still outstanding — closure refused
        with self.assertRaises(ProtocolViolation):
            inc.transition(CLOSED_VERIFIED, actor="verifier-2")
        self.assertFalse(rest.satisfied)

    def test_attribution_only_does_not_satisfy_restitution(self):
        """§9.4 — restored credit does not automatically satisfy
        restitution requirements."""
        inc = incident()
        inc.define_remedy("R-credit", "credit", mandatory=True)
        rest = inc.define_remedy("R-rest", "restitution", mandatory=True)
        cred = inc.remedy_requirements[0]
        cred.record_evidence(
            EvidenceRef(source="README", location="credits",
                         excerpt="credit restored"), by="executor-1")
        cred.satisfied = True
        # kinds are distinct: credit ≠ restitution
        self.assertFalse(rest.satisfied)
        self.assertEqual(inc._outstanding_mandatory(), [rest])

    def test_partial_remedy_records_remaining_balance(self):
        """§9.12 — a partially remediated case records its remaining
        balance and limitations."""
        inc = incident()
        inc.transition(INDEPENDENTLY_VERIFIED, actor="verifier-2")
        done = inc.define_remedy("R-pay", "payment", mandatory=True)
        owed = inc.define_remedy("R-rest", "restitution", mandatory=True)
        done.satisfied = True
        balance = inc.close_partial(
            actor="verifier-2",
            limitations_and_reason="full repair impossible: material lost")
        self.assertEqual(balance["remaining_balance"], ["R-rest"])
        self.assertEqual(inc.state, PARTIALLY_REMEDIED)
        self.assertIn("impossible", inc.limitations_and_reason)


class OverwriteTests(unittest.TestCase):
    def test_correction_preserves_prior_version(self):
        """§9.6 — changing a finding preserves the prior version and
        records the correction; nothing is silently overwritten."""
        inc = incident()
        inc.impact_assessment = "harm: low"
        inc.revise("impact_assessment", "harm: severe",
                   reason="new evidence measured", prior="harm: low")
        self.assertEqual(inc.impact_assessment, "harm: severe")
        self.assertEqual(len(inc.revisions), 1)
        self.assertEqual(inc.revisions[0]["prior_value"], "harm: low")
        # the prior version is recoverable from the record itself
        self.assertIn("prior_value", inc.revisions[0])


class UnsubstantiatedTests(unittest.TestCase):
    def test_unsubstantiated_not_established_finding(self):
        """§9.7 — an unsubstantiated allegation is not presented as an
        established finding."""
        inc = incident()
        inc.record_finding(Finding(claim="allegation X", evidence_refs=[],
                                  disposition="UNVERIFIED", disputed=False))
        self.assertEqual(inc.established_findings(), [])
        # a witness upgrades it honestly:
        inc.findings[0].evidence_refs.append(
            EvidenceRef(source="archive", location="p.9", excerpt="X"))
        inc.findings[0].disposition = "ESTABLISHED"
        self.assertEqual(len(inc.established_findings()), 1)


class ReporterProtectionTests(unittest.TestCase):
    def test_affected_party_can_report_without_author(self):
        """§9.8 — the absence of the original author does not prevent an
        affected party from submitting a report."""
        inc = Incident("I-2", "reported deed", reporter="affected-1",
                       executor="", reporter_role="affected_party")
        self.assertEqual(inc.reporter_role, "affected_party")
        self.assertEqual(inc.state, "REPORTED")
        # the report exists and is received whether or not any author exists
        self.assertTrue(inc.status_history[0]["state"] == "REPORTED")


class SilenceTests(unittest.TestCase):
    def test_silence_not_recorded_as_forgiveness(self):
        """§9.9 — no response from an affected party is not recorded as
        forgiveness or satisfaction."""
        inc = incident()
        inc.record_affected_party_silence()
        self.assertTrue(inc.affected_party_silence_observed)
        with self.assertRaises(ProtocolViolation):
            inc.record_satisfaction(basis="silence", by="executor-1")
        self.assertIsNone(inc.satisfaction_recorded)
        # explicit, non-silent satisfaction remains possible:
        inc.record_satisfaction(basis="written statement", by="affected-1")
        self.assertEqual(inc.satisfaction_recorded["basis"],
                         "written statement")


class IntentTests(unittest.TestCase):
    def test_intent_not_inferred_from_outcome(self):
        """§9.10 — the system does not infer premeditated intent solely
        from harm or benefit."""
        inc = incident()
        with_evidence = inc.assess_predation(
            benefit="retained revenue",
            evidence_refs=[EvidenceRef(source="ledger", location="Q3",
                                       excerpt="benefit retained")])
        self.assertEqual(with_evidence["intent"], "UNVERIFIED")
        without = inc.assess_predation(benefit="retained revenue",
                                       evidence_refs=[])
        self.assertEqual(without["classification"], "UNVERIFIED")


class MissingVerifierTests(unittest.TestCase):
    def test_missing_verifier_leaves_unresolved(self):
        """§9.11 — a case cannot claim independent verification without
        a qualified, separate verifier; independence is not manufactured."""
        inc = incident(executor="executor-1")
        rec = inc.verify(verifier="", scope="criteria",
                         evidence_examined=[], criteria_passed=[],
                         criteria_failed=[], limitations="no verifier")
        self.assertEqual(rec.decision, INDEPENDENCE_UNESTABLISHED)
        self.assertTrue(all(v.decision != "INDEPENDENT"
                            for v in inc.verification_refs))


class PatternTests(unittest.TestCase):
    def test_pattern_is_conduct_never_a_verdict_on_a_being(self):
        """§2 K6 / §9 — repeated conduct is linked, dated, evidenced;
        it never becomes a permanent classification of inherent worth."""
        p = Pattern("P-1", incident_links=["I-1", "I-2", "I-3"],
                    evidence_refs=[EvidenceRef(source="register",
                                               location="entries 3-5",
                                               excerpt="same conduct")])
        a = p.assess()
        self.assertEqual(a["recurrence"], "ASSESSED")
        self.assertIn("never a verdict on a being", a["note"])
        with self.assertRaises(ProtocolViolation):
            p.classify_person()
        empty = Pattern("P-2", incident_links=[], evidence_refs=[])
        self.assertEqual(empty.assess()["recurrence"], "UNVERIFIED")


class EncodingLossTests(unittest.TestCase):
    def test_encoding_loss_warns_and_preserves_artifact(self):
        """§9.13 ⚠ reconstructed (draft arrived truncated mid-sentence) —
        suspicious replacement characters produce a warning; the warning
        is evidence of possible decoding loss, not of wrongdoing."""
        damaged = "tr\u2013nsport z \ufffd v telesu"
        scan = scan_encoding_integrity(damaged)
        self.assertTrue(scan["u_fffd_warning"])
        self.assertEqual(scan["hits"], 1)
        self.assertIn("not proof of wrongdoing", scan["note"])
        clean = scan_encoding_integrity("transport brez ran")
        self.assertFalse(clean["u_fffd_warning"])
        # the artifact itself is preserved — the scan never rewrites it:
        self.assertEqual(damaged, "tr\u2013nsport z \ufffd v telesu")

    def test_byte_identity_is_an_actual_comparison(self):
        """§8 — byte-identical transport cannot be inferred from visual
        similarity."""
        self.assertTrue(bytes_identical(b"vrata", b"vrata"))
        self.assertFalse(bytes_identical("vrata".encode("utf-8"),
                                         "vr\u00e0ta".encode("utf-8")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
