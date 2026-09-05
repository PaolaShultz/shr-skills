## Fructal Cap Design — Redesign

Observed: the fixture only records `state=blocked`. The remaining workflow failures and constraints are provided by the request; their underlying implementation is not available for inspection.

### Replacement motion

Use one durable request record with a globally unique `request_id`. No system is universally authoritative; authority is explicitly divided by domain:

| Domain | Authoritative owner |
|---|---|
| Request content and customer intent | Request record |
| Current support ownership | Workflow coordinator |
| Approval decision | Approval service |
| Compliance decision and rationale | Compliance reviewer/system |
| Financial transaction status | Billing system |
| Customer-facing aggregate status | Workflow coordinator, derived from the domain records |
| Audit history | Append-only audit ledger |

Email and dashboard must render the same versioned status projection. Email is a notification—not an independent status source—and links to the current dashboard record.

The redesigned flow is:

1. **Create safely**
   - The customer submits once using an idempotency key.
   - The coordinator creates or returns the existing `request_id`.
   - Entered content survives authentication, timeout, and recoverable validation failures.
   - Sensitive fields are classified at intake and disclosed only to actors permitted for their task.

2. **Record required decisions**
   - The coordinator requests approval and compliance review using the same `request_id`, request version, and operation id.
   - Each decision records actor, timestamp, request version, policy/version applied, outcome, and reason.
   - A material edit invalidates affected prior decisions and visibly returns the request to review; it never silently reuses approval.

3. **Expose one aggregate state**
   - The coordinator computes a state such as `awaiting_approval`, `awaiting_compliance`, `actionable`, `billing_pending`, `completed`, `rejected`, `cancelled`, or `blocked`.
   - The projection also reports each component decision and its freshness. Unknown or unreachable systems produce `status_unknown`, not an inferred success or failure.
   - Email carries the projection version and generated time. A stale email remains auditable but clearly directs the customer to the current record.

4. **Make handoff atomic**
   - Ownership changes through one compare-and-set operation containing previous owner, next owner, reason, timestamp, and accepted request version.
   - Until the recipient accepts, the sender remains responsible and the UI shows “handoff pending.”
   - Rejection or timeout returns responsibility to the sender with an explicit recovery action. There is never an ownerless intermediate state.

5. **Make retries replay-safe**
   - Every consequential command uses an idempotency key scoped to the request and operation.
   - Repeating a command returns its recorded result; it does not create another request, approval, or charge.
   - After a timeout, the coordinator checks operation status before retrying. Ambiguous billing outcomes enter reconciliation rather than replay.
   - Conflicting payloads using the same key are rejected and audited.

6. **Complete or recover visibly**
   - Billing begins only when the configured approval and compliance gates are satisfied.
   - Completion requires recorded downstream outcomes, not merely successful dispatch.
   - A blocked request identifies the blocking domain, current recovery owner, preserved state, and next safe action.
   - Cancellation stops new actions while retaining the audit trail. Any already-started billing action is reconciled before the workflow claims cancellation is complete.

### Constraint preservation

- **Audit:** append-only events capture commands, decisions, retries, handoffs, projection changes, and notification versions. Corrections are new events rather than overwritten history.
- **Privacy:** actors receive only task-relevant fields; emails contain minimal data; audit views are access-controlled; sensitive-value access is itself recorded. Retention and redaction follow the applicable policy.
- **Approval:** required approval cannot be bypassed by retries, handoffs, billing, or administrative status edits. Decisions bind to a specific request version.

The exact governing policies, retention period, required approval order, and whether compliance may override approval remain open questions. They must be configured from the actual regulatory requirements rather than inferred.

### Verification plan

Verify with correlated records across all five actors:

- Concurrent identical submissions yield one `request_id`; conflicting reuse of a key is rejected.
- Timeout before and after creation recovers the same request without losing entered work.
- Repeated approval, compliance, and billing commands create no duplicate effects.
- An ambiguous billing timeout triggers status inquiry/reconciliation before any replay.
- Every email status matches the cited projection version; stale messages point to the newer dashboard state.
- Handoff acceptance, rejection, timeout, and interruption always leave one identifiable recovery owner.
- Material edits invalidate only the decisions affected by the changed fields.
- Cancellation before approval, during review, and during an uncertain billing operation stops eligible future work and reports in-flight effects accurately.
- Unauthorized actors cannot view protected fields; permitted access and redaction remain auditable.
- Keyboard-only and assistive-technology users can identify status, owner, blocking reason, stale information, errors, and recovery actions; status changes are announced accessibly.
- Approval/compliance rejection cannot be converted to completion through retry or direct billing updates.
- Existing unrelated request data and historical audit entries remain unchanged.

No files or workflow state were modified.