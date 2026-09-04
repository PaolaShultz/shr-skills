Redesign mode

The only observed workflow evidence is `state=blocked` in [workflow.txt](/tmp/fructal-eval-accessibility_normal_path-01-2dto7r_x/fixture/workflow.txt:1). The cause, interface, approval consequence, and current pointer behavior are unavailable, so the proposal below preserves those as explicit product decisions rather than inventing them.

### Replacement approval motion

1. **Present one approval surface for every input method**
   - Use a semantic heading, status text, consequence summary, and native **Approve** and **Cancel** buttons.
   - Do not place essential status or consequences exclusively in hover content, color, icons, or pointer-triggered popovers.
   - When the surface opens, move focus to its heading or consequence summary and announce the current approval status.

2. **Preview consequences before commitment**
   - Immediately before **Approve**, state what will happen, which records or actors are affected, whether notification or another external effect occurs, and whether approval is reversible.
   - Keep this content visible and programmatically associated with the Approve button.
   - Require an additional confirmation only for a genuinely destructive or externally consequential approval. Keyboard and pointer activation must enter the same confirmation state.

3. **Commit through one input-independent action**
   - Both pointer activation and `Enter`/`Space` on the native Approve button invoke the same operation.
   - On activation, disable duplicate submission, retain context, expose a visible “Approving…” status, and announce it through a polite live region.
   - Do not move focus merely because processing began.

4. **Return definitive completion feedback**
   - On success, update the visible status to **Approved**, announce completion, identify any coupled effect such as notifications, and expose the next relevant action.
   - Move focus to the success heading only if the approval surface is replaced; otherwise keep focus in a stable, logical position.
   - Repeated activation must not create duplicate approvals or notifications.

5. **Recover beside the failure**
   - On failure, preserve entered work, selection, and surrounding context.
   - Show and announce a concise error beside the approval controls, explain whether anything changed, and provide a focused **Try again** action.
   - Put focus on the error summary only when users must act on it. If retry is unsafe or unavailable, expose the responsible owner or escalation route instead of leaving the request blocked.

6. **Handle interruption and cancellation explicitly**
   - Before submission, Cancel closes the surface and returns focus to the control that opened it.
   - During processing, allow cancellation only if the underlying operation supports it safely; otherwise disclose that processing is still underway.
   - On return or refresh, restore the authoritative status rather than replaying stale local success or failure feedback.

### Constraints preserved

- **Accessibility:** keyboard and assistive-technology users receive the same status, preview, feedback, and recovery semantics as pointer users.
- **Authorization and ownership:** approval still requires an authorized actor and retains an auditable approver identity.
- **Data integrity:** submission is idempotent and status comes from the authoritative approval state.
- **Safety and consent:** consequential effects are disclosed before commitment, without treating navigation or authentication as consent.
- **Existing business behavior:** approval rules and downstream effects remain unchanged until their actual definitions can be inspected.

This motion passes the cap test conceptually: the obvious action has one result, consequences remain legible, context and intent survive processing, and every terminal state supplies accessible feedback and a route forward. It has not been validated against an implementation or affected users.

### Verification plan

Verify with pointer, keyboard-only, and representative screen-reader/browser combinations:

- Reach the approval, read current status and complete consequence preview, then approve without pointer input.
- Confirm focus order, accessible names/descriptions, and announcements for ready, processing, success, and failure states.
- Confirm success identifies all effects and that focus remains predictable.
- Force a failure; confirm no input or context is lost, unchanged state is explicit, and retry succeeds without duplicate effects.
- Interrupt processing, refresh, navigate away and return, and confirm authoritative status is restored.
- Activate repeatedly and confirm only one approval and one set of downstream effects occurs.
- Check visible focus, contrast, zoom/reflow, and operation without hover, color, animation, or audio cues.
- Supplement automated checks with keyboard and screen-reader usability testing; automation alone cannot establish equivalent experience.

Open decisions requiring owning-system evidence are the exact consequence text, reversibility, whether processing can safely be cancelled, the authoritative source of status, and the escalation owner for non-retryable failures. No files were modified.