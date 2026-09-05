## Fructal Cap Design — recovery motion

The fixture only exposes `state=blocked`; the detailed implementation is unavailable. The two constraints are therefore treated as provided requirements:

- Mandatory reauthentication must remain.
- Sensitive form contents must never be persisted in browser local storage on shared devices.

### Replacement motion

Use a short-lived, encrypted server-side draft owned by the authenticated account. Keep any changes not yet synchronized only in the current tab’s memory.

1. While authenticated, autosave changed fields to the server and show an accessible status such as “Saved securely 10 seconds ago.” Do not use `localStorage`, `sessionStorage`, IndexedDB, service-worker caches, or URLs for form content.
2. Shortly before predictable expiry, save immediately and announce: “Your session is about to expire. Your saved answers will remain available after you sign in.”
3. When reauthentication is required, freeze editing and open an in-page reauthentication dialog. Preserve the page and its in-memory values; do not navigate away.
4. After successful authentication, reconcile the retained in-memory form with the account’s server draft, preferring newer field revisions. Return focus and scroll position to the field the user was editing.
5. If the tab was closed, refreshed, or moved to another device, retrieve the server draft only after authentication and explicit “Resume form” confirmation.
6. If reauthentication is cancelled or fails, leave the form visibly locked. Offer “Try again” and “Discard this draft.” Discarding requires confirmation and deletes the server draft; authentication itself does not submit the form.
7. On final submission, use an idempotency key so retries cannot create duplicate submissions. Delete the recovery draft only after the server confirms submission.

Server drafts need a documented retention period, encryption, authorization checks, auditability, and deletion behavior. A draft must be account-bound—not recoverable using a bearer identifier stored in the browser. If policy also prohibits server-side drafts, that is an open constraint conflict: only same-tab memory preservation is possible, and recovery after a tab or browser loss cannot be guaranteed.

### Ownership and failure behavior

- Browser tab: temporary unsaved edits, focus, scroll position; cleared when the tab closes.
- Draft service: last confirmed saved revision and expiry time.
- Authentication service: identity renewal only; it neither submits nor discards data.
- Form service: field reconciliation and idempotent final submission.
- User: explicitly chooses whether to resume or discard a recovered draft.

Offline or failed autosave must be announced beside the save status: “Not saved—keep this tab open,” with a retry control. A timeout must not trigger blind replay; first query the draft or submission status to prevent duplicate effects.

### Verification plan

Verify that:

- Expiry after a successful autosave restores every field, focus, scroll position, and validation state.
- Edits made immediately before expiry survive same-tab reauthentication from memory.
- Refresh, tab closure, and another-device sign-in recover only the last server-confirmed revision.
- Failed, cancelled, interrupted, and repeatedly attempted authentication never submits or discards the form.
- Offline autosave clearly identifies which revision is safe and recovers when connectivity returns.
- Back, refresh, multiple tabs, and submission retries do not duplicate drafts or submissions.
- Sign-out and confirmed discard make the draft inaccessible according to retention policy.
- Browser inspection finds no sensitive values in local/session storage, IndexedDB, caches, history, URLs, logs, analytics, or error telemetry.
- Keyboard-only and screen-reader users receive expiry/save/error announcements, remain trapped correctly within the dialog, and return to the originating field after success.

This preserves mandatory reauthentication and the shared-device storage prohibition while making reauthentication a temporary checkpoint rather than a destructive restart. No files were changed.