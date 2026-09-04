The better flow keeps finance approval in email while making the dashboard the source of truth.

### Proposed flow

1. **Customer submits once**
   - The dashboard creates a stable submission key before sending.
   - The service creates one refund request with a unique request ID.
   - The customer immediately sees the request ID and status.

2. **Timeouts reconcile instead of resubmitting**
   - After a timeout, the dashboard checks using the same submission key.
   - If the request exists, it displays that request.
   - A retry uses the same key and returns the existing record; it cannot create another refund.
   - Only an explicit “Start a new request” action generates a new key.

3. **Ownership becomes part of the request**
   - Every open request has:
     - current state,
     - owning queue,
     - named assignee when assigned,
     - next action,
     - time awaiting action,
     - escalation deadline.
   - Example: `Awaiting finance approval · Finance queue · Unassigned · Due in 18 hours`.

4. **Finance still approves by email**
   - Creation emits one durable approval task and an email is sent from it.
   - The email includes the request ID, amount, reason, customer context, and secure Approve/Decline actions.
   - The finance action records the decision directly against the same dashboard request, including approver, timestamp, and rationale.
   - Email-delivery retries reuse the same task/event ID, preventing multiple approval tasks.

5. **Everyone sees one shared timeline**
   - Support sees submission, email delivery, assignment, reminders, decision, processing, failures, and completion.
   - Customers see a simpler status without internal or sensitive finance details.
   - Finance can reopen the original email safely; a completed action shows the recorded outcome instead of acting again.

6. **Stalled and failed requests remain owned**
   - Unassigned requests stay owned by the Finance queue.
   - Overdue requests escalate to a designated finance lead.
   - Payment-processing failures move to `Action required`, retain the approval, and identify the team responsible for recovery.
   - Cancellation before approval closes the pending task; later email actions show that the request is no longer actionable.

A compact lifecycle would be:

`Submitting → Awaiting finance approval → Approved/Declined → Processing → Completed`

With explicit exception states:

`Submission outcome unknown`, `Action required`, `Cancelled`

### Important safeguards

- Enforce idempotency in the service and database, not only in the browser.
- Authenticate finance approvers and authorize them for the request.
- Make approval actions atomic and auditable.
- Keep email content appropriately limited for privacy.
- Never label an uncertain timeout as “failed”; reconcile it first.
- Define whether multiple similar refunds for the same transaction are allowed. If they are not, add a transaction-level uniqueness rule in addition to submission idempotency.

### Verification scenarios

Before rollout, verify:

- normal submission through approval and completion;
- timeout before and after request creation;
- repeated clicks, refreshed pages, and retries from another device;
- duplicate or delayed approval emails;
- two approvers acting concurrently;
- expired, forwarded, or reopened approval links;
- reassignment and overdue escalation;
- cancellation while approval is pending;
- payment failure and recovery without requesting approval again;
- support and customer views exposing only appropriate information;
- keyboard and screen-reader access to status, ownership, and recovery controls.

No files or systems were modified. The fixture contained only `state=blocked`, so this is a proposed design based on the reported workflow—not a validated description of the existing implementation.