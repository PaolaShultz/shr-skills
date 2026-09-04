Redesign mode

`workflow.txt` remains unchanged at `state=blocked`. The required approval is preserved, but the current state provides no owner, status, feedback, or recovery route.

### Replacement motion

Replace the generic blocked state with an explicit approval lifecycle:

1. Work reaches the approval boundary and entered work is retained.
2. Create an approval request containing:
   - request ID
   - approving role/owner
   - submitted revision
   - approval scope
   - request timestamp and status
3. Set the workflow to `awaiting_approval`, showing who must act and whether the request was delivered.
4. Resolve the request through one clear action:
   - **Approve:** atomically mark that revision approved and resume the workflow.
   - **Request changes:** return it to the submitter with feedback while preserving work.
   - **Cancel:** close the request without discarding work.
5. For delays or delivery failures, expose retry/escalation beside the stalled state. Escalation ownership and timing remain policy decisions.

The approval must remain bound to the submitted revision; later edits invalidate it and require a new request. This preserves the constraint without allowing stale or ambiguous approval.

### Proposed state representation

```text
state=awaiting_approval
approval_request_id=<id>
approval_status=pending
approval_owner=<role-or-actor>
submitted_revision=<revision>
requested_at=<timestamp>
delivery_status=<delivered|failed>
```

Terminal transitions should be `approved`, `changes_requested`, or `cancelled`, each recording actor, timestamp, and revision.

### Verification plan

Verify that:

- Submission retains work and creates exactly one inspectable approval request.
- Approval resumes only the matching revision.
- Rejection returns actionable feedback without losing context.
- Duplicate approval actions are idempotent.
- Failed delivery offers retry without duplicating requests.
- Interruption and reopening restore the same request and workflow position.
- Cancellation preserves draft work and clearly closes responsibility.
- Status, owner, feedback, and recovery controls are keyboard- and assistive-technology-accessible.
- Unrelated workflow state remains unchanged.

Implementation was not performed because the explicit Redesign-mode boundary prohibits modifying the system. Material open decisions are the approving owner, escalation policy, timeout, and authoritative storage format.