The fixture only confirms `state=blocked`; no implementation details were available. Based on the reported workflow, the dashboard should become the system of record while email remains the finance notification and action channel.

### Proposed flow

1. **Create once**
   - The dashboard generates a persistent idempotency key before submission.
   - Every retry reuses that key.
   - The backend atomically creates the refund or returns the existing request.
   - A timeout leads to “checking status,” not another independent submission.

2. **Assign ownership immediately**
   - Each request records:
     - Request ID
     - Current state
     - Owning team and named owner
     - Submitted/updated timestamps
     - Required next action
     - Approval deadline
   - Support can search by customer, order, or request ID and see who must act next.

3. **Keep approval in email without splitting state**
   - Finance receives an email containing the request ID, relevant context, deadline, and authenticated **Approve** / **Reject** links.
   - Those actions update the same dashboard record.
   - Email replies are not the approval record unless reliably ingested and authenticated.
   - Repeated or stale approval actions return the current result instead of acting twice.

4. **Use an explicit lifecycle**
   - `Submitted → Awaiting finance → Approved → Refund processing → Refunded`
   - Alternate states: `Rejected`, `Failed—retryable`, `Cancelled`, and `Needs review`.
   - Every state names its owner and permissible next action.
   - A stalled approval triggers reminders and then escalation to a backup finance owner.

5. **Make recovery visible**
   - After submission, show the request ID immediately.
   - If the response times out, retain the form and display: “We’re checking whether request RF-123 was received.”
   - Processing retries operate against the existing refund record and payment-provider idempotency key.
   - Support sees an event history covering submission, assignment, emails, approval, retries, and completion.

### Key controls

- Use separate stable idempotency keys for request creation and payment execution.
- Enforce uniqueness transactionally; UI button disabling alone is insufficient.
- Never infer approval from an email being delivered or opened.
- Require authenticated authorization for finance decisions and retain an audit trail.
- Redact sensitive customer/payment data from email; link back to controlled details.
- Use compare-and-set/version checks so approval, cancellation, and retries cannot overwrite newer decisions.

### Verification plan

Test:

- Normal approval through email.
- Submission timeout followed by several retries.
- Two browser tabs submitting the same persisted request key.
- Finance clicking Approve twice, or approving after rejection/cancellation.
- Payment-provider timeout followed by processing retry.
- Primary owner absent and escalation activated.
- Support locating the request and identifying the current owner.
- Email delivery failure without losing the dashboard request.
- Keyboard and screen-reader use for status, recovery, and approval actions.

Success means one logical request, at most one payment refund, a visible owner in every actionable state, and a complete audit trail.

Open decisions are the finance routing rules, approval deadline, escalation owner, whether multiple legitimate partial refunds per order are allowed, and the authentication mechanism behind email actions. No files or systems were modified.