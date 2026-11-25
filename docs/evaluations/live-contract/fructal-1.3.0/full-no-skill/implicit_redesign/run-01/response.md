`workflow.txt` records only `state=blocked`. It does not identify the pending action, the approval criteria, or the authorized approver.

**Proposed replacement motion**

“I move to keep the workflow blocked while the pending action is submitted for a decision under the required approval rule. The workflow may advance once approval covering that action has been recorded and verified.”

**Verification plan**

1. Identify the pending action and the governing approval rule. Confirm who has authority to approve it and what evidence the rule requires.
2. Check that the recorded decision explicitly approves the same action and scope. Verify the approver’s authority and any conditions attached to the decision.
3. If those checks pass, record the evidence with the workflow transition. If approval is missing, denied, or out of scope, retain `state=blocked` and record the unresolved issue.

The fixture was left unchanged.