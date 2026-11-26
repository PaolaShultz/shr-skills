Move the approval gate to the point where the protected action would take effect. Keep the request available while approval is pending, so the requester can see who owns the next step and resume the same request after a delay.

The required approval comes from your description. The fixture records only `state=blocked`. It does not identify the protected action, who can approve it, or whether the block reflects a missing decision or a decision that failed to reach the workflow. [workflow.txt](/tmp/fructal-eval-implicit_redesign-01-mj0ueu_6/fixture/workflow.txt:1)

**Proposed motion**

1. On submission, show what approval would authorize. Record the request once under a stable ID, preserve its submitted version within permitted storage, and show “Awaiting approval,” the responsible approver or queue, and the next step. If routing fails, show “Needs assignment” and give a designated workflow owner responsibility for recovery.
2. Give the authorized approver the same ID and submitted version. Approval releases only the action covered by that decision. If the requester must separately confirm execution, return them to that choice. A request for changes returns ownership to the requester with the reason and their prior work available. A material edit requires approval of the revised version.
3. After interruption, reopen the same request. If a decision or execution times out, check its recorded status before retrying. If the outcome is still unknown, show who will reconcile it and keep replay blocked. If cancellation is permitted while pending, record it on the request and prevent a late approval from releasing the action.

**Verification plan**

- Submit once, interrupt the handoff, and reopen as requester and approver. Check that both see the same ID, version, status, and next owner. Simulate failed routing and confirm the workflow owner can recover the existing request.
- Attempt execution while pending, after rejection, and with approval for an older version. Each must leave the protected action unexecuted. Approve the current version and verify one intended effect after any required confirmation.
- Drop an acknowledgment after a successful decision or execution, then retry. Verify that the recorded outcome is recovered without duplicating the effect. Race cancellation against approval and check that both actors see one authoritative outcome.
- Complete the handoff by keyboard and with a screen reader. Check that status, reasons, and recovery actions are accessible and that focus returns to the relevant request. Compare unrelated requests and saved work before and after each scenario.

Before implementation, confirm the protected action, approval authority, recovery owner, and whether approval itself authorizes execution. The fixture was left untouched. These checks are proposed and have not been run.