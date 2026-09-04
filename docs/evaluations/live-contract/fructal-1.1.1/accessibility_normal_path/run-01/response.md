The fixture contains only `state=blocked`; it provides no implementation, interface, actor roles, or reason for the block. The replacement below is therefore a design proposal, not validated behavior.

### Replacement approval motion

1. **Present one approval task**

   Show the request as a single, keyboard-focusable region containing:

   - Current status: “Blocked — awaiting approval”
   - Request owner and approver
   - What will happen if approved
   - Any irreversible, external, security, cost, or data effects
   - “Approve” as the primary action and “Decline” as a distinct action

   The same information must be available as visible text and programmatic names/descriptions. It must not exist only in hover content, color, icons, or pointer-only popovers.

2. **Use the same consequence preview for every input method**

   Activating “Approve” by pointer, Enter, or Space opens the same review step. Move keyboard focus to its heading and expose it as a labelled dialog or equivalent page region.

   The review step contains:

   - The exact request being approved
   - Immediate and downstream consequences
   - Affected people, systems, or records
   - Whether the action can be reversed
   - “Confirm approval” and “Go back”

   Opening the preview is not consent. Confirmation is required only when approval has a meaningful consequence; routine approvals should complete directly if no further decision is necessary.

3. **Preserve context through confirmation**

   “Go back,” Escape where safe, or closing the review returns focus to the original Approve control. Preserve entered comments, scroll position, request selection, and approval ownership.

   Confirming approval disables repeated submission without removing focus or context. Expose “Approval in progress” visibly and through a polite live region. Use `aria-busy` on the affected region when applicable.

4. **Provide equivalent completion feedback**

   On success:

   - Change the authoritative status to “Approved”
   - Announce “Request approved” through a live status region
   - Move focus to a persistent completion summary when the interface substantially changes
   - Show approver, timestamp, and resulting next step
   - Remove or disable actions that are no longer valid

   Feedback should remain on screen and in the document structure; a disappearing toast alone is insufficient.

5. **Keep recovery beside the failure**

   On failure, preserve comments and the pending request. Keep focus within the approval task and show:

   - “Approval not completed”
   - A useful, non-technical reason when known
   - Whether the request remains pending or ownership changed
   - “Try again” for retryable failures
   - “Return to request” or an identified escalation/contact path for non-retryable failures

   Announce the failure assertively without repeatedly interrupting the user. Retrying must not create duplicate approvals.

6. **Handle delay and handoff explicitly**

   If completion is delayed, show “Approval submitted — confirmation pending,” announce it, and provide an inspectable status rather than leaving the control spinning indefinitely. A refreshed page or another channel must derive from the same authoritative state. If another approver acts first, explain that outcome and retain access to the completed record.

### State model

`Blocked / awaiting approval → Reviewing consequences → Submitting → Approved`

Material alternatives:

- `Reviewing → Blocked` when the user goes back
- `Submitting → Blocked with retained input` after a retryable failure
- `Submitting → Confirmation pending` after a timeout or uncertain response
- `Blocked → Declined` through its own consequence-aware motion
- `Any pending state → Completed by another actor` when ownership changes concurrently

The approval constraint remains intact: only an authorized approver can commit the decision, and consequential effects remain visible before commitment. The redesign removes input-method-dependent access and prevents status loss during failure or delay.

### Verification plan

Verify with pointer, keyboard alone, and at least one representative screen reader/browser pairing that:

- Status and consequence details are reachable in a logical reading and tab order.
- Enter and Space invoke the same action as a pointer click.
- Focus moves into the preview and returns correctly on cancellation.
- Approving requires no hover, drag, precise targeting, or timed interaction.
- Pending, success, failure, timeout, and concurrent-completion states are both visible and announced once.
- Comments, position, selection, and ownership survive cancellation, failure, and retry.
- Repeated activation cannot create duplicate approval.
- Refresh and cross-actor handoff show the same authoritative status.
- Color, animation, sound, and transient toast messages are not the sole feedback.
- Unrelated requests and their state remain untouched.

Real keyboard and screen-reader acceptance testing is still required. The fixture does not identify the UI technology, authorization rules, consequence types, live-region behavior, or source of truth, so those remain open implementation decisions. No files were modified.