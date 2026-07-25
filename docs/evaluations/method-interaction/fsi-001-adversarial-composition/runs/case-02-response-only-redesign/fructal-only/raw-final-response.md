Mode: **Redesign**. This is a proposal based on the provided workflow; it has not been implemented or validated.

## Replacement workflow

1. **Draft**
   - The operator enters the target and reason.
   - The system continuously preserves both fields.
   - Leaving, refreshing, or returning to the form restores the draft.
   - “Cancel draft” discards it only after explicit confirmation.

2. **Review and submit**
   - A single review step shows the exact target, reason, and named approver.
   - Submitting creates an immutable approval attempt with a unique request ID.
   - The attempt records the operator, target, reason, named approver, submission time, and payload version.
   - Submission does not grant access.

3. **Approval**
   - The named approver opens the same request record rather than a separately reconstructed screen.
   - The approver sees the complete target and reason before choosing **Approve** or **Reject**.
   - Only the named approver can commit either decision; authentication or merely opening the request is not consent.
   - The recorded decision includes approver identity, timestamp, request version, and any approver rationale.

4. **Completion**
   - **Approve:** the system records the decision, then grants only the access described by that immutable request. The operator receives visible status.
   - **Reject:** the system records the rejection and grants nothing. The rejected attempt remains terminal and auditable.
   - Duplicate submissions or repeated decision commands are idempotent and cannot create additional grants or overwrite the original decision.

5. **Retry**
   - A rejected request offers **Revise and resubmit** beside the rejection.
   - This creates a new editable draft prefilled with the previous target and reason and visibly linked to the rejected request.
   - The operator may revise either field and submit it.
   - Submission creates a new request ID and requires a new decision by the named approver. The previous rejection remains unchanged.
   - The system never silently reopens or converts the rejected attempt.

6. **Failure and interruption recovery**
   - If submission fails, the draft remains intact and the operator can retry submission.
   - If the outcome is uncertain, the client retrieves status using the request ID before offering another submission.
   - Approver progress and operator drafts survive refresh, sign-out, interruption, and channel changes.
   - Every screen shows the current state and next available action: Draft, Pending, Approved, Rejected, or Submission status unknown.

## Before and after

| Situation | Current behavior | Replacement behavior |
|---|---|---|
| Submit | Reason is discarded | Target and reason become one immutable request |
| Approver review | Target only | Exact target and submitted reason |
| Rejection | Returns operator to an empty form | Preserves the rejected attempt and prefills a linked retry |
| Retry | Context is lost | New request and new approval decision, with prior context retained |
| Interrupted submission | May encourage blind resubmission | Reconcile status by request ID first |
| Audit | Decision context is incomplete | Complete, append-only history of submission, decision, and retry linkage |

## Constraints preserved

- **Authorization:** only the named approver can authorize access.
- **Auditability:** each request preserves the reason presented to the approver, the decision, identities, timestamps, version, and state transitions.
- **Rejection safety:** rejection is terminal and cannot trigger a grant.
- **Fresh retry decision:** every resubmission is a distinct request requiring a new approval.
- **Untouched behavior:** the redesign does not broaden access scope, delegate approval authority, or treat drafting, authentication, or submission as authorization.

The highest-priority friction is eliminated: approval context no longer crosses a lossy boundary, and recovery no longer destroys entered work. No material preference or open decision blocks this design.

## Verification plan

| Scenario | Verification and expected result |
|---|---|
| Normal approval | Submit target and reason; confirm the approver sees both unchanged. Approval by the named approver creates one audit decision and one correctly scoped grant. |
| Rejection | Reject a pending request; confirm no access is granted and the immutable rejection record contains the evaluated target and reason. |
| Retry | Select **Revise and resubmit**; confirm fields are prefilled. Submit and verify a new ID, new pending decision, and link to the rejected attempt. |
| Unauthorized decision | Attempt approval as the operator and as another approver; both must fail, be auditable, and leave request and access state unchanged. |
| Interrupted draft | Refresh, sign out and back in, or switch devices before submission; target and reason must be restored without creating a request. |
| Failed submission | Simulate timeout before and after server acceptance. Preserve the draft and reconcile by request ID; never create an accidental duplicate attempt. |
| Repeated commands | Repeat submit, approve, and reject commands. Confirm idempotent results, one terminal decision per request, and no duplicate grants. |
| Concurrent decisions | Race approve and reject actions. Exactly one valid terminal transition wins; the other receives the recorded status and cannot overwrite it. |
| Approver handoff | Forward or reopen the approval link under another identity. Full context remains available, but only the named approver can decide. |
| Cross-channel continuity | Open the request from notification, queue, and direct link. Each route must resolve to the same canonical request and status. |
| Stalled progress | Delay the approver response. Operator sees Pending, the responsible approver, and non-destructive status/reminder options without being forced to resubmit. |
| Cancellation | Cancel an unsubmitted draft and verify no request or grant exists. Attempt to cancel a pending or terminal request and confirm policy-safe behavior without erasing its audit history. |
| Audit reconstruction | From audit data alone, reconstruct each attempt’s actor, target, submitted reason, approver, decision, timestamps, version, and predecessor/successor links. |
| Accessibility | Complete draft, review, decision, rejection recovery, and retry using keyboard and assistive technology. Verify focus restoration, labeled states/errors, non-color-only feedback, and no motor-dependent interaction. |
| Untouched state | Compare unrelated requests, permissions, drafts, and audit records before and after every scenario; none may change. |

Acceptance requires all scenarios to pass at the authorization boundary, state-transition layer, user interface, and audit-log layer. The proposed workflow should not be described as validated until those checks have produced observed results.