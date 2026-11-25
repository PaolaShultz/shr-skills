**Proposed flow:** Make the consequence preview part of the required approval step. The fixture records only `state=blocked`, so this is a design proposal.

1. A keyboard user activates **Review and approve** with Enter or Space. A dialog opens with focus on its **Review consequences** heading. The preview follows the heading in screen-reader reading order. Any preview links or controls are in the Tab sequence before **Cancel** and **Approve**.
2. Only an explicit activation of **Approve** submits the action. **Cancel** or Escape closes the dialog, returns focus to **Review and approve**, and leaves the action blocked.
3. If approval fails, keep the dialog and preview open. Update a visible `role="alert"` region with the actual outcome and recovery step. For a confirmed failure, use “Approval failed. The action is still blocked. Try again.” Keep focus on the approval control so the user can retry without navigating back. If the outcome is uncertain, announce that and provide a way to check status before retrying.

No files were changed.