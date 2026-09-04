The fixture only confirms `state=blocked`; the detailed current behavior comes from your description. No files or systems were modified.

Proposed flow:

1. Customer submits once in the dashboard.
2. The system immediately creates a refund request with a durable request ID and shows it to the customer and support.
3. The request enters `Awaiting finance approval` and is assigned to a named finance queue or owner.
4. Finance receives an email containing a link to the same dashboard record. Email is notification, not a separate approval record.
5. Finance approves or rejects in the dashboard. The decision, actor, timestamp, and reason are recorded.
6. After approval, refund processing runs once. Support and the customer see the resulting status and any recovery action.

Use a state model such as:

`Submitted → Awaiting finance approval → Approved → Processing → Refunded`

With explicit alternatives:

- `Rejected`
- `Needs information`
- `Processing failed — safe to retry`
- `Cancelled`

Duplicate prevention:

- Generate an idempotency key when submission begins and reuse it for retries.
- Enforce uniqueness server-side, ideally using customer/order, refund scope, amount, and request intent.
- If a retry matches an existing request, return that request instead of creating another.
- Disable repeated submission while the result is unknown, but provide “Check status” and a safe retry path.
- Make refund execution itself idempotent; approval retries must never issue payment twice.

Ownership and visibility:

- Every nonterminal request must have one accountable owner: a person or an explicitly staffed queue.
- Show owner, current state, age, last action, and next required action on the support view.
- Set an approval deadline with reminders and escalation to a backup finance queue.
- Preserve a single audit trail across customer submission, finance decision, support intervention, retries, and payment-provider responses.
- Restrict financial decisions to authorized finance users while keeping status readable by support.

Key product behavior: after a timeout, tell the customer, “We couldn’t confirm the result. Your request ID is R-123; checking status…” The system should reconcile that ID before offering another submission.

Before implementation, resolve three policy decisions: who owns the finance queue, when overdue requests escalate, and which fields define “the same refund.” Then verify with timeout-before-response, repeated clicks, concurrent retries, delayed approval email, reassignment, provider timeout, and double-approval scenarios. The critical acceptance condition is that every attempt resolves to one inspectable request and, at most, one refund.