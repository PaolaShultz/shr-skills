Redesign mode. I inspected the available artifact: [workflow.txt](/tmp/fructal-eval-complex_multi_actor_continuity-01-2qtqu2j_/fixture/workflow.txt), which only records `state=blocked`. The disagreement, duplication, and handoff problems are requester-provided facts; no implementation, logs, schemas, or policies were available to validate their causes. Nothing was modified.

## Replacement motion

Introduce one canonical request record identified by an immutable `request_id`. Authority is divided explicitly by domain rather than allowing every system to claim authority over the whole request:

| Domain | Authority |
|---|---|
| Request identity, lifecycle state, current owner, version | Canonical request registry |
| Approval decision and supporting decision reference | Approval service |
| Compliance disposition and required conditions | Compliance reviewer/system |
| Charges, refunds, and settlement state | Billing system |
| Customer-visible status | Versioned projection of the canonical record |
| Email content | Notification generated from that same versioned projection |
| Audit history | Append-only audit ledger |

The registry is a logical role; which existing system hosts it remains an implementation decision.

### Normal flow

1. Customer or support agent submits an intent with a stable idempotency key.
2. The registry atomically creates or returns the existing request and issues its `request_id`.
3. Required approval and compliance work is created from that ID. Each assignment records one accountable owner, status, due time, and escalation route.
4. Approval and compliance services submit signed, version-checked decisions. They remain authoritative for their respective decisions; the registry advances lifecycle state only when the required conditions are satisfied.
5. Billing receives a uniquely identified command only after the recorded prerequisites are met. Re-delivery returns the existing billing result rather than creating another charge.
6. The registry publishes a versioned state event. Dashboard and email consume the same projection. An email states both the status and its effective timestamp/version, so delayed delivery cannot masquerade as current state.
7. Completion records the outcome and references to approval, compliance, and billing evidence in the audit ledger.

A visible state should distinguish at least:

`draft → submitted → awaiting_approval / awaiting_compliance → approved → billing_pending → completed`

with explicit `needs_information`, `rejected`, `cancel_pending`, `cancelled`, and `manual_review` paths. Parallel approval and compliance may coexist, but each must remain separately visible rather than being collapsed into an ambiguous “processing” status.

### Retry and duplicate handling

- The same actor intent retains its idempotency key across timeouts, channel changes, and retries.
- Registry creation, approval tasks, compliance tasks, and billing commands each have their own uniqueness boundary tied to `request_id`.
- A timeout means “outcome unknown,” not “failed; create another request.” The nearby recovery action is **Check existing request / retry safely**.
- Conflicting payloads under the same key are rejected visibly and routed for reconciliation; they are never silently merged.
- Event consumers deduplicate by event ID and apply only newer record versions.

### Ownership and handoff

A handoff is a state transition, not a note:

1. Current owner initiates transfer and names the receiving owner or queue.
2. Required context, outstanding actions, deadlines, and decision references stay attached to the request.
3. Recipient accepts ownership, creating an auditable acknowledgement.
4. Until acceptance, the sender remains accountable and the UI shows `handoff pending`.
5. Rejection, timeout, or unavailable recipient returns the request to the sender or a named escalation owner—never to an ownerless queue.

The customer sees the responsible function and expected next update, but not private reviewer identities or internal compliance material.

### Audit and privacy

The redesign preserves the constraints instead of weakening them:

- Audit: append-only entries record actor/service identity, timestamp, request version, action, reason code, authority, and evidence references. Corrections append compensating records rather than rewriting history.
- Privacy: operational events carry identifiers and minimal status data; sensitive documents remain in their authorized repository and are referenced by access-controlled handles. Emails contain the least sensitive useful status and direct the customer to an authenticated channel.
- Approval: neither submission, authentication, handoff, nor billing setup counts as approval. Required approvals must be explicit, attributable, current, and bound to the request version they authorize.
- Authorization: every read, decision, ownership change, and disclosure is checked against role and request scope.

## Failure and continuity behavior

- If email delivery fails, the dashboard remains current and exposes notification status without changing request state.
- If a projection lags, it displays “updating” with its last applied version rather than presenting stale data as authoritative.
- If an approval or compliance decision arrives for an obsolete request version, it is retained for audit but cannot advance the request; reassessment is requested.
- If billing’s result is uncertain, the workflow reconciles by command ID before retrying.
- Cancellation checks the current irreversible boundary. Before that boundary it cancels outstanding work; afterward it presents the applicable reversal or manual-review path.
- Service outages retain queued work, ownership, idempotency keys, and causal ordering. Resumption continues the same request.
- Repeated or cross-channel use retrieves the existing request by authenticated identity and request ID rather than starting a parallel workflow.

## Verification plan

Before implementation, validate the design with:

- Simultaneous customer and agent submissions produce one request and one downstream task set.
- Lost responses and repeated retries do not duplicate approvals, reviews, requests, or charges.
- Dashboard and email derive from the same request version; delayed email is identifiable as historical.
- Every lifecycle state has exactly one accountable owner or a visible pending handoff with a fallback owner.
- Handoff acceptance, rejection, timeout, and interruption retain context and deadlines.
- Stale or conflicting approval/compliance updates cannot advance the lifecycle.
- Billing timeout and redelivery resolve to one financial result.
- Cancellation works before and after the irreversible boundary without hiding consequences.
- Audit reconstruction explains every transition without exposing protected content to unauthorized actors.
- Keyboard and assistive-technology paths announce state, ownership, errors, retry outcomes, and handoff results without relying on color or email alone.
- Rebuilding projections from the ledger yields the same dashboard state and notification history.

These are proposed verification scenarios, not validated behavior.

Material decisions still open are where the canonical registry and audit ledger will live, the exact approval/compliance sequencing mandated by applicable regulation, retention and redaction periods, the billing irreversibility boundary, and ownership/escalation service-level rules. Those require policy owners and system evidence before implementation.