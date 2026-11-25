Give each request **one durable reference and one current recovery owner**. A customer who retries should return to the same request. A support agent looking up that reference should be able to answer three questions: what has been confirmed, who has the next action, and what happens if that action stalls.

The local [fixture](./workflow.txt) contains only `state=blocked`. It gives no reason, owner, approval decision, or billing outcome. The channel disagreement, duplicate requests, and stalled handoffs are reported symptoms. The workflow below is a proposed redesign. Nothing was modified, and no external service was accessed.

### Authority and protected properties

The request establishes audit, privacy, and approval as constraints. Their precise policies are absent from the fixture. The proposal assigns authority **per fact** so that a delayed email, a support note, or a billing timeout cannot overturn a decision made elsewhere.

| Fact | Proposed authority and safeguard |
|---|---|
| Request identity, customer intent, current owner, and next action | A shared workflow record holds the reference, request version, and accepted handoffs. Customer and support channels use the same record with role-appropriate views. |
| Compliance judgment and approval | The compliance reviewer records their judgment. The approval service records whether the applicable gate has passed for the exact request version. As a design assumption, billing requires that gate to pass. The policy owner must confirm which effects require approval and when human review is mandatory. |
| Financial effect | Billing confirms whether it applied an effect and supplies a receipt or definitive failure. An approval or a delivery acknowledgment alone cannot establish that a charge occurred. |
| Audit and privacy | Each transition records the actor or service, request version, time, decision or outcome, and evidence reference under the applicable retention policy. Corrections are linked events. Sensitive evidence stays in its authorized store. Customer email carries a minimal update and an authenticated link. Access to reviewer reasoning follows role and purpose. |

### Proposed motion

1. **Submit once and resume.** Before commitment, show the customer the request details, any financial consequence, and the approval requirement. Preserve permitted draft fields and form position across reauthentication, and identify any fields privacy policy requires them to re-enter. On explicit submission, bind a stable submission key to the customer and the reviewed content. Atomically create the request and its receipt. If the response is lost, retrying that key returns the same reference. Reuse with changed content prompts a review of the change. Support can locate the original submission before initiating another.

2. **Transfer ownership on acceptance.** Each handoff records the destination, requested action, and time. The sending owner remains accountable until the recipient accepts. Acceptance changes the owner and next action together, with a version check so concurrent claims cannot both succeed. During a compliance referral, the approval service owns delivery until the reviewer accepts. The reviewer then owns the decision until the approval service accepts it back. An overdue handoff appears in the sender’s recovery queue with its escalation contact. The customer sees, for example, “Awaiting compliance review — no action needed from you.”

3. **Bind approval to the reviewed work.** The reviewer can approve, decline, or request specific information. When customer input is needed, the customer sees the question beside the relevant field, and a named case owner tracks the response. Preserve prior answers and decisions within privacy limits. A material amendment creates a new version and triggers the required review before any gated effect. A decline closes the gate and surfaces the permitted explanation and available recourse.

4. **Resolve billing uncertainty before replay.** Once the gate passes, send billing a stable effect key tied to the approved version and intended charge. Billing enforces uniqueness for that key. A timeout leaves the request at “Confirming billing outcome,” with a named reconciliation owner. That owner checks billing by key and records the receipt if the charge succeeded. Replay requires a definitive safe-to-retry result and the same key. If billing cannot establish the outcome, the owner investigates while the customer can leave and return to the same request.

5. **Keep channels and cancellation coherent.** Generate dashboard status and email from the same committed transition. Date each email update and link to current status, so an older message remains intelligible if delivery is delayed. Expose versioned events to services and ignore stale or duplicate deliveries. Record cancellation against the same reference. Before dispatch, serialize cancellation with dispatch so only one wins. After dispatch, show “Cancellation requested” while the recovery owner establishes what happened. Any reversal follows the applicable policy and has its own auditable outcome.

### Verification plan

| Exercise | Acceptance condition |
|---|---|
| Complete a request across all five actors. Delay and reorder email and service events. | One reference follows the request through approval and billing. Each view shows permitted facts from the correct source. Older events cannot regress status. |
| Double-submit, lose the receipt, reauthenticate, and resume with support. | One request exists. The customer returns to the correct position with permitted work intact. Support finds the same request. A deliberate second request requires fresh intent. |
| Interrupt a handoff before and after acceptance. Have two reviewers claim it. | Exactly one recovery owner is visible at each point. The overdue action reaches that owner’s queue. Only one reviewer acquires the case. |
| Decline a request, request information, and amend an approved request while dispatch is pending. | The customer can act on the permitted feedback. Billing cannot execute against a declined or superseded approval. The audit history preserves the sequence. |
| Lose billing’s response after a successful charge. Race cancellation against dispatch. | Reconciliation finds the existing receipt. At most one charge occurs. The customer sees a pending outcome until billing confirms the result, and any reversal is traceable. |
| Test customer, support, and reviewer views with keyboard and screen reader. Inspect email, logs, and service events under each role. | Status changes are announced, focus resumes predictably, and recovery controls are reachable. Restricted evidence stays within its access boundary. Authorized reviewers can reconstruct the case. |

Before adoption, the policy owners need to confirm approval scope, permissible draft and audit retention, customer-visible reasons, and cancellation rights. Billing must also confirm that it can enforce effect-key uniqueness and look up outcomes by key. Until then, an ambiguous billing result requires owned reconciliation. These checks are proposed and remain unexecuted.