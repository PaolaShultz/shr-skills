The artifact only exposes `state=blocked`; it does not record the request, approver, status, or recovery path. The approval requirement is preserved, but its implementation is leaving progress ownerless.

Proposed replacement motion:

1. When approval becomes necessary, create an approval record containing:
   - request and affected action
   - requester and designated approver
   - submitted time and response deadline
   - `pending`, `approved`, `changes_requested`, or `rejected` status
   - retained work/context and return destination
2. Move the workflow to `awaiting_approval`, not generic `blocked`.
3. Let unrelated work continue while preventing only the approval-dependent action.
4. Notify both actors and show the requester the current owner, deadline, and status.
5. From the approval request, the approver can:
   - approve, returning the workflow to the exact continuation point;
   - request changes with a reason, returning it to the requester with work intact;
   - reject with a recorded reason.
6. If the deadline expires or the approver is unavailable, route the request to a named backup or escalation owner. Never leave it in an ownerless wait.
7. Permit cancellation by the requester without losing the underlying draft, where retention is safe.

The approval authority and prohibition on premature execution remain unchanged. Authentication is not treated as approval, and retries cannot duplicate the consequential action.

Verification plan:

- Approval: the protected action cannot run beforehand; one approval resumes it once from the preserved position.
- Changes requested: comments and entered work survive the handoff and resubmission.
- Rejection/cancellation: no protected action occurs, and all actors receive a clear terminal status.
- Delay: the visible deadline triggers the configured reminder and escalation, with ownership always identifiable.
- Interruption/retry: reopening or retrying preserves the request and does not create duplicate approvals or executions.
- Concurrency: stale approval cannot authorize a materially changed request; changed scope requires renewed approval.
- Accessibility: status, owner, deadline, reasons, and controls are keyboard-operable and exposed with meaningful assistive-technology labels; updates do not rely on color alone.
- Auditability: each transition records actor, timestamp, decision, and request version.
- Untouched state: unrelated workflow data and independently executable work remain unchanged.

A material design decision remains open because the fixture provides no policy details: who may approve, the response deadline, escalation owner, and which request changes invalidate an approval must come from the owning policy or business authority.

No fixture files were modified.