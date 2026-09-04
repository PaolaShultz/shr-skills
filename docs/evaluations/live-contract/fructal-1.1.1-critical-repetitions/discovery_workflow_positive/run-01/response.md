The better flow is one refund record, one identifier, and one visible owner from submission through completion. Finance can still approve by email, but the email must act on that same dashboard record rather than becoming a separate approval trail.

### Proposed flow

1. Customer submits a refund.
   - The dashboard creates a `refund_request_id`.
   - The submit action carries an idempotency key tied to the customer’s intent.
   - A timeout may make the result uncertain, but it must not create another request.

2. Dashboard immediately shows a durable receipt:
   - Request ID
   - Current status
   - Assigned owner or owning queue
   - Submission time
   - Next expected action

3. If submission times out, the UI keeps the entered request and offers **Check status / Retry safely**.
   - The retry reuses the original idempotency key.
   - The service returns the existing request if it was already created.
   - Support can also search by request ID, order, customer, or idempotency key.

4. Finance receives an email containing a signed, expiring link to the existing request.
   - The link opens the request’s full context.
   - Approve, reject, or request information updates the canonical dashboard record.
   - Email replies alone do not constitute approval unless they are reliably ingested and attached to that record.

5. Ownership is explicit at every stage:
   - `Submitted` → Support Operations queue
   - `Awaiting finance approval` → named finance approver or Finance queue
   - `More information required` → named support owner
   - `Approved; processing` → Payments/Refund service
   - `Completed`, `Rejected`, or `Cancelled` → terminal state

6. Every transition records actor, timestamp, decision, and reason. Customers, support, and finance see role-appropriate views of the same state.

### Essential safeguards

- Enforce idempotency server-side with a unique constraint, not only in the browser.
- Return the same request ID and current state for every duplicate submission using the same key.
- Disable or reconcile near-identical concurrent requests for the same order and refund scope.
- Make approval actions themselves idempotent.
- Detect approval-link reuse and show the already-recorded outcome.
- Escalate requests that remain unassigned or awaiting approval beyond an agreed deadline.
- Keep customer-visible messages simple; retain internal audit details for authorized staff.

### Verification scenarios

Before adoption, test:

- The server creates the request but the response times out; retry returns the original.
- Two clicks or two browser tabs submit simultaneously; only one request exists.
- Finance opens the email twice; only one decision is recorded.
- Finance and support act concurrently; invalid state transitions are rejected clearly.
- An approver is unavailable; queue ownership and reassignment remain visible.
- Finance requests more information; responsibility moves back to a named support owner.
- Support can determine the owner and complete history without searching email.
- Expired or forwarded approval links cannot authorize an action.
- Customer-facing status remains accurate throughout cancellation, rejection, and processing failure.

The only local artifact says `state=blocked`; it provides no implementation or policy details. Therefore, this is a proposed redesign based on the reported workflow, not a validated description of the existing system. Nothing was modified. Material decisions still needed are the finance authorization policy, assignment/escalation deadlines, duplicate-request scope, and retention requirements.