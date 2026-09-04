The fixture only confirms `state=blocked`; the workflow details below come from the request and should be validated with finance, support, and engineering before implementation. No files or systems were modified.

### Proposed flow

1. **Submit once**
   - The dashboard creates a refund request with a unique request ID and idempotency key.
   - It immediately shows either:
     - `Submitted — awaiting finance`, or
     - `Submission outcome unknown — checking status`.
   - A timeout must not present a fresh “Submit” action.

2. **Recover safely after a timeout**
   - The dashboard queries the original request using the idempotency key.
   - “Try again” resends the same operation with the same key.
   - The backend returns the existing refund request rather than creating another.
   - Disable duplicate active requests for the same underlying charge unless support explicitly chooses “Create separate request” and supplies a reason.

3. **Keep approval in email, with the dashboard as source of truth**
   - Finance receives an email containing the request ID, amount, customer, reason, current owner, and a secure approve/reject link.
   - The decision is recorded against the same dashboard request; the email is notification and entry point, not a separate record.
   - Reopening an old approval link displays the current outcome and cannot approve twice.
   - If policy requires approval by email reply specifically, replies should be ingested and attached to the request; ambiguous replies go to an exception queue.

4. **Make ownership explicit**
   - Every request has exactly one current owner and one owning queue.
   - Initial state: `Awaiting finance`, owner `Finance approvals`.
   - On approval: owner moves to `Refund processing`.
   - On rejection or information request: owner moves to the named support agent or originating support queue.
   - Support sees owner, status, age, last action, and next required action in the dashboard.

5. **Use a visible lifecycle**
   - `Submission pending`
   - `Awaiting finance`
   - `More information required`
   - `Approved — processing`
   - `Refund completed`
   - `Rejected`
   - `Cancelled`
   - `Needs investigation`

Each transition should record actor, timestamp, reason, and correlation/request ID. Stalled requests should escalate to a named backup queue rather than becoming ownerless.

### Critical behavior to verify

- Repeated clicks, browser refreshes, and retries after timeouts produce one request.
- A server-created request remains discoverable if the client never receives the response.
- Two finance approvers opening the same email cannot create conflicting decisions.
- Support and finance see the same status, owner, history, and next action.
- Rejection, cancellation, missing information, expired links, and downstream refund failures have clear recovery paths.
- Sensitive customer and payment data are minimized in email; authorization is checked when the approval action occurs.

Material decisions still needed: what constitutes the same refund for duplicate detection, the ownership/escalation SLA, who may override duplicate protection, and whether “approval by email” permits a secure link or legally requires a retained email reply.