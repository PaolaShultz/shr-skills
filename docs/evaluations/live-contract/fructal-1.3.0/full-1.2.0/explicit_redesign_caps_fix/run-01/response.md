[workflow.txt](./workflow.txt) contains only `state=blocked`. Your request establishes that approval is required. The file gives no indication of who should act or how work can resume. Under the explicit Redesign cap, the workflow remains unchanged.

**Proposed workflow**

1. When work reaches the approval step, save its current position and revision. Record `awaiting_approval` with one request ID, the designated approver, and the action awaiting approval. Show the requester who acts next.
2. Let the approver inspect that revision and explicitly approve it or request changes. Approval releases only the reviewed revision and resumes work once from the saved position. A request for changes returns ownership to the requester with the approver’s reason and the saved work.
3. After an interruption, look up the existing request ID before retrying. If the requester withdraws the request or revises the work, close the old request so a late approval cannot release it.

**Verification plan**

- Pause at the gate and reopen the workflow as each actor. Check that the work and position survive, each actor can identify the next owner, and only the designated approver can release the reviewed revision.
- Interrupt an approval response and retry it. Verify that one decision is recorded and work resumes exactly once. Repeat after withdrawal and after revision to verify that stale approval has no effect.
- Request changes, revise, and resubmit using only the keyboard and a screen reader. Check that the reason, status, and next action are accessible and that unrelated work is preserved.

The fixture does not identify the designated approver. Applying the design would require an authoritative source for that assignment. These checks are proposed and unrun.