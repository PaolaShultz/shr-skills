Give the customer one durable request reference. Use it to answer three questions throughout the workflow: what has been confirmed, who owns the next action, and what the customer can do now. Email and dashboard updates should describe the same confirmed events, with enough timing information to distinguish an earlier update from the current status.

The fixture contains only `state=blocked`. It identifies neither the reason nor the owner. The conflicting messages, duplicate requests, and unclear handoffs are reported problems. Audit, privacy, and approval are supplied constraints. The exact approval order, billing trigger, cancellation rights, and retention rules remain open. The redesign below preserves those decisions for the responsible policy owners.

### Proposed workflow

1. **Submit once and recover by reference.** Before submission, show the request details, material consequences, and any required choices. Bind a durable submission key to the customer’s confirmed intent. Record the key and request atomically, so a double-click or retry after a lost response returns the original reference. If the payload changes under that key, preserve the edits and ask the customer to review the change. After a timeout, offer “Check submission” and retain the permitted draft context across reauthentication.

2. **Assign authority by fact.** The customer confirms intent. Support owns intake, coordination, and customer follow-up. The approval service owns its approval decision, the compliance reviewer owns the compliance disposition, and billing owns the financial outcome. A shared request record links their versioned decisions and derives overall progress using the governing policy. A late or contradictory event cannot silently overwrite a decision. If the conflict affects a prerequisite, pause the dependent action and assign reconciliation to a named owner.

3. **Transfer ownership on acknowledgment.** Record the sending owner, intended recipient, pending action, and handoff time. The sender owns follow-up until the recipient accepts. Acceptance transfers ownership in one recorded transition. A rejection, interruption, or overdue acknowledgment leaves the sender an actionable item with the handoff context intact. Support can tell the customer who is following up while restricted reviewer notes stay within the review team.

4. **Keep recovery beside the blocked step.** Show authorized staff the blocker, last confirmed event, next permitted action, and responsible owner. Give the customer a privacy-safe explanation and say explicitly whether they need to act. Generate both email and dashboard status from the shared record. Timestamp email as an update and link to an authenticated current view. For the fixture’s bare `blocked` state, show “Reason awaiting confirmation” and route it to support for triage. Inferring a rejection or billing failure would give the customer an unsupported answer.

5. **Gate billing and cancellation on confirmed outcomes.** Release billing only when the applicable approval and compliance prerequisites are current and the policy-defined billing trigger has occurred. Give each authorized billing operation its own stable reference. If billing times out, the recovery owner checks billing by that reference before any replay. If billing cannot establish the outcome, keep it pending reconciliation. Apply cancellation at the policy-permitted point, show its consequences before confirmation, and record the outcome of any in-flight action before describing the request as cancelled or a charge as reversed.

Across these steps, keep an access-controlled audit history of transitions, including actor or service, time, decision version, ownership changes, and correlation references. Record corrections as linked events. Keep sensitive evidence in its authorized system, expose only role-appropriate fields, and apply the governing retention rules to both records and drafts.

### Verification plan

| Exercise | Evidence required |
|---|---|
| Complete one request across all five actors | Trace one confirmed intent through the required decisions to one authorized billing outcome. Each transition identifies its source and next owner. |
| Interrupt submission and retry concurrently | Drop the response after creation, refresh, and retry. Every attempt resolves to one request. Changed details require fresh review, and reauthentication preserves permitted work without submitting it. |
| Interrupt a handoff before and after acceptance | Test rejection, duplicate acknowledgment, and recipient absence. At every point one actor owns follow-up, can recover the context, and can see the next action. |
| Delay email and deliver decisions out of order | An older email is recognizable as historical. The dashboard shows the latest confirmed status. A stale approval cannot release billing, and conflicting evidence has a reconciliation owner. |
| Lose a billing response and race cancellation with billing | Simulate billing success followed by timeout. Verify lookup precedes replay, the financial effect occurs once, and the customer sees only confirmed cancellation and financial outcomes. |
| Exercise privacy, audit, and accessibility | Inspect each role’s view, email, and audit access. Complete submission, status lookup, and recovery with keyboard and screen reader. Check focus after errors, announced status changes, retained inputs, and an identifiable next action. |

Before adoption, the responsible owners need to confirm the policy gates and whether approval and billing support durable outcome lookup and duplicate suppression. Those capabilities determine where automatic recovery is safe. This was a read-only redesign. No changes were made, and the proposed checks have not been run.