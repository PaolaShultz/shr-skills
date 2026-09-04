The required approval remains intact, but the workflow should become an owned, recoverable waiting motion rather than an opaque blocked state.

### Replacement motion

1. When approval becomes necessary, preserve the submitted work and create an approval request containing:

   - Requester and responsible approver
   - Exact decision and consequences
   - Submission time and response deadline
   - Stable reference to the retained workflow state

2. Replace `blocked` with an inspectable state such as `awaiting_approval`. Notify both actors and show the requester who owns the next action and when follow-up occurs.

3. The approver can approve, reject with a reason, or request changes:

   - **Approve:** resume automatically from the retained checkpoint.
   - **Reject:** return the workflow to the requester with the reason and retained work.
   - **Request changes:** reopen the relevant input without losing context.

4. If the deadline passes, send a reminder and route the request to a designated backup or escalation owner. Never approve implicitly.

5. Allow the requester to cancel or revise a pending request. Revision should supersede the old request clearly, preventing a stale approval from advancing changed work.

The exact approver, deadline, and escalation owner are policy decisions not present in the fixture.

### Verification plan

- Confirm submission creates one approval request and preserves all entered work.
- Confirm approval resumes from the checkpoint exactly once.
- Confirm rejection and change requests return their reason alongside editable retained work.
- Confirm cancellation prevents later approval from advancing the workflow.
- Confirm revision invalidates the prior approval request.
- Confirm reminders and escalation occur at configured deadlines without bypassing approval.
- Confirm duplicate or delayed responses are idempotent and visibly marked stale.
- Confirm requester and approver can inspect current status, ownership, timestamps, and decision history.
- Confirm notifications and controls work through keyboard and assistive-technology paths, with status not conveyed by color alone.
- Confirm unrelated workflow state remains unchanged.

This is a proposed design based on the provided `state=blocked` artifact and the reported approval requirement; it has not been implemented or validated with affected actors, and the fixture was not modified.