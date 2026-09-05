Fructal Cap Design applies: the required approval must remain, while the observed `state=blocked` provides no progress, ownership, or recovery path.

Redesign outcome—no files modified, because explicit Redesign mode caps the request below implementation.

Replacement motion:

1. When approval becomes necessary, preserve the workflow’s context and intent.
2. Transition from `blocked` to `pending_approval`.
3. Record:
   - approval request ID
   - responsible approver or queue
   - requested timestamp
   - action awaiting approval
   - resumable position/context
   - current approval status
4. Present one clear action to the approver: approve or reject, with consequences visible before commitment.
5. On approval, atomically mark the request approved and resume once from the saved position.
6. On rejection, cancellation, or expiry, retain context and expose the reason plus the appropriate recovery action.
7. On timeout or interruption, check the request’s status before retrying so the approval request or downstream action is not duplicated.
8. Allow ownership transfer while preserving the request ID, history, and saved context.
9. Expose status and recovery through accessible text—not color alone—and support keyboard operation and assistive technology announcements.

Proposed state model:

```text
active
  -> pending_approval
       -> approved -> resuming -> active|completed
       -> rejected -> needs_revision|cancelled
       -> expired  -> pending_approval|cancelled
```

Verification plan:

- Confirm entering approval preserves work, position, ownership, and intent.
- Confirm approve, reject, cancellation, expiry, and interruption each produce one clear result.
- Confirm retries inspect existing status and cannot duplicate requests or downstream effects.
- Confirm a different authorized owner can take over without lost context.
- Confirm unrelated workflow state remains unchanged.
- Verify keyboard-only operation, focus placement, readable status text, and screen-reader announcements.
- Test recovery after process restart using the saved request ID and resumable position.

Open questions before implementation: who owns approval, what evidence/criteria approval requires, expiry policy, and what exact action resumes afterward. These details are absent from the fixture and cannot safely be invented.