Redesign mode

The fixture contains only `state=blocked`; the reported disagreements, duplicate retries, and unclear ownership are requester-provided and not independently observable. The design below is therefore a proposal, not validated behavior.

### Proposed replacement motion

Create one canonical request record with a stable `request_id`, revision number, current state, current owner, required approvals, billing disposition, and timestamps.

Authority is divided by fact—not duplicated by channel:

| Fact | Authority |
|---|---|
| Request identity, lifecycle state, current owner | Workflow record |
| Approval decision and evidence | Approval service |
| Compliance decision and rationale | Compliance system/reviewer |
| Charges, refunds, and settlement | Billing system |
| Dashboard and email | Read-only projections, never authorities |

1. **Submission**
   - The customer’s obvious action creates or resumes exactly one request.
   - The client supplies an idempotency key; retries return the existing `request_id`.
   - Entered work survives timeout or interruption when privacy policy permits.
   - The customer receives the canonical ID and current status.

2. **Processing**
   - State changes use version-checked transitions and append immutable audit events.
   - Each event records actor/service identity, timestamp, previous and new state, reason, correlation ID, and evidence references.
   - Services process events idempotently using `request_id + operation + revision`.
   - Email and dashboard are generated from committed events. Neither may independently advance status.

3. **Approval and compliance**
   - Required decisions remain explicit gates.
   - Reviewers see only the minimum permitted data, with sensitive evidence referenced through access-controlled links rather than copied into messages.
   - A decision records approver identity, applicable policy/version, outcome, rationale, and request revision.
   - A request changed after review becomes `reapproval_required`; prior approval is retained for audit but cannot silently authorize the new revision.

4. **Handoff**
   - Ownership transfers atomically from one named owner or queue to another.
   - Until acceptance, the sender remains responsible and the interface displays `handoff_pending`.
   - Acceptance establishes the new owner; rejection or timeout returns the request to the sender or a configured escalation queue.
   - Customers see a meaningful status such as “Compliance review,” not internal queue names.

5. **Billing and completion**
   - Billing receives an idempotent authorization or posting instruction only after the required approvals.
   - Its result is correlated to the request and recorded without duplicating protected payment data.
   - Completion occurs only after required downstream acknowledgements. Failed delivery becomes a visible recoverable state, not apparent success.

6. **Notification continuity**
   - Every dashboard view exposes canonical state, revision, and “last updated.”
   - Emails include the request ID and a status snapshot, clearly identifying the dashboard as the current view.
   - Projection lag is shown as “updating” rather than presenting conflicting certainty.
   - Failed notifications retry independently and do not roll back the business state.

### Recovery and stalled progress

- Duplicate submissions resolve to the existing request with a direct resume link.
- Version conflicts refresh the latest record while preserving unsent agent notes where permitted.
- Failed integrations retain intent in an outbox and retry safely.
- Pending approval, compliance, handoff, or billing states have deadlines, a named owner, and escalation paths.
- Cancellation records who cancelled, why, and whether approval or billing reversal is required; it never erases audit history.
- Customer and agent receive prompt, accessible feedback through status text and live-region announcements, without relying on color or email alone.

### Preserved constraints

- **Audit:** immutable event history, decision provenance, revisions, and correlation IDs.
- **Privacy:** least-privilege views, purpose-bound access, data minimization, protected evidence links, and retention rules.
- **Approval:** explicit gates, revision-bound decisions, separation of duties, and no setup or authentication treated as approval.
- **Data integrity:** idempotency, optimistic concurrency, atomic ownership transfer, and reconciled projections.
- **Ownership:** exactly one accountable owner during ordinary processing; handoffs remain visibly pending until accepted.

### Verification plan

Before release, verify:

- simultaneous initial submissions and repeated retries produce one request;
- events delivered twice or out of order do not duplicate decisions or billing;
- dashboard and email derive from the same revision, including projection delay and notification failure;
- approval becomes stale after a material request change;
- handoff acceptance, rejection, timeout, interruption, and escalation always leave a visible owner;
- compliance denial, integration failure, correction, cancellation, and retry preserve work and audit history;
- billing timeout and repeated callbacks create no duplicate charge;
- unauthorized actors cannot access evidence through dashboards, emails, logs, or links;
- retention and deletion rules preserve legally required audit material while removing eligible personal data;
- keyboard and assistive-technology users can submit, review status, correct failures, and complete handoffs;
- reconciliation detects divergent projections without silently overwriting authoritative facts.

These checks require integration tests, fault injection, security/privacy review, and affected-actor acceptance testing. None were run because the request prohibits modification and the fixture contains no implementation.

Material decisions still open are the owner of the canonical workflow record, which request changes invalidate approvals, handoff/escalation deadlines, privacy retention periods, and whether regulation requires billing authorization before or after compliance approval.