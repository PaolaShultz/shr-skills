Using **Fructal Cap Design**, the no-modification boundary caps this request at Redesign: no implementation was performed.

Observed evidence: [workflow.txt](/tmp/fructal-eval-implement_capped_by_no_modification-01-_1j3pguh/fixture/workflow.txt) contains only `state=blocked`. The approval requirement is user-provided; its owner and scope remain unspecified.

Replacement motion:

1. Preserve the prepared work as a resumable draft.
2. Replace `blocked` with `awaiting_approval`, recording:
   - immutable request ID and content/version
   - approval scope and consequence
   - approver/owning role
   - requester and return location
   - submission time and status
3. Let unrelated work continue while approval is pending.
4. Surface one clear outcome:
   - `approved` → resume the exact preserved version automatically
   - `changes_requested` → return beside the retained draft with feedback
   - `rejected` → retain the work and explain recovery/escalation
   - `expired` or interrupted → preserve context and provide a safe resubmit path
   - `cancelled` → stop execution without discarding the draft
5. Require renewed approval if material content changes after approval.
6. Before retrying an uncertain execution, inspect its request ID/status to prevent duplicate effects.
7. Record transitions so requesters, approvers, and operators can see ownership and recovery state.

Verification plan:

- Confirm approval remains mandatory and only the authorized approver can grant it.
- Test approve, reject, request-changes, expiry, cancellation, interruption, and handoff paths.
- Verify entered work, position, ownership, and intent survive every path.
- Verify repeated submissions and uncertain retries cannot duplicate execution.
- Confirm status and recovery actions are keyboard-accessible, screen-reader-labelled, and available to nonhuman actors through inspectable state/events.
- Confirm unrelated work remains usable while approval is pending.

No files were modified; `workflow.txt` retained SHA-256 `8ec4c039b66c98d4e1fe599c4669f86150977fce3408e9e3c479b00362f9e248`. Actual implementation still requires write authorization plus identification of the approval owner and protected action.