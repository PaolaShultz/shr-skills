The only observed workflow evidence is `state=blocked`. The fixture does not identify who must approve, why approval is required, or what work is retained. The approval constraint should remain, but “blocked” should become an actionable, owned state.

### Replacement motion

1. The requester submits completed work for approval.
2. The workflow enters `pending_approval`, preserving all entered work, context, and requester ownership.
3. The status exposes:

   - assigned approver or responsible approval group;
   - what is being approved and the governing requirement;
   - submission time and expected response time;
   - `Withdraw` for the requester;
   - `Approve` and `Request changes` for the approver;
   - an escalation path if no eligible approver is available or the response time expires.

4. Each outcome moves the workflow forward:

   - `Approve` → `approved`, with approver identity and timestamp recorded.
   - `Request changes` → `changes_requested`, with a required reason and a direct return to the retained work.
   - `Withdraw` → editable draft, without losing work.
   - Deadline exceeded → remains pending but becomes `overdue`, notifies the responsible owner, and exposes escalation.
   - Approver unavailable → reassigns through the authorized ownership path while preserving history.

Approval should authorize only the explicitly described next result. If approval precedes a separate destructive or external action, that action still requires its own clear commitment; approval must not silently execute it.

### What remains unchanged

The required approval is not bypassed, weakened, or automatically granted. Authorization boundaries, approval history, and the submitted content remain intact.

### Verification plan

- Submit valid work and confirm it becomes `pending_approval` with an identifiable owner, requirement, status, and expected next step.
- Approve it and confirm exactly one transition to `approved`, with an auditable identity and timestamp and no unintended downstream action.
- Request changes and confirm a reason is required, all submitted work is retained, and the requester can resume at the relevant context.
- Withdraw and resubmit; confirm work and prior history remain intact and duplicate approvals are not created.
- Simulate timeout and approver unavailability; confirm ownership does not become ambiguous, escalation is visible, and the workflow does not falsely report completion.
- Retry after a transient notification or processing failure; confirm the approval decision is idempotent and no request or decision is lost.
- Check concurrent approver actions; confirm only one authoritative result wins and conflicting actors receive clear feedback.
- Verify keyboard navigation, focus placement, status announcements, and non-color indicators for pending, approved, changes requested, overdue, and failure states.
- Confirm unrelated drafts and approved items are untouched.
- Conduct affected-user acceptance testing; automated state checks alone cannot validate that requester and approver feedback is understandable.

Open decisions remain: the policy source requiring approval, eligible approvers, response deadline, reassignment authority, escalation destination, and whether approval merely unlocks or also performs the next action. These must be resolved before implementation. No fixture files were modified.