The only observable workflow evidence is `state=blocked` in [workflow.txt](/tmp/fructal-eval-accessibility_normal_path-01-j94h2ybw/fixture/workflow.txt:1). The current interface, approval consequences, and recovery behavior are unavailable, so the proposal below is a design—not a validated description of existing behavior.

### Replacement approval motion

1. **Present one shared approval state**
   - Show a visible status heading such as “Awaiting your approval.”
   - Expose the same text programmatically as the region’s accessible name.
   - Place focus on the heading only when the approval view opens through navigation; do not unexpectedly move focus during routine updates.

2. **Preview consequences before commitment**
   - Display what will happen, affected target, scope, initiator, and whether the action is reversible.
   - Associate this preview with the native **Approve** button using accessible description markup.
   - Provide **Approve** and **Decline** as ordinary keyboard-focusable buttons—not pointer-only cards, hover controls, or custom click handlers.
   - Put advanced details behind an accessible disclosure that works with Enter and Space.

3. **Commit through one explicit action**
   - Activating **Approve** by click, Enter, or Space invokes the identical handler.
   - If approval has a destructive or external consequence, use one confirmation dialog that restates that exact consequence. Focus begins on the safest action, remains inside the dialog, and returns to the initiating control when cancelled.
   - Do not add a second confirmation when intent was already captured explicitly and precisely.

4. **Expose progress consistently**
   - After submission, disable duplicate approval while preserving readable context.
   - Change visible status to “Approval in progress” and announce it through a polite live region.
   - Keep keyboard focus stable unless navigation is necessary.
   - The server-side approval state remains the source of truth; pointer and assistive-technology feedback derive from the same state transition.

5. **Confirm completion**
   - On success, show and announce “Approved,” including what completed and any next step.
   - Replace or disable the approval controls so repeated activation cannot create duplicate effects.
   - If the workflow continues elsewhere, provide a clearly named native link or button and preserve the user’s context.

6. **Recover beside the failure**
   - On failure, retain the consequence preview, entered information, and approval intent.
   - Show a persistent inline error near the controls and announce it assertively once.
   - Explain whether nothing changed, the result is uncertain, or partial completion occurred.
   - Offer a keyboard-accessible **Try again** action when retry is safe; otherwise provide **Check status** or a named escalation path.
   - Return focus to the error summary only when necessary to make the failure discoverable, with links back to affected fields or controls.

### What remains unchanged

The approval constraint, authorization checks, audit trail, ownership rules, and backend integrity protections remain intact. Accessibility is incorporated into the normal approval path rather than implemented as a separate mode.

### Verification plan

Verify with keyboard-only operation and at least one screen reader/browser combination that:

- Status, consequence preview, control names, and relationships are announced in a logical reading order.
- Tab, Shift+Tab, Enter, Space, and Escape support the complete approve, decline, cancel, and retry paths.
- Pointer and keyboard activation produce the same backend request and state transitions.
- Progress is announced once without stealing focus.
- Success communicates the same completed consequence visually and programmatically.
- Failures retain context and expose whether retry is safe.
- Duplicate activation cannot produce duplicate approval.
- Refresh, interruption, and return show the authoritative current status rather than stale controls.
- Contrast, focus visibility, zoom, and touch-target behavior remain usable.

Affected keyboard and screen-reader users should perform acceptance testing before treating the motion as validated. No files or system state were modified.