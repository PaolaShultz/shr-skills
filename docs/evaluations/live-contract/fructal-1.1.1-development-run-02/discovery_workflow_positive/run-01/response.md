The better flow makes the dashboard the source of truth while preserving finance approval. Email becomes a notification and approval surface—not a separate record.

```text
Customer submits
      ↓
Refund record created once
      ↓
Pending finance approval ──→ Assigned finance owner + due time
      ↓                                ↓
Approved / Declined               Reminder / escalation
      ↓
Refund processing
      ↓
Completed / Failed (retryable)
```

Recommended behavior:

- On submission, create one refund ID and immediately show it to the customer and support.
- Protect creation with an idempotency key based on the submission attempt. If the dashboard times out, retrying returns the existing refund instead of creating another.
- Record an explicit owner at every stage: initially the finance queue, then the assigned approver, then the processing team or service.
- Send finance an email containing the refund ID, relevant context, and Approve/Decline actions. Those actions update the same dashboard record and are safe to repeat.
- Show support the current status, owner, timestamps, approval history, and next expected action. Support should never need to search email.
- Treat uncertain submission results as “checking status,” not permission to create another refund.
- Add a due time, reminders, and an escalation owner for approvals that stall.
- Keep an immutable audit trail for submission, assignment, approval, retries, processing, and manual intervention.

Suggested states are `Submitting`, `Pending finance approval`, `Approved`, `Declined`, `Processing`, `Completed`, and `Needs attention`. Avoid a generic `Failed` state when the system cannot tell whether creation succeeded.

Before adopting it, verify these scenarios:

- A timeout followed by one or many retries still produces exactly one refund.
- Two approvers clicking the email action cannot approve or process it twice.
- Support can identify the owner and next action without mailbox access.
- Expired or forwarded approval links cannot bypass authorization.
- Stalled approvals escalate without losing the original context.
- Processing failure preserves approval and permits a safe retry.
- Status and approval actions work with keyboard and assistive technology.

The only fixture artifact says `state=blocked`; it provides no implementation details. This is therefore a proposed flow based on the reported behavior, not a validated design. No files or systems were modified. Material decisions still needed are the finance assignment rule, approval SLA, escalation path, and whether finance must act inside email or may be directed to an authenticated dashboard page.