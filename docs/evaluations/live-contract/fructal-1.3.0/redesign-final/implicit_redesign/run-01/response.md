Give the blocked request a named approval owner and a visible next step. Keep the protected action on hold until an authorized approver approves the exact request.

The approval requirement comes from your description. [workflow.txt](./workflow.txt) contains only `state=blocked`. It doesn’t identify the protected action, the approver, or whether an approval request has already been sent. The cause of this particular stall is therefore uncertain.

**Proposed motion**

1. Before asking the requester to submit, show what they are asking someone to approve and what approval will allow. On submission, preserve the submitted version and give both parties one request ID. The requester sees “Awaiting approval,” who owns the decision, and where to check its status.
2. The approver opens that same request and can approve, decline, or return it for changes. Approval releases only the reviewed version. A return preserves the entered work, shows the reason beside the relevant input, and assigns the next step to the requester. A decline closes the request with a visible reason.
3. If routing fails or the approver is unavailable, keep the gate closed and assign recovery to a designated routing owner who can locate an authorized approver. For the existing blocked item, that owner first checks for an outstanding request, a recorded decision, or an action already taken. If the outcome is uncertain, reconcile it under the same ID before retrying. After an interruption, either party can reopen the record at the current step.

Before adoption, confirm who may approve or reroute, which action approval permits, what request data may be retained, and when withdrawal takes effect. Those details aren’t recorded in the fixture.

**Verification plan**

- Submit once, double-submit, and retry after a timeout. Verify one request ID, one reviewable version, and no protected effect before approval. Interrupt execution after approval and verify recovery produces exactly one effect.
- Try an unauthorized approval and approval of an older version after revision. Both must leave the current version gated. Return a request for changes, reopen it, and check that the requester has the saved inputs, reason, and next step. Verify a decline produces no protected effect.
- Simulate failed delivery and an unavailable approver. Verify the routing owner can find and reassign the same record, and the requester sees who owns it. Race withdrawal against approval and check that both parties see one outcome consistent with the agreed withdrawal rule.
- Complete submission, review, and recovery by keyboard and with a screen reader. Check focus after a return, announced status changes, and access to the reason and next action. Compare unrelated requests, drafts, and permissions before and after each scenario.

These are proposed checks. I inspected the fixture locally without modifying it or contacting external services.