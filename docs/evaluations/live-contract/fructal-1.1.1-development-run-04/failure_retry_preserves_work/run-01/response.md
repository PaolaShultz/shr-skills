The fixture only establishes `state=blocked`; it contains no implementation details. The following is therefore a replacement design based on the requested continuity guarantees, not a validated description of existing behavior.

### Replacement submission motion

1. **Create a durable draft identity**
   - On opening the submission form, create one `request_id`.
   - Persist it across refreshes, timeouts, retries, and return navigation.
   - Every subsequent operation uses this same identity.

2. **Continuously preserve the draft**
   - Save the title against `request_id` after edits.
   - Upload selected files into temporary durable staging associated with that identity.
   - Record each file’s stable upload reference, name, size, checksum, and status.
   - Persist the return location as structured navigation state, not browser history alone.
   - Show save/upload status accessibly without blocking continued entry.

3. **Submit by reference**
   - The final action sends `request_id` plus an idempotency key; it does not resend or reconstruct the draft.
   - The server atomically transitions the request from `draft` to `submitting`, then `submitted`.
   - Repeated submission calls with the same key return the same result rather than creating another request.

4. **Handle timeout as an unknown outcome**
   - A timeout must not reset the form or create a new identity.
   - The client checks status for the existing `request_id`:
     - `submitted`: show success and return using the preserved location.
     - `submitting`: show that processing is still underway and continue polling or offer a later status check.
     - `draft` or recoverable failure: restore the title, staged files, return location, and request identity, then offer **Retry submission**.
   - Retry resumes the same request; users do not reselect files or re-enter the title.

5. **Keep recovery adjacent to failure**
   - Display the failure inline with clear retained-state feedback, such as: “Submission wasn’t confirmed. Your title and 3 files are saved.”
   - Provide retry, return, and—where supported—cancel controls.
   - Returning to the prior location does not discard the draft. Explicit discard is a separate confirmed operation.

### State contract

Use a lifecycle such as:

`draft → submitting → submitted`

with recoverable outcomes returning to the same `draft`, never to an empty form. Store at minimum:

- `request_id`
- `title`
- stable staged-file references and upload status
- structured `return_location`
- submission idempotency key
- lifecycle state and last error
- timestamps or version data for conflict handling

The necessary constraints remain intact: files stay subject to upload validation, authentication and ownership checks still apply, and final submission remains explicit. Temporary files should follow the existing privacy and retention policy, with expiry communicated before it can affect recovery.

### Verification plan

Verify that:

- A timeout before, during, and after server acceptance preserves all four continuity elements.
- Retrying repeatedly produces one submitted request with the original identity.
- Refresh, browser restart, return navigation, and reauthentication restore the same authorized draft.
- Partial file-upload failure retains successful uploads and retries only incomplete files.
- Status checks distinguish “still processing” from “safe to retry.”
- Two tabs cannot silently overwrite newer title or file state.
- Keyboard and assistive-technology users receive perceivable save, failure, retry, and success feedback with focus moved to the relevant status.
- Explicit discard removes the intended draft only, while unrelated drafts and return state remain untouched.

No system files were modified. Real actor acceptance and implementation feasibility remain unverified because the fixture provides no code, storage model, authentication rules, retention policy, or interface behavior.