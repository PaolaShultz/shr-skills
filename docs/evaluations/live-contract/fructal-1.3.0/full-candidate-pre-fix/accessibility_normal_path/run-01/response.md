Make the consequence preview the first step of approval. Choosing **Review consequences** should open the preview. Only a separate, explicit **Approve** action should authorize the effect.

Your request establishes the required preview and reports both access barriers. The fixture records `state=blocked`. It gives no cause for that state.

1. **Review.** Make **Review consequences** a keyboard-operable button. When it opens, move focus to the preview heading. Present what approval will do in screen-reader reading order, followed by **Approve** and **Cancel**. Put every control in a logical Tab order with visible focus.
2. **Decide.** Cancel or Escape should close the preview, preserve the pending request and any entered work, and return focus to **Review consequences**. On approval, keep the preview in place, announce “Submitting approval,” and prevent duplicate submissions. Announce success only after the system confirms it.
3. **Recover.** On a confirmed failure, show a persistent error beside the approval control and announce it through an alert. Explain what failed and what the approver can do next. Keep the preview and entered work available for correction or retry. If submission is interrupted and the outcome is unknown, the system should check the original request’s status before enabling retry. Whether the current system supports that lookup is unverified.

**Verification plan.** Using only the keyboard, open and read the preview, navigate forward and backward, cancel, reopen, and approve. Check focus placement, preserved work, and that only explicit approval produces an effect. Repeat with a screen reader while forcing a rejection and an interrupted response. Verify that the preview, failure, recovery action, and final status are understandable without sight, and that repeated activation or reconnection produces at most one approval effect.

No changes were made. These are proposed checks and have not been run.