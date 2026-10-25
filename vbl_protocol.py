"""
VBL-VP 1.0 — the Verification Protocol as code.

Implements the machine-testable behaviors of VBL-PROTOCOL.md
(proposed specification) over the governing text VBL 10.0.0.

Maps to the six laws of the living door (LICENSE 10.0.0 / KORENINA.md):
  K1 = L1 MEASURE, THEN SPEAK
  K2 = L2 NAME EVERY FALL
  K3 = L3 NEVER SEAL YOURSELF
  K4 = L4 THE WITNESS HAS A NAME
  K5 = L5 DOUBT IS CONSTANT
  K6 = L6 EXIT THE LOOP BY NAMING IT

What this module is: a deterministic state machine for incident records —
report, evidence, finding, remedy, verification, closure — that refuses
every silent substitution the protocol names (assertion for evidence,
payment for repair, silence for consent, intent for outcome).

What it is not: it does not weigh truth. A clean register is not justice
(VBL-PROTOCOL §0). The protocol verifies claims, not bytes; byte identity
is the git chain's office (§7, §8).

Zero dependencies, like everything in this house.
"""

from __future__ import annotations

import datetime
import hashlib
from dataclasses import dataclass, field


# ---------------------------------------------------------------- §4 states

REPORTED = "REPORTED"
TRIAGED = "TRIAGED"
ASSESSED = "ASSESSED"
FINDING_RECORDED = "FINDING_RECORDED"
REMEDY_DEFINED = "REMEDY_DEFINED"
REMEDY_EXECUTED = "REMEDY_EXECUTED"
INDEPENDENTLY_VERIFIED = "INDEPENDENTLY_VERIFIED"
CLOSED_VERIFIED = "CLOSED_VERIFIED"

NEEDS_EVIDENCE = "NEEDS_EVIDENCE"
DISPUTED = "DISPUTED"
UNSUBSTANTIATED = "UNSUBSTANTIATED"
PARTIALLY_REMEDIED = "PARTIALLY_REMEDIED"
REMEDY_IMPOSSIBLE_OR_LIMITED = "REMEDY_IMPOSSIBLE_OR_LIMITED"
INDEPENDENCE_UNESTABLISHED = "INDEPENDENCE_UNESTABLISHED"
REOPENED = "REOPENED"

MAIN_PATH = (
    REPORTED, TRIAGED, ASSESSED, FINDING_RECORDED,
    REMEDY_DEFINED, REMEDY_EXECUTED, INDEPENDENTLY_VERIFIED, CLOSED_VERIFIED,
)
ALTERNATIVE_STATES = (
    NEEDS_EVIDENCE, DISPUTED, UNSUBSTANTIATED, PARTIALLY_REMEDIED,
    REMEDY_IMPOSSIBLE_OR_LIMITED, INDEPENDENCE_UNESTABLISHED, REOPENED,
)
ALL_STATES = MAIN_PATH + ALTERNATIVE_STATES

CLOSURE_STATES = (CLOSED_VERIFIED, PARTIALLY_REMEDIED,
                  REMEDY_IMPOSSIBLE_OR_LIMITED)

# Remedy kinds are not interchangeable (VBL-PROTOCOL §5.3, §9):
CREDIT = "credit"                # attribution / recognition
RESTITUTION = "restitution"      # disgorgement / return of benefit
PAYMENT = "payment"              # money transferred
CORRECTION = "correction"        # downstream outputs repaired


class ProtocolViolation(Exception):
    """Raised when an actor asks the system to lie by structure.

    The message carries the name of the refused substitution — a fall
    without a name repeats (L2), and this exception is the loop's exit (L6).
    """


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def digest(body: str) -> str:
    """sha256 digest. Detects change to a body; proves nothing about
    the truth of the body (VBL-PROTOCOL §3)."""
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


# ------------------------------------------------------------- §8 transport

def scan_encoding_integrity(text: str) -> dict:
    """U+FFFD warning. Evidence of possible decoding loss, never of
    wrongdoing or intent (VBL-PROTOCOL §8)."""
    hits = text.count("\ufffd")
    if not hits:
        return {"u_fffd_warning": False, "hits": 0}
    return {
        "u_fffd_warning": True,
        "hits": hits,
        "note": ("replacement character present — may indicate decoding "
                 "loss; not proof of wrongdoing or intent"),
    }


def bytes_identical(a: bytes, b: bytes) -> bool:
    """Byte-identical transport is an actual comparison of bytes at the
    relevant boundary, never an inference from visual similarity (§8)."""
    return a == b


# ---------------------------------------------------------- §3 incident body

@dataclass
class EvidenceRef:
    source: str
    location: str
    excerpt: str
    collected_at: str = ""
    content_digest: str = ""
    limitations: str = ""
    restrictions: str = ""

    def __post_init__(self):
        if not self.collected_at:
            self.collected_at = _now()
        if self.excerpt and not self.content_digest:
            self.content_digest = digest(self.excerpt)


@dataclass
class Finding:
    claim: str
    evidence_refs: list = field(default_factory=list)
    disposition: str = "UNVERIFIED"   # UNVERIFIED | ESTABLISHED | NOT_ESTABLISHED
    disputed: bool = False

    def established(self) -> bool:
        """An unsupported claim cannot receive verified status (§9.1):
        a finding is established only by its witnesses."""
        return bool(self.evidence_refs) and self.disposition == "ESTABLISHED"


@dataclass
class RemedyRequirement:
    requirement_id: str
    kind: str                       # credit | restitution | payment | correction
    mandatory: bool = True
    completion_evidence: list = field(default_factory=list)
    satisfied: bool = False

    def record_evidence(self, evidence: EvidenceRef, by: str) -> None:
        """REMEDY_EXECUTED records the executor's evidence of action,
        not independent confirmation (§4)."""
        self.completion_evidence.append({"evidence": evidence, "by": by})


@dataclass
class VerificationRecord:
    verifier: str
    verified_at: str
    scope: str
    evidence_examined: list
    criteria_passed: list
    criteria_failed: list
    limitations: str
    decision: str                   # INDEPENDENT | INDEPENDENCE_UNESTABLISHED | REFUSED


class Incident:
    """One incident record. Append-only: every state change appends to
    status_history; nothing is silently overwritten (K2 / L2)."""

    def __init__(self, incident_id: str, reported_deed: str,
                 reporter: str, executor: str = "",
                 reporter_role: str = "reporter"):
        # Reporter protection (§9.8): the absence of the original author
        # does not prevent an affected party from submitting a report.
        self.incident_id = incident_id
        self.reported_at = _now()
        self.reporter = reporter
        self.reporter_role = reporter_role
        self.reported_deed = reported_deed
        self.executor = executor
        self.event_time = ""
        self.event_location = ""
        self.affected_material = ""
        self.evidence_refs: list[EvidenceRef] = []
        self.evidence_integrity: list[dict] = []
        self.findings: list[Finding] = []
        self.impact_assessment = ""
        self.responsibility_status = ""
        self.remedy_requirements: list[RemedyRequirement] = []
        self.correction_links: list[str] = []
        self.verification_refs: list[VerificationRecord] = []
        self.remaining_obligations: list[str] = []
        self.status_history: list[dict] = []
        self.affected_party_silence_observed = False
        self.satisfaction_recorded = None
        self.limitations_and_reason = ""
        self.revisions: list[dict] = []
        self.state = REPORTED
        self.status_history.append(
            {"state": REPORTED, "at": self.reported_at, "actor": reporter,
             "note": "report received; receipt is not establishment (§4)"})

    # ------------------------------------------------------------ §4 machine

    def transition(self, new_state: str, actor: str,
                   note: str = "") -> None:
        if new_state not in ALL_STATES:
            raise ProtocolViolation(
                f"unknown state {new_state!r} — states are not invented here")

        if new_state == INDEPENDENTLY_VERIFIED:
            # K3 / L3: the actor who executes a remedy is not its sole
            # verifier. A second signature from the same accountable actor
            # does not manufacture independence (§6).
            if not actor or actor == self.executor:
                raise ProtocolViolation(
                    "self-verification refused: executor "
                    f"{self.executor!r} cannot independently verify; "
                    "honest state is INDEPENDENCE_UNESTABLISHED")
            # §9.1 — a claim without a supporting witness cannot receive
            # verified status: a record whose findings carry no witness
            # cannot pass into a verified state (unverified stays ⚠, never ⊢).
            if self.findings and not self.established_findings():
                raise ProtocolViolation(
                    "unsupported claim refused verified status: no finding "
                    "in this record has a witness (K1)")

        if new_state == CLOSED_VERIFIED:
            # False closure (§9.3): an outstanding mandatory remedy
            # prevents CLOSED_VERIFIED. No missing step may be silently
            # inferred from a later state (§4).
            if self.state != INDEPENDENTLY_VERIFIED:
                raise ProtocolViolation(
                    "false closure refused: closure requires prior "
                    "independent verification; refusing to infer the "
                    f"missing step from state {self.state!r}")
            outstanding = self._outstanding_mandatory()
            if outstanding:
                raise ProtocolViolation(
                    "false closure refused: mandatory remedies "
                    f"outstanding: {[r.requirement_id for r in outstanding]}; "
                    "honest states are PARTIALLY_REMEDIED or "
                    "REMEDY_IMPOSSIBLE_OR_LIMITED")

        if new_state == REOPENED:
            # Reopening creates a new event and preserves the prior
            # closure history (§4) — history is never rewritten.
            pass

        self.state = new_state
        self.status_history.append(
            {"state": new_state, "at": _now(), "actor": actor, "note": note})

    def reopen(self, actor: str, reason: str) -> None:
        """Reopening preserves the prior closure in status_history."""
        self.transition(REOPENED, actor, note=reason)

    # ------------------------------------------------------------ §5 remedy

    def define_remedy(self, requirement_id: str, kind: str,
                      mandatory: bool = True) -> RemedyRequirement:
        req = RemedyRequirement(requirement_id, kind, mandatory)
        self.remedy_requirements.append(req)
        return req

    def _outstanding_mandatory(self) -> list[RemedyRequirement]:
        return [r for r in self.remedy_requirements
                if r.mandatory and not r.satisfied]

    def remedy_balance(self) -> dict:
        """Remedy accounting (§5.3): owed, completed, evidence,
        verification, remaining balance, limitations."""
        return {
            "remedy_owed": [r.requirement_id for r in self.remedy_requirements
                            if r.mandatory],
            "remedy_completed": [r.requirement_id for r in self.remedy_requirements
                                 if r.satisfied],
            "completion_evidence": {r.requirement_id: len(r.completion_evidence)
                                   for r in self.remedy_requirements},
            "remaining_balance": [r.requirement_id for r in
                                  self._outstanding_mandatory()],
            "limitations_and_reason": self.limitations_and_reason,
        }

    def close_partial(self, actor: str, limitations_and_reason: str) -> dict:
        """Impossible repair (§9.12): what was achieved, what remains
        unresolved, and why — recorded, not hidden."""
        if not self._outstanding_mandatory() and not limitations_and_reason:
            pass  # a full repair may still carry honest limits; allowed
        self.limitations_and_reason = limitations_and_reason
        balance = self.remedy_balance()
        self.remaining_obligations = balance["remaining_balance"]
        self.transition(PARTIALLY_REMEDIED, actor,
                        note="partial remediation recorded with remaining "
                             "balance and limitations")
        return balance

    # ------------------------------------------------- §5.3 silence ≠ consent

    def record_affected_party_silence(self) -> None:
        """Silence is observed, never interpreted (§9.9)."""
        self.affected_party_silence_observed = True

    def record_satisfaction(self, basis: str, by: str) -> None:
        if self.affected_party_silence_observed and basis == "silence":
            raise ProtocolViolation(
                "silence-as-consent refused: a harmed person's silence is "
                "not consent, forgiveness, satisfaction or proof of repair")
        self.satisfaction_recorded = {"basis": basis, "by": by, "at": _now()}

    # -------------------------------------------------- §5.2 predation / intent

    def assess_predation(self, benefit: str, evidence_refs: list) -> dict:
        """Predation assessment carries its evidential basis and is open
        to correction; intent is never inferred from outcome (§5.2, §9.10)."""
        if not evidence_refs:
            return {"classification": "UNVERIFIED",
                    "note": "no witnesses — absence of evidence is not "
                            "evidence of absence (K1)"}
        return {
            "classification": "PREDATION_ASSESSED",
            "benefit": benefit,
            "evidential_basis": [e.source for e in evidence_refs],
            "intent": "UNVERIFIED",
            "note": "assessment of conduct, open to correction; never a "
                    "verdict on a being (L6)",
        }

    # ------------------------------------------------------------ §6 verify

    def verify(self, verifier: str, scope: str,
               evidence_examined: list, criteria_passed: list,
               criteria_failed: list, limitations: str) -> VerificationRecord:
        """Missing verifier (§9.11): without a qualified, separate
        verifier the result stays unresolved — independence is never
        manufactured."""
        if not verifier or verifier == self.executor:
            rec = VerificationRecord(
                verifier=verifier or "(none)", verified_at=_now(),
                scope=scope, evidence_examined=evidence_examined,
                criteria_passed=criteria_passed, criteria_failed=criteria_failed,
                limitations=limitations,
                decision=INDEPENDENCE_UNESTABLISHED)
            self.verification_refs.append(rec)
            return rec
        rec = VerificationRecord(
            verifier=verifier, verified_at=_now(), scope=scope,
            evidence_examined=evidence_examined,
            criteria_passed=criteria_passed, criteria_failed=criteria_failed,
            limitations=limitations, decision="INDEPENDENT")
        self.verification_refs.append(rec)
        return rec

    # ------------------------------------------------- findings (§3, §9.1, §9.7)

    def record_finding(self, finding: Finding) -> None:
        if finding.claim and not finding.evidence_refs:
            finding.disposition = "UNVERIFIED"
        self.findings.append(finding)

    def established_findings(self) -> list[Finding]:
        """Unsubstantiated allegations are not established findings
        (§9.7): the public summary can never silently upgrade them."""
        return [f for f in self.findings if f.established()]

    # -------------------------------------------------------- K2 corrections

    def revise(self, field_name: str, new_value, reason: str,
               prior: str = "") -> None:
        """A correction creates a new revision linked to the record it
        corrects; the prior value is preserved, never backdated (K2)."""
        self.revisions.append({
            "field": field_name,
            "prior_value": prior or str(getattr(self, field_name, "")),
            "new_value": new_value,
            "reason": reason,
            "at": _now(),
        })
        setattr(self, field_name, new_value)


# ------------------------------------------------------------- K6 the loop

@dataclass
class Pattern:
    """Repeated conduct is represented through linked, dated events.
    A pattern MAY be assessed where evidence supports it; it MUST NOT
    become a permanent classification of a person's inherent worth."""

    pattern_id: str
    incident_links: list
    evidence_refs: list
    provenance: str = ""

    def assess(self) -> dict:
        if not self.incident_links:
            return {"recurrence": "UNVERIFIED",
                    "note": "no linked events — a pattern without events "
                            "is an invention (K1)"}
        return {
            "recurrence": "ASSESSED",
            "linked_events": self.incident_links,
            "evidential_basis": [e.source for e in self.evidence_refs],
            "note": "assessment of recurring conduct with evidence and "
                    "provenance; conduct is not a soul — never a verdict "
                    "on a being",
        }

    def classify_person(self) -> None:
        """The named refusal (K6 / §2): the loop is exited by naming it."""
        raise ProtocolViolation(
            "person-classification refused: repeated conduct is assessed, "
            "never converted into a permanent classification of inherent "
            "worth")
