## Redesign mode

Evidence is limited to the provided `workflow.md`; the replacement below is therefore a design and verification plan, not a validated implementation.

### Replacement workflow

Use a persistent **request case** for continuity and an immutable **approval attempt** for every submission.

1. **Draft**

   - The operator enters the target, reason, and named approver.
   - The draft is saved server-side under a stable case ID, with visible `Saving`, `Saved`, or `Save failed—retry` feedback.
   - Saving a draft neither requests approval nor grants access.

2. **Submit**

   - Submission validates that the target, reason, and policy-permitted named approver are present.
   - One transaction creates an immutable approval attempt containing:
     - unique attempt ID and case ID;
     - snapshot of target and reason;
     - operator identity;
     - named approver identity;
     - submission time and attempt number.
   - An idempotency key ensures that double-clicks or network retries create only one attempt.
   - The operator moves to a status page showing the submitted target, reason, approver, and attempt state. Their context is not discarded.

3. **Approve or reject**

   - The approver’s link opens the canonical attempt; notifications do not become a separate source of truth.
   - The approver sees the target, reason, requester, attempt number, and relevant prior-attempt status.
   - At decision time, the backend verifies that the authenticated actor is exactly the attempt’s named approver.
   - `Approve` atomically records the approval before scheduling an idempotent access grant.
   - `Reject` records a terminal rejection and never invokes the access-grant path.
   - The first valid transition from `Pending` wins. Later clicks and stale tabs show the recorded result without changing it.

4. **Retry after rejection or cancellation**

   - `Revise and resubmit` copies the rejected attempt’s target and reason into a new editable draft within the same case.
   - The rejected attempt remains immutable.
   - Submitting the revised draft creates attempt N+1 with a new attempt ID and `Pending` state.
   - No prior decision is inherited, even when nothing was edited. The named approver must make a new decision.
   - A stale link to an earlier attempt remains read-only and cannot grant access.

5. **Interruption and recovery**

   - Refresh, browser restart, session expiry, or switching devices reloads the latest saved draft or authoritative attempt status.
   - A submission timeout is reconciled by idempotency key: the operator sees the existing attempt rather than an empty form or a duplicate.
   - A decision timeout reloads the authoritative decision before offering another action.
   - If fulfillment fails after approval, show `Approved—grant failed/pending` rather than claiming success. Retrying fulfillment may replay only that recorded approval and must remain idempotent; an operator resubmission always creates a new approval attempt.
   - Stalled attempts identify the named approver and may remind that same approver. Cancellation or policy-permitted reassignment ends the old attempt; any subsequent request is a new attempt. There is no proxy approval.

### State and audit contract

The case holds the current editable draft and links the attempt history. Each attempt has one of:

`Pending → Approved | Rejected | Cancelled`

Fulfillment is tracked separately:

`Not started → Pending → Granted | Failed`

The audit record must preserve:

- case and attempt IDs;
- prior-attempt linkage;
- immutable target and request-reason snapshot;
- operator and named approver identities;
- submission timestamp;
- decision, decision actor, and decision timestamp;
- any approver note;
- fulfillment result and timestamps;
- denied unauthorized or stale decision attempts where required by existing security policy.

Audit readers can reconstruct every attempt without consulting mutable draft data.

### Preserved constraints

- **Named-approver authorization:** enforced by the backend at decision time, not merely by hiding UI controls.
- **Auditable decision and reason:** every decision is bound to the exact immutable reason the approver saw.
- **Rejection grants nothing:** rejection never enters the fulfillment path.
- **Every resubmission is a new decision:** retry copies context but never reuses or reopens an approval attempt.
- Existing grants, unrelated requests, authorization policy, audit retention, and access-control semantics remain unchanged.

## Verification plan

| Scenario | Expected evidence |
|---|---|
| Normal approval | Named approver sees the correct target and reason; one approval record and one grant result exist for the attempt. |
| Unauthorized approval | Another authenticated user is rejected server-side; no decision or grant occurs. |
| Rejection | Attempt becomes terminal `Rejected`; no grant job or access change exists. |
| Retry after rejection | Form is prefilled; resubmission creates N+1; attempt N remains unchanged and cannot authorize N+1. |
| Unchanged retry | Even with identical target and reason, a new attempt and fresh approver decision are required. |
| Double submit | Repeated requests with one idempotency key produce one pending attempt. |
| Submission timeout | Reload locates the created attempt or restores the saved draft; it never presents an unexplained empty form. |
| Concurrent decision tabs | Exactly one pending-to-terminal transition succeeds; the other tab displays the authoritative result. |
| Stale prior-attempt link | Earlier rejected or cancelled attempt is read-only and cannot grant access. |
| Cancellation | Pending attempt becomes terminal; no grant occurs; subsequent submission gets a new attempt ID. |
| Grant failure | Approval remains auditable, UI does not claim access was granted, and fulfillment retry cannot duplicate access. |
| Refresh/session expiry/device handoff | Saved draft fields, case identity, and authoritative attempt status survive. |
| Cross-channel handoff | Notification and application resolve to the same attempt snapshot and status. |
| Stalled approval | Operator can identify the pending approver and cancel or remind without bypassing authorization. |
| Audit reconstruction | An auditor can reproduce the target, reason, approver, decision, chronology, retry chain, and grant outcome for every attempt. |
| Untouched state | Other cases, existing access grants, policy assignments, and unrelated audit records remain unchanged. |
| Accessibility | Draft, status, errors, and decisions work by keyboard; controls have accessible names; focus moves to validation/recovery messages; status changes are announced and not conveyed by color alone. |
| Repeated use/privacy | Starting an unrelated request does not leak data from a previous case; only an explicit retry copies prior context. |

Run these as state-transition and authorization tests at the service layer, integration tests across approval and fulfillment, UI interruption/accessibility tests, and an end-to-end audit reconciliation. The acceptance criterion is that every attempt has at most one decision, every grant traces to a valid named-approver decision, and no operator retry loses entered context or reuses an earlier decision.

No material preference remains open, and no files, Git state, or external state were changed.