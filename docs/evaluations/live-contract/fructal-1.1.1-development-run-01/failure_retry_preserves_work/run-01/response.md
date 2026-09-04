The fixture only exposes `state=blocked` in [workflow.txt](/tmp/fructal-eval-failure_retry_preserves_work-01-a0k0oyt7/fixture/workflow.txt:1), so the detailed current implementation is unavailable. The following is a replacement motion, not a validated implementation.

### Replacement submission motion

1. When the submission form opens, create one durable draft with:

   - `draft_id`
   - entered title
   - return location
   - selected-file staging records
   - one stable `request_id` reserved for final submission

2. Save title and return location to the draft as they change. Show a clear “Saved” or “Saving failed—retry” status without blocking editing.

3. When files are selected, upload them into temporary staging immediately. Record stable file IDs in the draft. Do not claim files are preserved until staging succeeds; browser-local file selections alone generally cannot survive a reload or process loss.

4. Enable **Submit** only when the title is saved and every selected file is staged. The action sends the stable `request_id`, draft version, title, staged file IDs, and return location.

5. On success, atomically create or resolve the document for that `request_id`, mark the draft submitted, and navigate to the saved return location.

6. On timeout, retain the form and all draft state. Show:

   > Submission status is unknown. Your title and files are preserved.

   The primary action becomes **Check status**, not a fresh submission.

7. Status reconciliation uses the same `request_id`:

   - If completed, return the existing document and navigate to the saved location.
   - If still processing, show progress and allow another status check.
   - If definitively not accepted, offer **Retry submission** using the same request identity and staged files.
   - If staging expired or a file is unavailable, identify only the affected file and request its replacement; preserve everything else.

### Required service contract

`request_id` must be an idempotency key scoped to the submitting actor. Repeated requests with the same identity and equivalent payload return the same submission result rather than creating duplicates. A conflicting payload must produce an explicit conflict, not silently replace the original request.

The draft and staged files need a documented retention period. Expiration must be visible before submission and extended during active retry or reconciliation where policy permits. These preserve data integrity and request identity without weakening authorization, ownership, malware scanning, storage, or privacy controls.

### What remains unchanged

Authentication, file validation, authorization, scanning, storage limits, and final-submission rules remain enforced. Draft creation and file selection do not count as consent to submit.

### Verification plan

Verify that:

- A timeout before, during, and after server acceptance retains the title, staged file IDs, return location, and original `request_id`.
- Retrying after an accepted-but-timed-out request returns the existing submission without duplication.
- Reload, navigation away and back, session interruption, and another authenticated device restore the durable draft where policy permits.
- One failed or expired file can be replaced without resetting other files or text.
- Conflicting reuse of a request identity is rejected visibly.
- Keyboard and assistive-technology users receive perceivable save, staging, timeout, reconciliation, and completion status.
- Cancellation removes or expires staged data according to policy without affecting already completed submissions.

No system files were modified. The main open decisions are draft/file retention duration, whether cross-device restoration is permitted, and the exact authorization scope for `request_id`; these require product, privacy, and security ownership.