The fixture provides only one observed workflow fact: `state=blocked`. It does not expose the interface, approval consequences, status model, or current pointer behavior. The proposal below therefore treats those details as open implementation inputs—not validated behavior.

### Replacement approval motion

1. **Present one approval summary to every user**
   - Show the current status in persistent text, such as “Awaiting your approval.”
   - Identify the request, owner, requested action, and last update.
   - Use the same content and underlying state for pointer, keyboard, and screen-reader paths.

2. **Make the consequence preview directly reachable**
   - Provide a native button labeled **Review approval consequences**.
   - Pointer click and keyboard activation (`Enter` or `Space`) open the same review panel.
   - Do not place essential information exclusively in hover tooltips.
   - The button’s accessible name and expanded state must be programmatically exposed.

3. **Show consequences before commitment**
   - The review panel explains:
     - What approval will change.
     - Who or what will be affected.
     - Whether the action is reversible.
     - Any notifications or external effects.
   - Place **Approve** and **Cancel** after this content in logical reading and tab order.
   - Require no additional confirmation unless the approval is destructive or externally consequential and the first action did not already express exact intent.

4. **Submit through one shared action**
   - Pointer click and keyboard activation invoke the same approval command.
   - On submission, disable duplicate activation and expose a persistent **Approving…** status.
   - Announce the transition through an appropriate live region, while keeping visible text for users who miss or suppress announcements.
   - Preserve focus context rather than moving it unexpectedly.

5. **Provide unambiguous completion**
   - On success, replace the pending state with persistent text such as **Approved by [actor] at [time]**.
   - Announce completion to assistive technology.
   - Move focus only when necessary; otherwise keep it on the updated control or a meaningful status target.
   - Update every source of truth from the same result so visual and assistive states cannot diverge.

6. **Put recovery beside failure**
   - On failure, retain the review panel, entered information, request context, and approval intent.
   - Display and announce a specific failure message beside the action.
   - Offer a keyboard-accessible **Try again** button using the same command.
   - If retry is unsafe or unavailable, provide the next responsible actor or escalation route rather than leaving the workflow at `blocked`.
   - Cancellation returns focus to **Review approval consequences** without losing the request’s state.

### What remains unchanged

The approval requirement, authorization rules, audit trail, and underlying consequences remain intact. The redesign changes how users move through and perceive the workflow; it does not weaken the constraint or create a separate “accessible” approval path.

### Verification plan

Verify against the implemented interface:

- Complete review and approval using pointer only, keyboard only, and a screen reader with the keyboard.
- Confirm all three paths receive identical status text, consequence content, result, and recovery options.
- Check logical reading and tab order, visible focus, native button activation, focus return after cancellation, and focus behavior after success or failure.
- Confirm progress, success, and failure are both persistent visually and announced programmatically.
- Test failure followed by retry and ensure no request context or entered work is lost.
- Test repeated activation and delayed responses to ensure only one approval occurs.
- Confirm a refresh or handoff shows the authoritative approval state rather than stale “pending” or `blocked` state.
- Test at high zoom and with reflow to ensure consequences and recovery controls remain reachable.

Affected-user testing is still required; automated accessibility checks alone cannot validate announcement timing, comprehension, or practical recovery. No files were modified.