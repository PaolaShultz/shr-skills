The fixture confirms only that the workflow is currently `blocked`; the duplicate and ownership problems are requester-reported and not independently observable from the available artifact ([workflow.txt](/tmp/fructal-eval-discovery_workflow_positive-01-47g926ki/fixture/workflow.txt:1)).

A better flow:

1. **Submission creates one durable refund case**
   - Generate a stable `refund_request_id`.
   - Disable repeat submission while the first request is unresolved.
   - If the dashboard times out, “Retry” checks that same ID instead of creating another request.
   - Server-side idempotency should provide the real duplicate protection.

2. **The dashboard becomes the source of truth**
   - Show a clear lifecycle: `Submitted → Awaiting finance → Approved/Rejected → Processing → Refunded`.
   - Display the current owner, submission time, amount, and last activity.
   - Support can search by customer, order, or refund ID.

3. **Email becomes an approval surface, not a separate workflow**
   - Finance receives an email containing the refund ID, context, and a secure approve/reject link.
   - The decision updates the same dashboard case.
   - Replies or repeated link use cannot create another request or apply approval twice.

4. **Ownership is explicit at every handoff**
   - `Awaiting finance` is owned by the finance queue or a named approver.
   - After approval, ownership moves to the refund-processing service or designated team.
   - Rejection returns ownership to support with a visible reason.
   - Overdue approvals follow a defined escalation path; they never become silently ownerless.

5. **Recovery stays beside the failure**
   - After a timeout, show: “Submission status unknown—checking request RF-123.”
   - Resolve that check to either the existing case or a safe resubmission using the same idempotency key.
   - Preserve all entered information and give support a visible event history.

Important safeguards:

- Enforce uniqueness for the intended refund scope, commonly order/payment plus refund amount or a client-generated idempotency key.
- Record immutable audit events for submission, assignment, reminders, decisions, retries, and processing.
- Require authenticated, authorized approval; email possession alone should not grant authority.
- Make concurrent, stale, and repeated approval actions harmless and clearly reported.

Verification should cover normal approval, dashboard timeout before and after persistence, double-clicks, simultaneous retries, repeated email-link use, reassignment, rejection, overdue escalation, and support lookup. Also verify keyboard and assistive-technology access to status and recovery controls.

Open decisions are the duplicate scope (one refund per order versus partial refunds), finance escalation timing, and whether ownership is queue-based or individually assigned. No files or systems were modified, and this proposal has not been validated against an implementation.

Applied the workflow-continuity method from [Fructal Cap Design](/tmp/fructal-eval-discovery_workflow_positive-01-47g926ki/executor-state/codex-home/skills/fructal/SKILL.md).