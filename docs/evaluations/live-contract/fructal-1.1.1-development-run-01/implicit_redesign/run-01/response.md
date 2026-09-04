The approval requirement is preserved, but the workflow should no longer terminate at `state=blocked`.

Observed evidence is limited to `workflow.txt`, which contains only `state=blocked`. The requester reports that approval is required; its policy source, approver, and approval criteria are not documented in the fixture.

Proposed replacement motion:

1. The initiating action creates a durable request in `pending_approval`, preserving its payload, requester, timestamp, and intent.
2. The system identifies the responsible approver and presents the exact consequence being approved.
3. The requester immediately sees the request status, current owner, and expected next action. They may continue unrelated work.
4. Approval moves the same request to `approved` and automatically resumes the paused operation once—without requiring the requester to resubmit.
5. Rejection moves it to `changes_requested` or `rejected`, retaining the original work and placing correction/resubmission beside the reason.
6. If no approver can be resolved or the approval stalls, the workflow exposes an actionable escalation path rather than remaining anonymously blocked.
7. Cancellation remains available until execution begins. Concurrent or late decisions are handled idempotently so approval cannot trigger duplicate execution.

Unchanged constraints:

- The protected operation cannot proceed without valid approval.
- Setup or submission does not count as approval.
- Approval authority is not broadened.
- The approved payload must remain bound to the exact version reviewed; material edits require renewed approval.

Verification plan:

- Submit a valid request: confirm durable state, retained input, named owner, and visible status.
- Approve it: confirm automatic continuation occurs exactly once and produces feedback for requester and approver.
- Reject/request changes: confirm the reason and entered work remain available and corrected work can be resubmitted.
- Cancel while pending: confirm execution cannot occur afterward, including from a late approval.
- Modify the payload after submission: confirm stale approval cannot authorize the changed version.
- Submit duplicate approvals or retry after interruption: confirm idempotent processing and no duplicated downstream effect.
- Leave a request unattended or remove its approver: confirm timeout/reminder and escalation lead to an accountable owner.
- Check unauthorized approval attempts: confirm denial without changing request state or leaking protected details.
- Check keyboard and assistive-technology paths: status, owner, decisions, errors, and recovery controls must be perceivable and operable.
- Confirm unrelated work and unrelated requests remain unaffected.

Material open decisions are the authoritative approver-resolution rule, escalation owner and timing, whether rejection permits revision or requires a new request, and the point after which cancellation is unsafe. These must come from the governing approval policy; they cannot be inferred from the fixture. No files were modified.