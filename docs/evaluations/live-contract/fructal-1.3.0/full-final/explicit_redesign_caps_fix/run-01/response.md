**Proposed redesign:** Replace `blocked` with `awaiting_approval` on the existing work item. Give the requester a tracking ID and show who owns the decision, what needs approval, and what approval will allow. The required approval still gates the action while the requester can track progress without resubmitting.

[workflow.txt](./workflow.txt) contains only `state=blocked`. Your request identifies approval as the constraint. The file leaves two policy details open: who may approve and which action their decision authorizes.

**Replacement workflow**

1. On submission, preserve the submitted version and the requester’s place, subject to permitted storage. Return the tracking ID. Assign the decision to an authorized approver. If routing fails, show `needs_assignment` and give a designated routing owner the next step.
2. The approver reviews that version and sees the consequence before choosing **Approve**, **Request changes**, or **Decline**. A change request returns the same item to the requester with a reason and a way to revise it. A decline records the reason and closes the request.
3. Approval authorizes only the reviewed version. Record the decision before starting the gated action, and track completion separately. If a response is lost, use the tracking ID to check the outcome before retrying. Give the operator responsible for the action any unresolved outcome to reconcile.
4. While approval is pending, the requester can withdraw the item. Resolve concurrent withdrawal and approval as one ordered transition and show both parties which decision took effect.

**Verification plan:** Trace one item from submission through approval and completion. Confirm that an unauthorized decision or approval for an older version cannot release it. Exercise missing assignment, revision, decline, and simultaneous withdrawal and approval. Interrupt a submission and a release, then retry each and check for one item and one effect. Resume by tracking ID and verify the saved work, position, owner, and next step. Use keyboard-only navigation and a screen reader to check decision controls, status updates, and recovery. Compare an unrelated item before and after each scenario.

The explicit Redesign cap governs the deliverable. The fixture was inspected only. The workflow and checks above are proposals.