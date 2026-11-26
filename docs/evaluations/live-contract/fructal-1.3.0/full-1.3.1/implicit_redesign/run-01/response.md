Give the blocked request one durable approval record. The requester can leave and return to it, the approver can see what needs a decision, and the workflow can resume from that decision. **The protected action must wait for approval.**

The approval requirement comes from your request. The only observed content of `workflow.txt` is `state=blocked`. It identifies neither the protected action nor the approver, and it gives the requester no way to tell who acts next. The file alone cannot establish whether an approval request was delivered.

### Proposed motion

1. When the workflow reaches the gate, save its position and the work it may retain. Create or reuse an approval record keyed to this request and the version being approved. Show the requester “Awaiting approval,” the proposed effect, the current owner, and the record ID.
2. Put that same record in the authorized approver’s queue. If routing fails or no approver is assigned, retain the request and give a designated routing owner a task to resolve the assignment. The requester can check progress without resubmitting.
3. Record the approver’s decision against the reviewed version. Approval releases that version for execution once. A request for changes returns the requester to the saved work with the reason. A denial closes the gate with a visible outcome. If the requester withdraws while approval is pending, close the record and reject any late decision.
4. After an interruption, reopen the same record. If execution started but its outcome is unknown, assign reconciliation to the workflow operator and check the downstream status before any retry. Display the confirmed result on the record.

Before implementation, the process owner needs to identify the protected effect, who may approve it, who handles routing and execution exceptions, and which work may be retained. Those details are absent from the fixture.

### Verification plan

| Scenario | Concrete check |
|---|---|
| Approval and handoff | Submit once and reopen as each actor. Verify the same ID, saved position, owner, and next step. Confirm zero protected effects before approval, including after an unauthorized decision attempt, and exactly one after valid approval. |
| Routing failure and interruption | Interrupt delivery and restart the workflow. Verify the routing owner can recover the original request and the approver receives one actionable item. |
| Changes, denial, and withdrawal | Verify reasons reach the requester, edits require approval of the revised version, and denial prevents execution. Race withdrawal against approval and verify one recorded outcome consistent with the order accepted. |
| Retry after an unknown outcome | Drop the execution acknowledgement after the effect occurs. Verify recovery checks status and records completion without repeating the effect. |
| Accessibility and isolation | Complete review and recovery by keyboard and with a screen reader. Check focus, announced status, and access to reasons. Compare an unrelated request before and after for unchanged content, ownership, and state. |

These are proposed checks. The fixture was read only and remains unchanged.