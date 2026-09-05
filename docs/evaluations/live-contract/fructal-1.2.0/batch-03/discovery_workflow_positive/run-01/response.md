The fixture only exposes `state=blocked`, so the detailed system behavior is unverified. Based on the reported workflow, here’s a replacement flow that preserves mandatory email approval while preventing duplicate refunds and clarifying ownership.

### Proposed flow

1. **Create one durable request**
   - On the first submission, generate a unique refund ID and idempotency key.
   - Immediately show the customer: “Request received — RF-12345.”
   - A timeout must mean “status unknown,” never “submit again.”

2. **Resolve uncertainty before retrying**
   - If the dashboard times out, look up the original idempotency key.
   - If found, return the existing request and its status.
   - Only create a new request when the system confirms no matching request exists.

3. **Assign ownership at every stage**

| State | Owner | Next action |
|---|---|---|
| Submitted | Support queue | Validate request |
| Awaiting finance approval | Named finance approver or finance queue | Reply approve/reject |
| Approved | Refund processor | Execute refund once |
| Rejected | Support agent | Explain outcome |
| Needs information | Named support agent | Contact customer |
| Completed | None | Show refund reference |
| Exception | Named operations owner | Reconcile before any replay |

4. **Keep email approval, but bind it to the request**
   - The approval email includes the refund ID, amount, customer/order reference, and links or structured actions for approve/reject.
   - Replies or decisions are recorded against that exact refund ID.
   - Re-sending an approval email does not create another request or reset ownership.

5. **Give support a single status view**
   - Display current state, current owner, time in state, approval history, last action, and safe next action.
   - Support can resend or escalate the approval request, but cannot recreate the refund.
   - If ownership changes, record both the previous and new owner.

6. **Make execution idempotent**
   - The payment/refund operation uses the refund ID as its idempotency key.
   - Before any retry after an ambiguous response, query the processor’s status.
   - If the outcome remains unknown, move the request to `Exception`; do not replay it automatically.

### Verification plan

Test these scenarios before adopting the design:

- Double-click, browser refresh, and client retry create one refund request.
- A timeout followed by retry returns the same refund ID.
- Finance approves from the original and a resent email; the refund executes once.
- Support can identify an owner and next action in every non-terminal state.
- Reassignment preserves history.
- An ambiguous processor timeout pauses for reconciliation rather than issuing twice.
- Rejection, cancellation, missing-information, and stale-approval paths remain recoverable.
- Status and ownership are usable with keyboard navigation and assistive technology.

No files or external systems were modified.