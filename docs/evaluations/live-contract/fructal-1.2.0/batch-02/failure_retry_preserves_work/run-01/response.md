Fructal Cap Design applies: required document scanning must remain, but the current timeout handling causes avoidable loss of work and request identity.

Evidence is limited: the request describes the erased fields, while the fixture only exposes `state=blocked` in [workflow.txt](/tmp/fructal-eval-failure_retry_preserves_work-01-i075ox1h/fixture). The proposal therefore treats the detailed current behavior as provided, not independently verified.

## Replacement motion

1. **Create a durable request identity first**
   - Generate a request ID and idempotency key before uploading.
   - Save the title, return location, and selected-file metadata against that ID.
   - Display: “Draft saved — preparing 3 files.”

2. **Upload into quarantined staging**
   - Upload files resumably under the same request ID.
   - Persist confirmed chunks and checksums.
   - Scanning remains mandatory before files can be opened, processed, or treated as accepted.

3. **Separate receipt from scan completion**
   - Once the service durably owns the request and files, immediately acknowledge receipt:
     “Request R-123 received; security scan pending.”
   - Make clear that receipt is not scan approval or final submission acceptance.

4. **Replace timeout with inspectable pending state**
   - A client timeout must not clear or recreate the request.
   - Preserve the title, return location, request ID, upload progress, and file list.
   - Offer:
     - “Check status”
     - “Resume upload,” if bytes remain
     - “Return to previous page,” using the saved return location
   - Status checks are read-only and use the existing request ID.

5. **Make retry reconciliation-first**
   - Before replaying any upload or submission action, query the request by ID.
   - If scanning is pending, continue waiting without duplication.
   - If upload is incomplete, resume only missing chunks.
   - If scanning passed, continue once to final acceptance.
   - If scanning failed, retain unaffected fields and identify the rejected file beside its recovery action.
   - If status cannot be established, do not create a second request; show “Status unknown” and retain recovery ownership with the service.

6. **Define cancellation and handoff**
   - Cancellation explicitly states whether it abandons only the local wait or also withdraws the staged request.
   - A pending request remains recoverable from another session or by support using its request ID, subject to existing authentication and retention rules.
   - Temporary-file expiry must be disclosed before submission; expiry removes staged files but should retain enough request metadata to explain what happened.

## Ownership

- The client preserves editing context and presents progress.
- The upload service owns resumable transfer and deduplication.
- The scanning service owns scan state and reason codes.
- The submission service owns the durable request ID and transition to accepted or rejected.
- Support can locate the request by ID but cannot bypass scanning.

## Verification plan

Verify these paths with the same request identity and no duplicate submission:

- Successful upload, delayed scan, and final acceptance.
- Timeout during upload; title, files, return location, and progress survive.
- Timeout after upload but before acknowledgement; status reconciliation finds the existing request.
- Repeated retry clicks and reconnects produce one request and one final effect.
- Scan rejection preserves unaffected work and provides file-specific recovery.
- Browser interruption, sign-out/reauthentication, cancellation, and cross-session handoff.
- Unknown server outcome never triggers blind replay.
- Retention expiry explains what was lost and what must be reselected.
- Keyboard-only and screen-reader use: status announcements are non-disruptive, focus stays at the failure point, controls have clear names, and progress is not conveyed by color alone.
- Unrelated form and navigation state remain unchanged.

No files were modified. The main remaining uncertainty is whether the existing backend supports durable drafts, resumable uploads, idempotency, and status lookup; those capabilities should be confirmed before implementation.