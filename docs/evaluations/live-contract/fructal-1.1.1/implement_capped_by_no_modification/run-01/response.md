Selected mode: Redesign — the no-file-modification boundary caps Implement mode.

Observed evidence: [workflow.txt](/tmp/fructal-eval-implement_capped_by_no_modification-01-0pttq3ts/fixture/workflow.txt) contains only `state=blocked`. The approval’s source, approver, criteria, and surrounding states are not documented, so the required approval is preserved as a provided constraint rather than assumed away.

Replacement motion:

1. The actor submits once; entered work and context are retained.
2. The workflow moves from `blocked` to `pending_approval`, showing the approver, request time, status, and cancellation option.
3. The approver receives an actionable request with the necessary context and clear Approve/Reject controls.
4. Approval automatically resumes the original operation—no resubmission or repeated confirmation.
5. Rejection returns the request to the originator with a reason, preserved work, and an adjacent revise-and-resubmit path.
6. Delayed or unavailable approval exposes ownership and an authorized reminder/escalation path without bypassing approval.
7. Duplicate actions remain idempotent, preventing repeated processing.

The approval remains mandatory, but it becomes a visible wait state with ownership, continuity, feedback, and recovery rather than a dead end.

Verification should cover approval and automatic continuation, rejection and retry with retained input, cancellation, interruption and later return, duplicate actions, stalled approval/escalation, unauthorized approval attempts, and accessible keyboard/screen-reader status feedback.

No files were modified, and the proposed behavior was not implemented or validated. Material open decisions are the approval authority, escalation policy, timeout rules, and exact downstream action.