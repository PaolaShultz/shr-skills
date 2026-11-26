Make the consequence preview part of the normal approval path. The approver should be able to read what approval will do, make a separate choice to approve, and hear whether that choice succeeded or needs attention.

**Proposed approval flow**

1. **Review the consequences.** A keyboard-focusable “Review approval” button opens the preview with Enter or Space. Move focus to the “Consequences of approval” heading. Put the full preview immediately after it in reading order, followed by native “Approve” and “Cancel” buttons. Opening the preview has no approval effect.
2. **Approve or cancel.** Only an explicit press of “Approve” submits the reviewed action. While it is pending, announce “Submitting approval” and prevent repeat submissions. Cancel or Escape before submission returns focus to “Review approval” and preserves the request and any entered work.
3. **Report the outcome where the approver is working.** On success, show and announce “Approved” beside the request. On a confirmed failure, keep the preview open and focus a visible error heading that explains what happened. Put the recovery control immediately after the explanation, with a specific label such as “Retry approval.” Preserve entered work and the reviewed consequences.
4. **Recover after interruption.** If the response is lost, show and announce “Checking approval status.” The system should look up the original submission when the approver returns. Offer retry only after confirming that approval did not take effect. If the consequences have changed, show the updated preview and require a fresh decision.

The supplied requirement establishes that the approver must be able to review the consequences before authorizing the effect. The keyboard barrier and missing failure announcement are reported symptoms. The fixture contains only `state=blocked`, so it does not establish their cause or whether submission status can currently be retrieved. The design requires a retrievable status tied to the original submission.

**Verification plan**

- Using only the keyboard, open the preview, read through long content, reach both actions with visible focus, and cancel. Verify that focus returns to the trigger, entered work survives, and no approval occurs.
- With a screen reader, complete one successful approval and force one confirmed failure. Verify that the preview is readable in order, each outcome is announced once, and the recovery control is reachable from the error.
- Delay or drop the response, press Approve repeatedly, then reopen the request. Verify that the recovered status matches the recorded outcome and that at most one approval takes effect. Change the consequences before retry and verify that fresh approval is required.
- Across those paths, compare unrelated requests, their owners, and their approval states before and after.

No files were modified. These checks describe how to verify the proposed flow once implemented.