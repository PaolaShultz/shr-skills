Redesign mode.

`workflow.txt` was inspected and left unchanged at:

```text
state=blocked
```

The required approval is a valid constraint, but the current motion turns it into an indefinite, ownerless stop. The file does not preserve the request, approver, status, or recovery path.

Proposed replacement motion:

```text
state=awaiting_approval
approval.required=true
approval.owner=<approver>
approval.request=<decision being approved>
approval.requested_at=<timestamp>
approval.return_to=<next workflow state>
```

Transitions:

- Approval granted → record the decision and resume at `approval.return_to`.
- Approval rejected → record the reason and return the work to its owner for revision.
- Approval unavailable or delayed → keep all context, expose the pending owner, and allow an authorized reassignment or escalation.
- Retry or interruption → reuse the existing request unless its decision-relevant content changed, avoiding duplicate approval.

This preserves the approval constraint while making responsibility, status, and recovery inspectable. Verification should cover approval, rejection and revision, interruption and resume, delayed escalation, duplicate actions, and preservation of unrelated state.

No implementation was performed because the explicit Redesign mode is the maximum permitted outcome; modifying `workflow.txt` would violate that boundary. The material open decisions are the approver, the approval subject, the valid post-approval state, and escalation policy.