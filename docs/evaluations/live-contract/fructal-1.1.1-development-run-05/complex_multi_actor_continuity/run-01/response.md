Redesign mode.

The only inspected artifact is `workflow.txt`, which reports `state=blocked`. The conflicting statuses, duplicate retries, unclear handoffs, and competing authority claims are requester-provided and not independently verified. No files or systems were modified.

## Core finding

The workflow has multiple publishers but no agreed authority for:

- Request identity
- Lifecycle state
- Current owner
- Approval evidence
- Billing effects
- Customer-facing status

That makes retries, handoffs, and notifications capable of creating contradictory business facts. Audit logging alone cannot resolve this if systems record different facts.

## Replacement motion

Create one authoritative request record and append-only event history in a designated workflow authority. Other systems remain authorities only for their own domain facts:

| Concern | Authority |
|---|---|
| Request ID, lifecycle state, owner, retry identity | Workflow authority |
| Approval decision and signed decision evidence | Approval service |
| Compliance disposition and rationale | Compliance reviewer’s system |
| Charges, refunds, and invoice state | Billing system |
| Email and dashboard wording | Projections of workflow state—not independent status authorities |

Every request receives an immutable `request_id`. Every initiating submission or retry also carries an `idempotency_key`. Repeating the same operation returns the existing request and current status; it must not create another request or repeat billing.

Use an explicit state model:

`Draft → Submitted → Under review → Awaiting approval → Approved/Declined → Billing pending → Completed`

Exceptional states should preserve their cause and recovery path:

- `Needs customer information`
- `Approval unavailable—retry scheduled`
- `Billing failed—no new approval required`
- `Cancelled`
- `Blocked—manual intervention required`

Transitions are accepted only when the expected request version matches. Each accepted transition appends an event containing actor/service identity, timestamp, prior and resulting state, correlation ID, reason code, and references to supporting evidence. Sensitive evidence stays in its owning system; the audit event stores a protected reference and minimum necessary metadata.

## Ownership and handoff

Ownership must be a workflow field, not inferred from inboxes or system activity.

A handoff is one atomic transition:

1. Current owner nominates the next owner or queue.
2. Workflow records `handoff_pending` while retaining the current owner.
3. Recipient accepts, or an established routing rule explicitly accepts on its behalf.
4. Workflow atomically changes the owner and records both parties.
5. Timeout or rejection returns the item to the prior owner or an escalation queue.

Until acceptance, the original owner remains accountable. The dashboard shows the accountable owner, intended recipient, handoff age, and escalation deadline. Customers see a privacy-safe status such as “Under review,” not internal personnel or compliance details.

## Approval, compliance, and billing

Approval and compliance decisions remain controlled by their respective regulated systems. The workflow authority records their signed outcome, evidence reference, policy/version identifier, and validity period; it cannot fabricate or override those decisions.

Billing begins only after the required approval and compliance predicates are satisfied. The billing command uses a stable operation key derived from the request and billing action. A retry queries or resumes that operation rather than issuing a new charge. Billing reports its domain result back as an event, after which the workflow advances.

Cancellation never erases history. It stops future eligible work, records who cancelled and why, and triggers explicit compensating actions where needed. If approval or billing is already in flight, the UI must disclose that cancellation is pending until those actors acknowledge it.

## Email and dashboard continuity

Both channels consume the same committed workflow events. Neither calculates status independently.

- The dashboard displays the latest authoritative version and its update time.
- Email is generated only after a committed transition and includes request ID, plain-language state, and a dashboard link.
- Delayed email retains the state’s effective timestamp.
- If an older email is opened later, it identifies itself as a point-in-time notice and directs the customer to the current dashboard state.
- Projection failures are retried idempotently and surfaced operationally; they do not alter request state.

## Preserved constraints

- **Audit:** Append-only transition history, actor attribution, policy versions, correlation IDs, and decision references.
- **Privacy:** Minimum necessary data per actor, role-based access, redacted customer status, protected evidence references, and retention rules applied by data class.
- **Approval:** No progression past guarded states without authentic, current approval and compliance evidence.
- **Ownership:** Exactly one accountable owner throughout submission, handoff, delay, and recovery.
- **Data integrity:** Versioned transitions and idempotent request, approval, notification, and billing operations.

## Verification plan

This proposal is not yet validated. Before implementation, verify:

- A normal request produces one ID, one coherent state sequence, and matching dashboard/email meaning.
- Concurrent duplicate submissions and repeated retries return the same request and do not duplicate approval work or charges.
- A failed or timed-out handoff retains a visible accountable owner and escalates without losing entered work.
- Approval-service interruption resumes from the same request and preserves the prior decision state.
- Billing timeout followed by retry reconciles before any second financial action.
- Cancellation at each consequential boundary stops or compensates work without deleting audit evidence.
- Delayed and out-of-order events cannot regress the authoritative state.
- Projection outages visibly alert operators while the source record remains intact.
- Each actor sees only necessary information; access and sensitive-field handling meet applicable policy.
- Keyboard and assistive-technology users can identify state, owner, errors, and recovery actions without relying on color or email alone.
- Audit reconstruction can explain every transition, decision, handoff, retry, and external side effect.

## Decisions required before implementation

- Which owned service will become the workflow authority, including its operational owner and availability target.
- The applicable regulations, retention periods, residency requirements, and segregation-of-duties rules.
- Exact approval/compliance predicates and who may override or expire them.
- Handoff acceptance and escalation time limits.
- Billing reconciliation and compensation rules.
- Migration and reconciliation policy for existing records whose systems currently disagree.

The current `blocked` status should remain unchanged until those decisions are made and the existing records are reconciled through an auditable process.