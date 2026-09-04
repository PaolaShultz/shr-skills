The fixture only establishes the observed outcome `state=blocked`; no implementation details are available. The replacement below therefore treats the four continuity requirements in the request as authoritative and leaves storage durations and security policy as open implementation decisions.

### Replacement submission motion

1. **Create a durable draft immediately**
   - Opening the form creates a server-side `request_id`.
   - Store an allow-listed return route with the draft, not merely in browser history or an arbitrary URL.
   - Autosave the title against that request identity.
   - Stage each selected file immediately and associate it with the same draft. Show upload progress and durable status per file.

2. **Submit by identity, not by form contents**
   - The primary action is **Submit documents**.
   - It sends the existing `request_id` plus an idempotency key; it does not create a new request on every attempt.
   - The server records a durable submission state such as `draft → submitting → accepted` or `needs_attention`.
   - Duplicate calls with the same key return the original result rather than creating duplicate submissions.

3. **Treat a timeout as an unknown result**
   - A client timeout must not reset the form or classify the request as failed.
   - Keep the title, staged-file references, return route, request identity, and current position intact.
   - Show: “We couldn’t confirm the result. Your draft and files are saved.”
   - Automatically check status using `request_id`.

4. **Provide recovery beside the timeout**
   - **Check status** is the primary recovery action while the result is unknown.
   - If the server confirms acceptance, show the receipt for the same request and then offer **Return to …**.
   - If no submission was recorded, change the action to **Retry submission**. Retry uses the same request identity and idempotency key.
   - If a particular file is invalid or staging expired, retain everything else and request replacement of only that file.

5. **Preserve return continuity**
   - Keep the return location attached to the draft through success, timeout, reload, authentication renewal, and retry.
   - Navigate away only after confirmed acceptance or an explicit **Leave draft** action.
   - Leaving should keep the draft unless the actor separately chooses an explicitly destructive **Discard draft** action.

### What remains constrained

- Authentication and authorization must be checked again when submitting or resuming; a saved draft does not grant submission authority.
- File staging needs access controls, encryption, malware scanning, retention limits, and explicit cleanup rules.
- Return locations must be validated internal destinations or opaque route identifiers to prevent unsafe redirects.
- Retrying must not bypass validation or conceal changed policy requirements.
- Privacy or retention policy may require staged files to expire, but expiration should produce a visible deadline and selective recovery—not silent loss.

### Verification plan

Verify these scenarios against both visible UI state and durable server state:

- Successful submission produces one request and returns to the stored location.
- A timeout before, during, and after server acceptance retains the title, file list, return route, and `request_id`.
- Repeated retries create exactly one submission and return the same receipt.
- Reload, browser restart, authentication expiry, and another authorized device can resume the same draft.
- One failed or expired file does not erase the title or unaffected files.
- Back navigation and explicit cancellation preserve the draft; discard requires distinct intent.
- Keyboard and assistive-technology users receive announced upload, timeout, status-check, retry, and success states without losing focus.
- Unauthorized actors cannot recover staged files or infer request contents.
- Unrelated drafts and submissions remain unchanged.

The principal open decisions are staging and draft retention periods, whether cross-device recovery is required, and which return destinations are permitted. This is a design proposal only; no files or system state were modified.