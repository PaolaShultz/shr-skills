Redesign mode

The fixture contains only `state=blocked`. That directly confirms a blocked state exists, but provides no implementation, transition history, ownership, retry, or synchronization evidence. The reported email/dashboard disagreement, duplicate retries, and competing authority claims therefore remain requester-provided conditions, not independently validated behavior.

## Replacement motion

Create one canonical request record with a stable `request_id`, immutable audit history, explicit ownership, and domain-specific authority. No participant is authoritative for the entire workflow.

| Domain | Authority | Responsibility |
|---|---|---|
| Customer request content and consent | Request service | Stores the submitted version and customer-visible intent |
| Work ownership and handoff | Request service | Records exactly one current owner and pending handoffs |
| Approval decision | Approval service | Issues a version-bound approval or rejection |
| Compliance decision | Compliance reviewer/system | Records review outcome and permitted rationale |
| Billing execution | Billing system | Records charge, reversal, or billing failure |
| Customer-facing status | Request service projection | Derives status from authoritative domain events |
| Email and dashboard | Neither | Render the same versioned status projection |

### Coherent workflow

1. The customer submits once. The request service assigns `request_id` and returns a receipt immediately.
2. Every submission or retry carries an idempotency key scoped to the customer, operation, and request version. Replays return the original result; they do not create another request.
3. The request service appends an audit event, sets one current owner, and derives the visible status.
4. An agent may propose a handoff, but ownership does not become ambiguous:
   - current owner remains accountable;
   - proposed owner receives a pending assignment;
   - ownership changes only on acceptance;
   - rejection or timeout returns the item to the existing owner with a visible recovery action.
5. Approval and compliance decisions reference the exact immutable request version. Editing decision-relevant content creates a new version and invalidates prior decisions where policy requires; it never silently reuses them.
6. Billing receives a uniquely identified execution command only after the required approval and compliance states are satisfied. Its own idempotency key prevents duplicate charges.
7. Domain systems publish versioned outcomes. The request service consumes them, rejects stale or conflicting transitions, and records both accepted and rejected events in the audit trail.
8. The dashboard reads the canonical projection. Email is generated from that same committed projection and includes the request ID, status version, timestamp, and a dashboard link. Delayed email remains identifiable as an older notification rather than competing truth.
9. Failures preserve entered work and completed decisions. The visible blocked state includes the blocking reason category, accountable owner, last successful step, and an authorized retry or escalation action.

## Constraint preservation

- Audit: append-only events capture actor/service identity, timestamp, correlation and idempotency keys, request version, transition, and reason code. Corrections are new events, never history rewrites.
- Privacy: each actor receives only the minimum fields needed for its task. Emails contain no sensitive request details; audit access is role-restricted, logged, and subject to applicable retention rules.
- Approval: approval cannot be inferred from authentication, assignment, setup, or submission. Decisions require explicit authorized action and bind to a specific request version.
- Integrity: transitions use optimistic concurrency or equivalent version checks; stale writes cannot overwrite newer state.
- Ownership: exactly one accountable owner exists throughout processing, including pending handoffs and failures.
- Interoperability: integrations exchange stable IDs, versions, reason codes, and idempotent commands rather than interpreting another system’s display text.

Existing retention periods, reviewer-separation rules, approval thresholds, privacy classifications, and billing reversal policy remain unchanged and must be supplied from their owning policies before implementation.

## Recovery and exceptional paths

- Duplicate submission: return the existing request and receipt.
- Timed-out retry: query by idempotency key before issuing new work.
- Conflicting domain event: quarantine it, preserve it in audit, keep the last valid projection, and assign reconciliation ownership.
- Notification failure: retry notification delivery without replaying the business transition.
- Handoff timeout: retain the current owner and expose escalation.
- Billing uncertainty: show “billing confirmation pending”; do not retry a charge until the billing system resolves the original execution key.
- Cancellation: record an explicit cancellation request, assess it against approval and billing state, and expose any irreversible consequence before commitment.

## Verification plan

Before release, verify:

- concurrent and repeated submissions produce one request;
- retries after timeouts return the original outcome;
- billing retries produce at most one financial execution;
- stale or out-of-order events cannot regress status;
- email and dashboard reference the same committed status version;
- handoff acceptance, rejection, timeout, interruption, and escalation always retain one accountable owner;
- edits correctly preserve or invalidate version-bound decisions according to policy;
- blocked requests retain work and provide an authorized recovery path;
- unauthorized actors cannot view sensitive fields, approve, reassign, or access protected audit data;
- audit history is complete, ordered, attributable, and tamper-evident;
- keyboard and assistive-technology users can identify status, owner, blockers, consequences, and recovery controls;
- cancellation before and after approval or billing produces the defined result without hiding irreversible effects.

This is a proposed design, not validated behavior. No files or systems were modified. The material open decisions are the organization’s binding status-transition rules, decision-invalidation policy, handoff timeout/escalation owner, privacy classification, retention requirements, and billing cancellation/reversal semantics.