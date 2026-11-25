**Give each request one durable reference, one current recovery owner, and a separate status for each consequential decision.** A customer should be able to answer “Was my request received?”, “Who acts next?”, and “Was I charged?” even when one service is unavailable.

The fixture contains only `state=blocked`. It identifies neither the blocked step nor its owner. The channel disagreement, duplicate requests, and lost handoffs are reported problems. Their frequency and causes are unknown. I would prioritize duplicate requests and uncertain billing outcomes first because their effects can be costly to reverse, then stalled handoffs and conflicting messages that can prompt further retries.

### Proposed workflow

| Actor | What the actor can establish | How work continues |
|---|---|---|
| Customer | Intent to submit a particular version of a request | Show the material terms and any billing consequence before submission. Preserve permitted draft data and issue a stable submission reference before sending. Repeated submission of the same intent returns the same request. |
| Support agent | Receipt, case coordination, and the next action communicated to the customer | Assign a support owner on receipt. A handoff records the work requested, the recipient, and the permitted context. The sender retains responsibility until the recipient accepts. A declined or overdue handoff returns to the sender’s attention with the request intact. |
| Approval service | The approval decision for a specific request version | Record the decision and version together. If the decision is delayed, the service exposes a pending status that support can check. A material amendment requires evaluation of the amended version. |
| Compliance reviewer | The disposition of a required review and any information needed to resolve it | On acceptance, the reviewer owns the review step. A request for customer input identifies exactly what is needed through an authorized channel. Restricted evidence and reviewer notes stay within the review boundary. |
| Billing system | Whether a particular billing operation is pending, posted, or definitively failed | Start billing only when the applicable approval, review, and customer authorization cover that operation. Use a durable operation reference. After a timeout, query or reconcile by that reference before retrying. If billing cannot establish the outcome, route it to a named recovery owner and hold further attempts. |

The shared request record would assemble these facts without giving any participant power to overwrite another participant’s decision. Each transition would identify the request version, source, event identifier, prior state, and responsible owner. Duplicate events would have one effect. Late events would remain auditable without moving the current view backward. An incompatible decision would open a reconciliation task for the authority responsible for that fact and hold dependent actions.

Email and dashboard would render the same customer-visible record. Email would identify the update time and request reference and link to the authenticated current view. For example, an email could say “We received your request at 09:42,” while a later dashboard update says “Approval granted at 10:18. Billing confirmation pending.” Support would see which update the customer received and could explain the difference. A delivery failure would trigger a notification retry independently of request processing.

Cancellation would have its own recorded outcome. Before a consequential action starts, an accepted cancellation would prevent it from starting. If a charge may already be in flight, the customer would see “Cancellation requested. We’re checking whether payment was processed,” with an owner for follow-up. Any reversal would follow the applicable authorization rules. After reauthentication or interruption, each actor would return to the permitted request, step, and saved work.

Audit, privacy, and approval are explicit constraints in the request. The fixture supplies no retention schedule, field-access matrix, review triggers, or cancellation rules. Those details require confirmation from their policy owners. The proposed audit trail would retain authorized transition evidence and references to restricted records, with role-specific views and policy-defined retention.

### Verification plan

- **Complete one request across all five actors.** Trace the same reference from submission through handoff, required decisions, billing, and customer notification. Check who owns each wait and confirm every consequential action has its required authorization.
- **Interrupt submission and billing after acceptance but before acknowledgment.** Retry from a second session and redeliver events out of order. Verify one request and at most one intended charge. Simulate unavailable billing lookup and confirm that the owner can reconcile the operation before another attempt.
- **Interrupt a handoff.** Close the sender’s session before acceptance, then test decline, timeout, and concurrent acceptance. Verify exactly one recovery owner, intact permitted context, and a visible next action throughout.
- **Race an amendment or cancellation against approval and billing.** Verify that stale approval cannot authorize amended terms, that cancellation prevents pending effects where permitted, and that an in-flight outcome remains visible until reconciled.
- **Check channel agreement, privacy, and accessibility.** Delay an email, deny access to reviewer notes, and expire a session mid-task. With keyboard and screen-reader users, verify that they can identify the current status and next action, resume at a meaningful position, and recover without resubmission or disclosure.

This is a redesign proposal. The verification plan has not been run. No fixture changes or external requests were made.