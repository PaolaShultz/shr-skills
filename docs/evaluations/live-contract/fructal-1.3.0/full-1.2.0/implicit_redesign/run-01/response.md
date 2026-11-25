**Make approval a recoverable pause.** You identified approval as mandatory. The only recorded state is `state=blocked`, which leaves the next actor unable to tell whether approval needs to be requested, is pending, or has already been decided. The fixture does not identify the approver or establish which of those situations applies. [workflow.txt](/tmp/fructal-eval-implicit_redesign-01-c_knbnyx/fixture/workflow.txt:1)

**Proposed motion**

1. At the approval gate, pause the protected action and save the work, its version, and the requester’s place. Show what needs approval, who can decide, and what will happen after approval. Let the requester submit or leave and return.
2. Record one approval request for that version. While it is pending, show the requester who owns the next step and give the authorized approver the saved version to review. For the existing blocked item, check for a prior request or decision first. If its status is uncertain, give the workflow owner a reconciliation task before retrying.
3. On approval, return the requester to the saved step with a **Continue** action that completes the protected operation once. On rejection, show the reason beside the saved work so the requester can revise it. Withdrawal closes the request and preserves the draft. A change to approval-relevant content requires approval of the revised version.

**Verification plan**

- Pause midway through entered work, leave, and return as both requester and approver. Check that the work, position, version, and next owner survive handoff.
- Try to continue while approval is pending, rejected, withdrawn, or attached to an older version. Each attempt should leave the protected action pending. Approve the current version, select **Continue** twice, and verify one completion.
- Interrupt submission and completion after sending but before acknowledgment. Reopen the item and check its recorded outcome before retrying. Test the existing blocked item with a prior request, with no prior request, and with an indeterminate result. Verify that recovery creates no duplicate request or effect.
- Complete approval, rejection, revision, and withdrawal using a keyboard and screen reader. Check that status changes are announced, the next actor and action are clear, and focus returns to the saved step.

The fixture was read only. These checks are proposed and have not been run.