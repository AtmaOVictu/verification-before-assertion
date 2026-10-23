# VBL-VP 1.0 — Verification Protocol

Status: Proposed specification
Governing text: VBL — Verification Before Assertion License, 10.0.0
Purpose: Make ethical commitments inspectable, enforceable within the implementing system, and resistant to self-certification.

⊨ WITH LOVE

> **Kit note (2026-10-23, scars visible, ×):** this body is the proposed
> specification as dictated, with three reconciliations, each measured:
> 1. The draft arrived titled "VBL 10.0.0 — Verification Protocol". The
>    number 10.0.0 already belongs to the license — LICENSE.md @main is
>    10.0.0 (blob 73476d4, the living door). One number must not carry two
>    bodies: the protocol takes its own series, VBL-VP. ×
> 2. "Governing text: …v2.6" was a receipt, not the living door; updated to
>    10.0.0. Earlier versions live in the publication chain, not in this
>    prose (LICENSE §10). ×
> 3. §9 arrived truncated mid-sentence ("Encoding loss: …preserve the
>    relevant"). The final test is reconstructed from §8 and marked ⚠ below.
>
> The implementing module is `vbl_protocol.py`; the acceptance tests are
> `test_vbl_protocol.py` (13 behaviors, 17 tests, each named for the fall
> it guards). Machine-testable means tested, not asserted (L4).

## 0. Foundational rule

No assertion without a witness. No cure without evidence. No verification by the sole executor. No closure that conceals an outstanding fall.

This protocol distinguishes five things that must never be silently substituted for one another:

Assertion — what an actor claims.

Evidence — what a source actually supports.

Finding — what an authorized assessment concludes from the evidence.

Remedy — what must be done in response.

Verification — what an independent check establishes about the remedy.

A claim may be sincere and still be unverified. Evidence may be genuine and still be insufficient. A remedy may be completed and still leave harm that cannot be undone.

The protocol records these distinctions; it does not claim that a clean register is equivalent to justice.

## 1. Scope and authority

VBL 10.0.0 expresses the governing ethical and licensing commitments. This protocol defines machine-testable behavior for systems that explicitly implement it.

The protocol does not, by itself:

establish that a particular user accepted the license;

create ownership of third-party material;

establish that an allegation is true;

guarantee that every remedy is legally enforceable;

authorize a system to override applicable law or valid safety requirements;

establish that reading the text has technically activated a machine.

The implementation MUST distinguish an ethical requirement, a contractual requirement, a system-enforced rule and a verified external fact.

## 2. KORENINA invariants

K1 — Measure before assertion

Every material factual claim MUST identify its supporting evidence or be marked UNVERIFIED.

Evidence references MUST preserve source identity, relevant location, acquisition time where known, and integrity information where available.

Absence of evidence MUST NOT be represented as evidence of absence.

K2 — Preserve every named fall

A correction MUST create a new record linked to the record it corrects.

The system MUST NOT silently overwrite, erase or backdate a prior finding or correction.

A report later found unsupported remains part of the history, with its disposition and supporting rationale recorded. It MUST NOT remain presented as an established fact merely because it was once reported.

K3 — No self-verification

The actor who executes a remedy MUST NOT be its sole verifier.

The verifier MUST have access to the evidence needed to assess the completion criteria and MUST disclose relevant conflicts of interest.

Where genuine independence cannot be established, the result MUST be marked INDEPENDENCE_UNESTABLISHED, not INDEPENDENTLY_VERIFIED.

K4 — Attribution travels with the work

Where attribution is required and the relevant authorship is established, the system MUST record the required credit and the locations where it must appear.

Unknown contributors MUST remain explicitly unknown. Their identities MUST NOT be invented.

Attribution MUST NOT be represented as proof that all other obligations have been discharged.

K5 — Doubt remains visible

Uncertainty, disagreement, missing evidence and incomplete remedies MUST have explicit representations.

The system MUST NOT convert uncertainty into certainty merely to complete a workflow.

K6 — Name the loop

Repeated conduct MUST be represented through linked, dated events with evidence and provenance.

The system MAY assess a recurring pattern where the evidence supports it. It MUST NOT turn that assessment into a permanent classification of a person's inherent worth.

## 3. Evidence and incident records

Each report MUST have a stable identifier and, where applicable, the fields listed in §3 of the dictation: incident_id, reported_at, reporter or an explicitly permitted anonymous identifier, reported_deed, event_time and event_location, affected_material, evidence_refs, evidence_integrity, assessment_status, responsibility_status, impact_assessment, remedy_requirements, correction_links, verification_refs, remaining_obligations, status_history.

Each evidence reference SHOULD include:

source identifier and source location;

verbatim excerpt or a precise description of the relevant evidence;

collection timestamp, if known;

a content digest or equivalent integrity check, where appropriate;

limitations, missing context and known uncertainty;

access and privacy restrictions.

A digest can help detect changes to a file. It does not prove the truth of the file's contents.

The register MUST minimize unnecessary personal data. Public accountability does not justify exposing private information unrelated to establishing or remedying the fall.

## 4. State machine

A report proceeds through explicit states:

REPORTED → TRIAGED → ASSESSED → FINDING_RECORDED → REMEDY_DEFINED → REMEDY_EXECUTED → INDEPENDENTLY_VERIFIED → CLOSED_VERIFIED

The following alternative states MUST be supported where applicable:

NEEDS_EVIDENCE

DISPUTED

UNSUBSTANTIATED

PARTIALLY_REMEDIED

REMEDY_IMPOSSIBLE_OR_LIMITED

INDEPENDENCE_UNESTABLISHED

REOPENED

These states are not interchangeable.

Transition rules:

REPORTED means a report was received, not that the allegation is established.

ASSESSED records the assessment and its evidential basis.

FINDING_RECORDED identifies what was established, what was not established and what remains disputed.

REMEDY_DEFINED specifies the required actions and their completion criteria.

REMEDY_EXECUTED records the executor's evidence of action, not independent confirmation.

INDEPENDENTLY_VERIFIED requires a verifier distinct from the sole executor and evidence satisfying the specified criteria.

CLOSED_VERIFIED is permitted only when all mandatory closure criteria are met or when the record explicitly uses a different, accurately named disposition.

No missing step may be silently inferred from a later state. Reopening a case creates a new event and preserves the prior closure history.

## 5. The cure: tragedy and predation

The protocol preserves the distinction in §4 and §9 of VBL while treating it as an evidence-based assessment of conduct, not a verdict on a being.

### 5.1 Tragedy

Where evidence supports that the harmful pattern has injured the doer as well as others, the assessment SHOULD consider both dimensions.

A remedy plan SHOULD address harm to affected parties, harm to the doer, recurrence prevention and feasible restoration.

Recognition of the doer's suffering MUST NOT erase obligations to other affected parties.

### 5.2 Predation

Where evidence supports that an actor imposed harm on others while retaining a benefit from that harm, the remedy assessment MUST consider:

the benefit obtained or retained;

attribution or recognition that was stripped;

the affected parties and material;

restitution or disgorgement where applicable;

correction of continuing outputs or downstream uses;

evidence needed to establish that the remedy was completed;

any remaining benefit or obligation that cannot yet be resolved.

The classification MUST state its evidential basis and uncertainty. It MUST be open to correction when new evidence materially changes the assessment.

The protocol MUST NOT infer intent solely from an adverse outcome. Intent, knowledge, benefit and recurrence require their own evidential basis.

### 5.3 Remedy accounting

A cure is not complete merely because the responsible actor has published an admission, restored credit or made a payment.

The record MUST distinguish:

remedy_owed

remedy_completed

completion_evidence

independent_verification

remaining_balance

limitations_and_reason

If full repair is impossible, the system MUST record what was achieved, what remains unresolved and why.

A harmed person's silence MUST NOT be treated as consent, forgiveness, satisfaction or proof of repair. The harmed person MUST NOT be made solely responsible for investigating, administering or verifying the remedy.

## 6. Independent verification

A verifier MUST evaluate the declared completion criteria against the available evidence.

The verifier MUST record:

identity or accountable role;

verification time;

scope of review;

evidence examined;

criteria passed and failed;

limitations and conflicts of interest;

decision and rationale.

The verifier MAY conclude that a particular action was completed without concluding that all harm was repaired.

The verifier MUST NOT claim more than the evidence establishes.

Where no suitably independent verifier is available, the system MUST preserve the result as unresolved. It MUST NOT manufacture independence through a second signature from the same accountable actor.

## 7. Publication, permission and version history

The implementation MUST distinguish:

the text of the license;

the version identified by that text;

the publication record;

evidence that a particular party received or accepted particular terms;

the protocol version used to assess a particular event.

A repository commit or signed publication record can support claims about the history and integrity of a published artifact. It does not, by itself, prove acceptance of contractual terms or establish every claim made by the artifact.

Every assessment MUST record the governing license and protocol versions used. Updating the protocol MUST NOT silently rewrite prior findings.

Permission records MUST identify the requested use, requester where appropriate, material, scope, date and decision. Silence MUST NOT be interpreted as permission where the governing terms require affirmative permission.

Any conflict between a proposed permission and a governing restriction MUST be flagged for explicit review rather than silently resolved by the implementation.

## 8. Character integrity and transport

The implementation MUST distinguish the intended text from the text actually received, stored, transformed and emitted.

For text whose integrity matters, it SHOULD record an appropriate encoding, integrity digest and transformation history.

The Unicode replacement character U+FFFD MUST trigger an integrity warning when it appears in a context where replacement may indicate decoding loss. It MUST NOT, by itself, be treated as proof of wrongdoing or intent.

The system MUST preserve original artifacts where legally and technically permissible and record any normalization or conversion that affects the evidence.

A claim of byte-identical transport requires an actual comparison of bytes at the relevant boundaries. It cannot be inferred from visual similarity.

## 9. Acceptance tests

A conforming implementation MUST demonstrate at least the following behaviors:

Unsupported claim: a claim without a supporting witness cannot receive verified status.

Self-verification: an executor cannot independently certify their own remedy.

False closure: an outstanding mandatory remedy prevents CLOSED_VERIFIED.

Attribution only: restored credit does not automatically satisfy restitution requirements.

Payment only: a payment record does not prove the full remedy was completed.

Silent overwrite: changing a finding preserves the prior version and records the correction.

Unsubstantiated report: an unsubstantiated allegation is not presented as an established finding.

Reporter protection: the absence of the original author does not prevent an affected party from submitting a report.

Silence: no response from an affected party is not recorded as forgiveness or satisfaction.

Uncertain intent: the system does not infer premeditated intent solely from harm or benefit.

Missing verifier: a case cannot claim independent verification without a qualified, separate verifier.

Impossible repair: a partially remediated case records its remaining balance and limitations.

Encoding loss ⚠ (reconstructed — the dictation arrived truncated here): suspicious replacement characters produce a warning and preserve the relevant artifact; the warning is evidence of possible decoding loss, never of wrongdoing.

Each behavior is verified by a named test in `test_vbl_protocol.py` — the acceptance list is code, not prose (L4). A conforming implementation runs green; anything else is named, not hidden.
