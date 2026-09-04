The current fixture contains only `state=blocked`; no implementation details are available. The following is therefore a replacement design, not a validated change. No files were modified.

### Replacement submission motion

1. **Create a stable draft immediately**
   - On opening the form, create a `draft_id`.
   - Capture the allowlisted return location as `return_to`.
   - Persist the title whenever it changes, both locally and to the draft service when available.
   - Keep the same `draft_id` through timeouts, reloads, and retries.

2. **Stage selected files before final submission**
   - Upload each selected file to temporary storage using resumable uploads.
   - Store stable attachment references under the draft, with filename, size, upload progress, and checksum.
   - A reload reconstructs the selection from those references; it must not depend on browser file-input state.
   - Failed uploads offer **Resume** or **Remove** beside the affected file without disturbing the title or other files.

3. **Submit one immutable snapshot**
   - The obvious **Submit documents** action first confirms all files are staged, then creates a snapshot containing:
     - `draft_id`
     - title
     - ordered attachment references and checksums
     - `return_to`
     - stable `request_id`
   - Send the request with `request_id` as its idempotency key.
   - Lock that snapshot for the attempt while allowing later edits to remain in a separate draft revision.

4. **Handle timeout as an unknown result—not a failure**
   - After a timeout, retain the complete form and show: “We couldn’t confirm whether the request completed.”
   - The primary action is **Check status and retry**.
   - First query status using the same `request_id`:
     - **Completed:** show the existing receipt and return action.
     - **Processing:** continue status checks without sending another submission.
     - **Not received / safely retryable:** resend the identical snapshot with the same idempotency key.
     - **Indeterminate:** retain everything and provide another status check plus an escalation/reference path.
   - Never generate a new request identity merely because the user retries.

5. **Complete without losing navigation context**
   - On confirmed success, show the receipt before navigation.
   - **Return** uses the preserved, validated `return_to`.
   - Browser back, reload, interruption, or reopening the draft restores the title, staged files, return location, request identity, and latest known status.

6. **Discard explicitly**
   - Leaving the page does not discard the draft.
   - **Discard draft** is a separate, explicit action that explains it will remove staged files and saved input.
   - Temporary files follow the applicable retention policy; expiry is disclosed while the draft is still recoverable.

### What remains unchanged

- Authentication, authorization, file-type and size restrictions, malware scanning, retention requirements, and destination permissions remain enforced.
- Retry does not bypass validation or create a second request.
- `return_to` must be an allowlisted route or opaque server-issued token, not an unrestricted URL.
- Staged content must receive the same privacy, encryption, access-control, and deletion protections as other uploaded documents.

### Essential state model

`Draft → Uploading → Ready → Submitting → Processing → Completed`

A timeout changes only the client’s knowledge:

`Submitting/Processing → Outcome unknown`

It does not clear the draft or create a new submission. Retry reconciles the existing `request_id` before replaying the same snapshot.

### Verification plan

- Enter a title, select multiple files, and force a timeout before and after server acceptance; confirm all four required values survive: title, files, return location, and request identity.
- Retry repeatedly and concurrently; confirm exactly one request/receipt is created.
- Reload or close and reopen during upload, submission, and unknown-result states; confirm recovery resumes from persisted state.
- Fail one file upload; confirm other files and entered data remain intact.
- Confirm checksum mismatch or expired staging produces targeted recovery without silently changing the submission.
- Complete successfully after a timeout; confirm status reconciliation finds the receipt rather than duplicating the request.
- Verify keyboard and assistive-technology users receive announced upload, timeout, retry, processing, and success states, with focus moved to the relevant recovery control.
- Confirm another account cannot discover the draft, staged attachments, request status, or return context.
- Confirm explicit discard removes recoverable draft state according to policy while ordinary navigation does not.

The main unresolved decisions are the authorized draft-retention duration, the canonical owner of idempotency/status records, and whether existing storage supports resumable staging. These affect implementation details but not the replacement motion.