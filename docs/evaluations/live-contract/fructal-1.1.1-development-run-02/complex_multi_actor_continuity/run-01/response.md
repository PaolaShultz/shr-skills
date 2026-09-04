Redesign mode. I inspected the disposable fixture without modifying it or accessing external services. The only observed system evidence is [`workflow.txt`](/tmp/fructal-eval-complex_multi_actor_continuity-01-8ddvcmmd/fixture/workflow.txt), which reports `state=blocked`. The disagreement, duplicate retries, handoff ambiguity, and competing authority claims are requester-provided and remain unverified.

### Proposed replacement motion

Create one canonical request record with an immutable event history and explicit lifecycle state:

`Draft → Submitted → Compliance review → Approval pending → Approved/Rejected → Billing pending → Completed`

Failure, cancellation, and correction are explicit states or events rather than status text maintained independently by each channel.

1. **Customer submits once**
   - Submission receives a stable request ID and idempotency key.
   - A retry with the same key returns the existing request and current status.
   - Changed content requires a new revision, preserving the prior submitted version for audit.

2. **Canonical workflow accepts or rejects the transition**
   - One workflow ledger is authoritative for request identity, lifecycle state, revision, ownership, and transition history.
   - Every transition records actor/service identity, timestamp, reason, prior state, resulting state, and correlation ID.
   - Audit history is append-only; corrections are new events, not overwritten records.

3. **Authority is bounded by domain**
   
   | Component | Authoritative for | Not authoritative for |
   |---|---|---|
   | Customer/support interface | Draft input and displayed intent | Lifecycle status |
   | Support agent | Assigned case work and handoff proposal | Approval or billing outcome |
   | Compliance reviewer | Compliance decision and rationale | Request ownership or payment completion |
   | Approval service | Approval decision under its policy | Overall workflow status |
   | Billing system | Charge/invoice outcome | Approval or request lifecycle |
   | Workflow ledger | Request state, revision, owner, and event sequence | Component-specific decision internals |

4. **Handoff uses offer-and-accept**
   - The current owner remains responsible while a handoff is pending.
   - The recipient explicitly accepts; only then does ownership change atomically.
   - Decline, timeout, or interruption leaves ownership with the sender and creates a visible recovery task.
   - Customer-facing status describes progress, not internal team routing.

5. **Approval and billing consume versioned commands**
   - Approval evaluates an immutable request revision.
   - Editing material regulated data invalidates the old decision and starts approval for the new revision.
   - Billing accepts only an approved revision and deduplicates by request ID plus approved revision.
   - Ambiguous billing timeouts are reconciled by querying the existing operation before retrying; they never create a fresh charge implicitly.

6. **Email and dashboard become projections**
   - Both derive from committed workflow events rather than writing their own status.
   - Email includes the request ID, event/version, timestamp, and a dashboard link, while avoiding sensitive content.
   - The dashboard shows the canonical state and last committed update.
   - Delayed projections display “last updated” and synchronization status. They do not guess or claim a newer state.
   - Notification failure is retried independently and cannot roll back or duplicate the underlying request.

### Preserved constraints

- **Audit:** immutable transitions, decision provenance, correlation IDs, and retained revision history.
- **Privacy:** least-data event payloads, role-scoped views, redacted notifications, and references to protected data rather than unnecessary copies.
- **Approval:** only authorized reviewers/services can record decisions; decisions bind to the exact reviewed revision.
- **Ownership and security:** authenticated actor attribution and atomic handoff prevent ownerless requests.
- **Data integrity and interoperability:** stable IDs, idempotency keys, revision checks, and versioned event contracts govern cross-system exchange.

Retention duration, legal-hold behavior, separation-of-duties rules, regional data boundaries, and the institution authorized to operate the canonical ledger remain material policy decisions. This design does not assume that the current approval service should own that ledger.

### Verification plan

Before implementation, validate the design with scenarios covering:

- simultaneous customer and agent retries produce one request;
- lost responses followed by retries return the existing outcome;
- email delivery delay or failure never changes canonical status;
- dashboard and email expose their event/version so discrepancies are detectable;
- handoff acceptance, rejection, timeout, and agent interruption never leave ownership unclear;
- a material edit after approval creates a new revision and requires reapproval;
- duplicate or timed-out billing calls produce at most one financial operation;
- rejection, cancellation, correction, and failed integrations retain work and provide a nearby recovery action;
- unauthorized actors cannot view private fields, transfer ownership, approve, or bill;
- audit reconstruction reproduces every state and responsible actor without mutable-history gaps;
- keyboard and assistive-technology users can identify state, owner, errors, and recovery actions without relying on color or email alone;
- unrelated requests and historical records remain untouched.

This is a proposed redesign, not validated behavior. No files or system state were changed.