Replace `state=blocked` with **Awaiting approval**, and show who has the request and what they need to decide. Your request establishes that approval is required. [workflow.txt](./workflow.txt) contains only `state=blocked`, so someone returning to the file cannot tell whether a request was submitted, who owns it, or how to resume.

**Proposed handoff**

1. When the requester reaches the approval gate, show the action that approval would permit. On submission, preserve the work and its resume point. Give the requester and designated approver the same request ID, tied to the submitted version. If submission is interrupted, look up that ID before retrying.
2. While approval is pending, show the approver as the next actor. If routing fails, keep the request open, show the delivery failure, and give the requester a way to retry routing with the same ID. A rejection returns the work to the requester with the reason and a revision path. Withdrawal closes the request and preserves the draft. A late decision on a withdrawn or superseded version has no effect.
3. Approval makes that version ready to resume. Return the requester to the saved position with a **Continue** action that names the protected effect. If completion is interrupted, check the recorded outcome before offering a retry so continuing twice produces one effect.

The fixture does not identify the protected action, the authorized approver, or the storage permitted for saved work. Confirm those details before implementation.

**Verification plan.** Walk one request from submission through approval and completion. Verify that the protected action requires approval for the exact version, the requester resumes at the saved position, and repeated submission or continuation produces one request and one effect. Repeat with routing failure, rejection, revision, withdrawal, a late approval, and interruption during completion. At each handoff, check that both actors can identify the status, owner, and next action, including by keyboard and screen reader wherever an interface presents them.

The explicit Redesign cap governs the deliverable. No file was modified, and the verification plan has not been run.