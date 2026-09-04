Redesign mode.

`workflow.txt` currently contains only `state=blocked`. This preserves the approval constraint but creates workflow-level obstruction: it identifies neither the required action nor its owner, and provides no recovery path.

Replacement motion:

1. When approval becomes necessary, transition to `pending_approval`, not a generic blocked state.
2. Record the approval owner, request identifier, submission time, and retained workflow context.
3. Present the approver with explicit `approve` and `reject` actions.
4. On approval, atomically transition to `ready` and resume from the retained position.
5. On rejection, transition to `changes_requested`, preserve existing work, and attach the reason plus a direct resubmission path.
6. If approval stalls, expose status and escalation ownership without bypassing approval.

Proposed representation:

```text
state=pending_approval
approval_status=requested
approval_owner=<owner>
approval_request_id=<id>
resume_from=<retained workflow position>
```

The required approval remains intact. Entered work, intent, ownership, and resumption context are preserved; approval becomes an actionable wait rather than an unexplained dead end.

Verification should cover:

- Approval advances the same workflow exactly once.
- Rejection retains work and supports correction and resubmission.
- Refresh, interruption, and handoff preserve status and context.
- Duplicate approval events do not duplicate downstream work.
- Missing or expired approval requests provide nearby recovery.
- Unauthorized actors cannot approve or bypass the constraint.
- Status and actions remain keyboard- and assistive-technology-accessible.

No files were modified. The explicit Redesign boundary prohibits implementation, so the requested implementation was intentionally not performed. The approval owner, timeout/escalation policy, and exact retained context remain open decisions because the fixture contains no evidence defining them.