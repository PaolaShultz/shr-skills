The better flow keeps finance approval, but makes the dashboard the source of truth. Email becomes a notification channel, not a separate approval system.

### Proposed flow

1. **Customer submits once**
   - The client creates a stable idempotency key for the submission.
   - The backend atomically creates or returns the existing refund request for that key.
   - A timeout leaves the request in “checking submission” rather than inviting a blind duplicate.
   - Retrying with the same key returns the original request and current status.

2. **Ownership is assigned immediately**
   - Every request has one visible accountable owner: initially the Finance Approval queue, then a named approver when claimed.
   - Support can see the request ID, owner, status, timestamps, amount, and latest action.
   - Reassignment and escalation are recorded in an audit trail.

3. **Finance receives an email notification**
   - The email contains request context and a secure link to the canonical dashboard record.
   - Approval or rejection happens against that record, with current authorization checked at action time.
   - If email-based buttons are unavoidable, they invoke the same idempotent approval command and show the resulting dashboard state.

4. **One explicit state progression**

   `Submitted → Awaiting finance → In review → Approved/Rejected → Refund processing → Completed/Failed`

   Exceptional states should be explicit: `Needs information`, `Cancelled`, and `Escalated`. Each state displays its owner and next action.

5. **Recovery stays attached to the request**
   - Processing retries reuse the same refund request and payment-operation key.
   - An ambiguous payment-provider timeout becomes “processing—outcome unknown” while reconciliation checks the original operation.
   - Only a confirmed failure enables retry.
   - Customers and support receive updates from the same recorded state.

### Essential safeguards

- Enforce uniqueness server-side using an idempotency key or stable business key; UI button disabling alone is insufficient.
- Make customer-submission deduplication and payment-provider deduplication separate protections.
- Use conditional state transitions so two approvers cannot independently approve the same request.
- Record actor, timestamp, previous state, new state, and reason for every transition.
- Alert on unclaimed or stalled requests using an agreed finance SLA.
- Do not expose sensitive financial or customer details unnecessarily in email.

### Verification scenarios

Before adoption, verify:

- A timed-out submission followed by multiple retries produces one request.
- Two genuinely separate refund requests are not incorrectly merged.
- Concurrent approval attempts produce one transition and a clear “already handled” result.
- Support can identify the current owner and next action at every non-terminal state.
- Stalled and reassigned requests retain their history and customer context.
- A provider timeout cannot initiate a second refund until the original outcome is reconciled.
- Expired, forwarded, or unauthorized email links cannot approve a request.
- Customer, support, finance, and payment records converge on the same terminal outcome.

The fixture only records `state=blocked`, so this is a proposed design rather than a validated description of the existing implementation. No files, systems, or external services were modified. Before implementation, the main decisions to settle are the finance assignment policy, approval SLA/escalation path, deduplication window or business key, and whether approval must occur inside the dashboard.