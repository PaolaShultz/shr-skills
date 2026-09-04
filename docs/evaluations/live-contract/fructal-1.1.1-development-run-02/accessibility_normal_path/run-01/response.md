The only available workflow evidence is [`workflow.txt`](/tmp/fructal-eval-accessibility_normal_path-01-sbkxvtcv/fixture/workflow.txt), which reports `state=blocked`. No interface, state model, or implementation is present, so the proposal below is a design—not validated behavior.

### Replacement approval motion

1. Present one semantic approval region containing:

   - Current status, such as “Awaiting your approval.”
   - What will happen if approved.
   - Material side effects, affected scope, reversibility, and who will be notified.
   - “Approve” as the primary action and “Decline” or “Cancel” as distinct alternatives.

2. Make every action a native keyboard-operable control with an accessible name. Keep keyboard focus order aligned with the visible order; do not require hover, pointer gestures, or a special screen-reader path.

3. When “Approve” is activated by pointer, Enter, or Space, use the same state transition:

   - If no further decision is necessary, submit immediately.
   - If confirmation is necessary because the effect is destructive or externally consequential, open one accessible confirmation dialog showing the exact consequence. Move focus into it, trap focus while open, support Escape to cancel, and return focus to “Approve” after cancellation.
   - Do not require duplicate confirmation when exact intent was already established.

4. While processing:

   - Disable repeat submission without removing the focused control.
   - Change the visible status to “Approval in progress.”
   - Announce the same status through a polite live region.
   - Preserve entered information, approval context, and the actor’s position.

5. On success:

   - Replace the pending state with an explicit completed state containing outcome, timestamp, approver, and affected scope.
   - Announce concise completion feedback, such as “Approved successfully.”
   - Move focus only when necessary; otherwise keep it stable and expose the result immediately after the action.
   - Provide the same next action to all users, such as “View approved item.”

6. On failure:

   - Keep all input and context.
   - Show and announce a specific failure status beside the approval controls.
   - Provide a keyboard-accessible “Retry approval” action at the failure point.
   - If retry is unsafe or unavailable, state why and identify the responsible recovery route.
   - Restore focus to the error summary or retry control, with a programmatic relationship between the error and failed action.

Pointer, keyboard, and assistive-technology activation must all call the same approval command and consume the same status model. Accessibility should be part of the normal motion, not a parallel workflow.

### What remains unchanged

Authorization rules, approval eligibility, audit requirements, irreversible-effect safeguards, and business consequences remain intact. The redesign changes how those constraints are surfaced and navigated, not whether they apply.

### Verification plan

Verify with pointer-only, keyboard-only, and screen-reader paths that:

- Pending status and consequence preview are both visible and programmatically available before commitment.
- Tab, Shift+Tab, Enter, Space, and Escape behave predictably with no focus loss.
- All input methods trigger the same command and resulting state.
- Processing, success, and failure are both visually presented and announced.
- Duplicate activation cannot create duplicate approvals.
- Cancellation returns users to the preserved approval context.
- A failed request retains work and offers an adjacent, operable recovery action.
- Refresh, delayed completion, or handoff to another session reads from the authoritative approval state rather than leaving stale “in progress” feedback.

Real screen-reader testing should cover at least one common browser/reader pairing on each supported platform; automated accessibility checks alone cannot establish equivalent usability.

Open decisions requiring product or implementation evidence are which consequences require confirmation, whether approval can be undone, the authoritative state source, timeout behavior, and who owns recovery when retry is prohibited. No files were modified.