**Proposed redesign.** Replace `blocked` with `awaiting approval` and show who owns the next step. Keep the protected action on hold until an authorized approver approves the exact request under review.

The approval requirement and its role in the blockage come from your report. [workflow.txt](./workflow.txt) contains only `state=blocked`. It gives someone returning to the workflow no way to tell who should act or how to resume. The fixture leaves the approver, the protected action, and the permitted storage for pending work unspecified.

**Replacement motion**

1. Before submission, show the requester what approval would authorize. On submission, give the request a stable ID, preserve its version and permitted context, and show both parties the same status, current approver, and next action. Reopening or retrying submission returns to that request.
2. The approver can approve the displayed version or return it with a reason. Returning it gives ownership back to the requester, who can revise and resubmit under the same ID. A revision requires a fresh decision. While approval is pending, the requester can withdraw it. If approval and withdrawal coincide, record one transition and show both parties which took effect.
3. After approval, the workflow takes ownership of the protected action and records its outcome against the approved version. If interrupted, look up the outcome before retrying. If it remains unknown, show “Outcome unconfirmed,” assign a recovery owner, and hold replay until that owner can establish what happened.

**Verification plan.** With a requester and an authorized approver, submit, interrupt the session, and reopen from each side. Check that the ID, permitted work, review position, owner, and next action survive. Exercise return, revision, withdrawal, and a stale or unauthorized approval attempt. Verify that only a current authorized approval releases the action, and that duplicate submissions and a lost completion response produce at most one effect. Repeat the handoff using a keyboard and screen reader, checking focus and status announcements. Compare an unrelated request before and after for unintended changes.

The fixture was left unchanged. These are proposed acceptance checks for a future implementation.