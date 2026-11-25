Use one dashboard record per refund request. Give it a stable request ID, a visible owner, and a clear next action. Finance can still receive an email, but the link should open the request where Finance records its decision.

| Stage | Owner | Next action |
|---|---|---|
| Awaiting Finance approval | Named Finance reviewer | Approve or decline and record the reason. |
| Approved, awaiting payment | Assigned payments owner | Issue the refund and track the payment result. |
| Payment outcome unknown | Same payments owner | Reconcile the original payment attempt before retrying. |
| Refunded or declined | Last owner remains visible | Show the customer the outcome and retain the decision history for support. |

**Make retries safe at both steps.** Generate a submission key before the customer first clicks Submit and reuse it after a timeout. Enforce uniqueness on the server so even simultaneous retries return the same request ID. Once Finance approves, use that request ID as the payment provider’s idempotency key. If the provider cannot deduplicate retries, keep an uncertain payment with its owner until they verify the outcome.

**Make handoffs explicit.** Update the stage and owner together, and log who made the change and when. Support can then look up the request ID and answer three questions from one screen: who owns it, what happened last, and what happens next.

The fixture contained only `state=blocked`, so the stages and roles above are proposed. Nothing was modified.