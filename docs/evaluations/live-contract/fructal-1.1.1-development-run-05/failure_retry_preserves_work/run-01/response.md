The fixture contains only [`state=blocked`](</tmp/fructal-eval-failure_retry_preserves_work-01-lof6qfbd/fixture/workflow.txt:1>), so the failure mechanism is not observable. The following is a proposed replacement motion, not a validated implementation.

### Replacement submission motion

1. **Create a durable draft identity immediately**
   - When the submission screen opens, create one server-side `request_id`.
   - Bind it to the authenticated user and tenant.
   - Store the validated return location with that draft.
   - Reopening or reauthenticating resumes this identity instead of starting over.

2. **Continuously preserve entered work**
   - Autosave the title to the draft after edits and on blur.
   - Begin resumable file staging when files are selected.
   - Store upload tokens, filenames, sizes, checksums, and completion state under the same `request_id`.
   - Keep the selected browser `File` objects while the page remains open; completed staging makes them recoverable after reload without relying on the browser file input.

3. **Make Submit one idempotent commitment**
   - Before commitment, ensure the latest title and file references are durably recorded.
   - Submit using the stable `request_id` as the idempotency key.
   - Give each network attempt a separate `attempt_id` for diagnosis, while preserving the logical request identity.
   - The server must return the existing result when the same request is committed again, never create a duplicate.

4. **Treat timeout as an unknown outcome**
   - Do not clear the form, create another request, or label the submission failed.
   - Show: “Confirmation was interrupted. Your title and files are saved. Checking submission status…”
   - Reconcile through `GET /requests/{request_id}`:
     - `accepted`: show the receipt, then offer return to the preserved location.
     - `processing`: continue status checks without resubmitting.
     - `not_committed` or recoverable failure: show Retry beside the error.
     - authentication expired: reauthenticate, then return to the same draft and reconciliation step.

5. **Retry the commitment, not the form**
   - Retry uses the same `request_id`, title revision, staged file tokens, and return location.
   - Incomplete uploads resume from acknowledged chunks.
   - The interface remains populated throughout retry.
   - Navigation occurs only after acceptance is known or the user explicitly chooses to leave.

A compact state model is:

```text
draft → staging files → ready → committing
                              ├─ accepted → receipt → saved return location
                              └─ outcome unknown → reconcile
                                                   ├─ accepted
                                                   ├─ processing
                                                   └─ retry same request_id
```

### Constraints preserved

- **Data integrity:** idempotency prevents duplicate submissions.
- **Privacy and ownership:** drafts and uploads remain scoped to the authenticated owner and retention policy.
- **Security:** the return location is validated or represented by a server-issued route token; it is not an arbitrary redirect URL.
- **Platform limits:** browsers generally cannot silently repopulate a cleared file input. Durable, resumable staging avoids depending on that capability.
- **User intent:** selecting files or autosaving a draft does not itself commit the submission.

Cancellation should stop active transfer or processing where possible but retain the draft unless the user explicitly chooses “Discard draft.” That destructive action should name what will be removed.

### Verification plan

Verify these scenarios against observable request and draft state:

- A normal submission produces one receipt and returns to the saved location.
- A timeout before the server receives the commit leaves the title, files, return location, and `request_id` intact; Retry succeeds.
- A timeout after server acceptance reconciles to the existing receipt without a duplicate.
- Reload, tab interruption, and authentication expiry resume the same draft.
- Partial file-upload failure resumes acknowledged chunks and preserves completed files.
- Repeated Retry actions still produce one logical submission.
- A modified title after a failed attempt saves a new revision intentionally and does not silently mix revisions.
- Keyboard and assistive-technology users receive announced saving, timeout, reconciliation, failure, and success states; focus moves to the nearby recovery control.
- Another user or tenant cannot access the draft or reuse its upload tokens.
- Invalid or stale return locations fall back safely while preserving the submission.
- Explicit discard removes only the named draft and staged uploads after confirmation.

The material open decisions are draft/upload retention duration, whether users may resume across devices, and what cancellation means once server-side processing has begun. No fixture files were modified.