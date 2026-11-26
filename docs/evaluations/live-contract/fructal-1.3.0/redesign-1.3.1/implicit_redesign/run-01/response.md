**Proposed handoff.** Keep the approval requirement and give the blocked work a durable request ID, a current owner, and a visible next action. You identified approval as the blocker. [workflow.txt](./workflow.txt) records only `state=blocked`, so it cannot tell an operator whose decision is pending or whether a decision has already been made.

1. **On submission**, preserve the work and its resume position within permitted storage. Record the version submitted, show the effect being requested, and route the request to an authorized approver. The requester sees “Awaiting approval,” the owner, and the request ID. If routing fails, keep the work pending and give a designated routing owner the action to assign it.
2. **At review**, show the approver the submitted version and the effect their decision authorizes. A request for changes returns ownership to the requester with a reason and a link back to the preserved work. Resubmission creates a new review version under the same ID. Denial closes the request with a visible reason. Withdrawal while pending invalidates that version’s pending decision.
3. **After approval**, allow only the approved version to proceed, and retain any separate commitment the requester must make. Give the executing service ownership until it records the outcome. After an interruption or timeout, look up the effect by request ID and version before retrying. If the outcome is uncertain, show “Checking outcome” and assign reconciliation to an operator.

**Open policy details.** Confirm the protected effect, who may approve it, who owns routing failures and reconciliation, and what work may be retained. These determine the permission checks, recovery assignments, and storage for the proposed handoff.

**Verification plan**

- Submit, interrupt the session, and reopen the request as both requester and approver. Check that each sees the same ID, version, owner, and next action, and that the requester can recover their permitted work and position.
- Try an unauthorized approval, request changes, edit, and submit a stale approval. Verify that each leaves the effect gated. Approve the current version and verify one intended effect after any required requester commitment.
- Exercise denial, routing failure, and withdrawal racing with approval. Verify a single recorded outcome for the race, a named recovery owner for failed routing, and consistent status for both people.
- Interrupt execution after the effect occurs but before acknowledgment. Retry and verify one effect. Simulate an unavailable status lookup and verify that reconciliation stays assigned without a replay.
- Use a keyboard and screen reader to locate the owner, hear status changes, review consequences, and recover focus after a return for edits. Compare an unrelated request before and after to confirm its content, ownership, and status are intact.

The fixture was inspected read-only. These are proposed checks for the replacement workflow.