Fructal Cap Design applies: the required consequence preview must remain, but its current presentation blocks keyboard users and leaves screen-reader users without recovery feedback. The only fixture evidence is [`workflow.txt`](/tmp/fructal-eval-accessibility_normal_path-01-37r35wqe/fixture/workflow.txt), which records `state=blocked`; no implementation details were available.

### Replacement approval motion

1. **Open approval review**
   - The initiating action opens a modal dialog or dedicated review page.
   - Move focus to its descriptive heading.
   - Identify the approving action and affected target explicitly.

2. **Present consequences in the keyboard path**
   - Render the consequence preview as ordinary semantic content, not hover-only UI.
   - Place it before the decision controls in DOM and focus order.
   - Include the exact scope, irreversible effects, and downstream notifications or charges where applicable.
   - Associate required acknowledgements with visible labels and instructions.

3. **Offer one clear decision**
   - Provide “Approve” and “Cancel” controls with distinct accessible names.
   - Keep “Approve” unavailable until every genuinely required acknowledgement is complete, and explain why through persistent text.
   - Escape or “Cancel” closes the review without performing the action or losing prior work; focus returns to the initiating control.

4. **Submit safely**
   - After activation, disable duplicate submission and expose a programmatic “Approval in progress” status.
   - Preserve the preview, entered context, and approval intent during processing.
   - If the outcome becomes uncertain, check transaction status before enabling retry.

5. **Report the outcome**
   - Success: announce a concise status, identify what was approved, and provide the next destination.
   - Failure: place a visible error summary next to the approval controls, announce it through `role="alert"` or an assertive live region, and move focus to the summary when further action is required.
   - Preserve all review state. Give “Try again” only when replay is safe; otherwise provide “Check status” or an escalation path.
   - The application owns technical recovery. The user owns only the approval decision.

This keeps the necessary preview active at the moment of commitment without making accessibility an additional task.

### Verification plan

Test with keyboard alone and at least one screen reader:

- Tab and reverse-tab reach the preview, acknowledgements, Approve, and Cancel in a coherent order.
- Focus enters the review predictably and returns correctly after cancellation.
- The preview is readable without hover, pointer input, or visual positioning.
- Approve produces exactly one request, including after repeated activation.
- Success and failure are both visible and announced; failure exposes a usable recovery action.
- Entered work, scope, position, and acknowledgements survive failure and interruption.
- Cancellation causes no external effect.
- An uncertain timeout triggers status inspection before retry, preventing duplicate approval.
- Reopening or handing off the blocked item retains enough context to understand its status and owner.
- Existing unaffected workflow state remains unchanged.

Open implementation questions are the exact consequence fields, whether approval is reversible, and what backend status or idempotency support exists. Those determine the final wording and safest retry behavior; they do not change the motion above. No files were modified.