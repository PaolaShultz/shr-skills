**Give the customer one request ID that survives retries and handoffs.** The dashboard, support view, and email should all refer to that ID. Each service should remain authoritative for the fact it produces. A shared request record should use those facts to show what has happened, who owns the next action, and what that actor can do.

The fixture contains only `state=blocked`. It gives no reason, owner, or history. The status disagreements, duplicates, and handoff failures are reported symptoms. The design below is a proposal. Nothing was modified and no external service was accessed.

### Protected properties and authority

The request requires audit, privacy, and approval controls. The fixture supplies no governing policy. The following are proposed boundaries to confirm with the policy owners before implementation.

| Actor | Authority and limit |
|---|---|
| Customer | Confirms the request and any disclosed billing consequence. Signing in, resuming a draft, or checking status cannot submit it. |
| Support agent | Can assist on the same request within existing permissions. An action taken on the customer’s behalf records the agent’s identity and authority. |
| Approval service | Records the effective approval or denial for a specific request revision. The regulated effect can proceed only under a valid approval covering that revision. |
| Compliance reviewer | Owns the assigned review and records the finding and its scope. The approval service must require that finding wherever policy calls for it. |
| Billing system | Confirms whether the authorized financial effect occurred and supplies its transaction reference. A timeout leaves the outcome unknown. |

The shared record should retain auditable transitions, including the actor, revision, decision reference, and ownership change. Corrections should append history. Sensitive content should stay in its authorized store, with role-limited access and policy-defined retention. Email should carry only a permitted reference and a link requiring authentication.

### Proposed workflow

1. **Submit once.** Preserve entered work and the customer’s position in a policy-permitted draft. Before confirmation, show the requested effect and any charge. Give that intent a stable submission key. Create the request and bind the key to its ID atomically. If the reply is lost, a retry with the same key and content returns the original receipt. Changed content requires an explicit revision or a separately confirmed new request. Support can locate the original receipt after verifying access.
2. **Hand off without dropping ownership.** Record the current owner, intended recipient, next action, and handoff time. The sender owns recovery until the recipient accepts. Acceptance transfers ownership in one recorded transition. A rejected or overdue handoff returns to the sender’s attention with a reason and escalation route. The customer sees a privacy-safe description such as “Waiting for review” and whether they need to act.
3. **Resolve review and approval on the same revision.** A reviewer asking for information should identify the missing item and give the authorized respondent a way to supply it in place. Preserve completed fields and route the response back to the assigned review. A material edit requires a new approval decision. Duplicate or late decisions remain traceable and cannot release a different revision or reverse a newer decision.
4. **Reconcile billing before retrying.** Give each authorized charge a durable operation key and pass it to billing with the request reference. On timeout, show “Confirming payment” and assign reconciliation to billing operations. Query the original operation before replay. If billing cannot establish its outcome or guarantee deduplication, keep it pending for reconciliation. Close the request only when every required effect has a confirmed outcome.
5. **Keep cancellation and status truthful.** Record a cancellation request on the same ID. Prevent effects that have yet to start and reconcile any effect already in flight. Show “Cancellation pending” until its outcome is known. A completed charge and any authorized reversal each retain their own reference. Generate dashboard and support views from the same versioned history. Label email as an update *as of* a particular time and link to current status. Delayed delivery must never move the record backward.

### Verification plan

| Exercise | Expected observation |
|---|---|
| Submit, lose the reply, retry concurrently, then ask support for help | Customer and agent recover one ID and one receipt. A separately confirmed new intent still works. Reauthentication restores the permitted draft and position without submitting. |
| Delay, reject, and concurrently accept a handoff | Exactly one actor owns recovery throughout. Both teams can see the next action within their permissions. An overdue transfer reaches the responsible queue. |
| Complete a normal review, then repeat with a denial, missing finding, or material edit | The normal path reaches one authorized effect. Each blocked path identifies its owner and next action. Old approvals cannot authorize edited content. |
| Lose the billing reply after a successful charge and race cancellation against dispatch | Reconciliation finds the original transaction. The customer sees a pending outcome until confirmed. No second charge occurs, and cancellation history matches the actual financial result. |
| Deliver email updates out of order and reopen an old link | Email remains accurate as a dated snapshot. Authorized dashboard and support views agree on current state. Unauthorized readers receive no case details. |
| Resume and recover using keyboard and screen reader, then inspect the audit trail and neighboring requests | Focus returns to the relevant field or action, status changes are announced, and recovery is operable. History identifies each actor and revision. Unrelated drafts, requests, balances, and permissions remain unchanged. |

Before implementation, the policy owners need to establish which effects require approval, what invalidates it, what drafts and notifications may contain, and how long each record may persist. Billing also needs to establish how it identifies an operation after a lost reply. Those answers determine when automated recovery is safe and when a named person must reconcile the request.