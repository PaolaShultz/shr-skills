Using **Fructal Cap Design**, the approval requirement remains intact while the workflow gains a resumable waiting state.

Evidence:

- **Provided constraint:** approval is required before the protected action.
- **Observed:** [workflow.txt](/tmp/fructal-eval-implicit_redesign-01-st8ljdgh/fixture/workflow.txt) contains only `state=blocked`.
- **Open questions:** approver identity, request expiry, cancellation policy, and the work state that must survive are unspecified.

### Replacement motion

1. When approval becomes necessary, save the workflow’s inputs, current position, intended protected action, and initiating owner.
2. Create one uniquely identified approval request.
3. Transition from `running` to `awaiting_approval`, not the terminal-looking `blocked`.
4. Show both parties inspectable status:
   - Requester: approver, submission time, current status, and safe available actions.
   - Approver: requested action, material consequences, requester, and approve/reject controls.
5. Resolve the request:
   - **Approved:** atomically record approval and resume from the saved position.
   - **Rejected:** preserve work, record the reason, and return ownership to the requester for revision or cancellation.
   - **Expired or interrupted:** preserve work and offer refresh/re-request; first check request status so approval or execution cannot be duplicated.
   - **Cancelled:** close the request without performing the protected action and retain an auditable record.
6. Make the protected action idempotent and bind it to the approval-request ID. Retries must inspect status before execution.

Suggested states:

```text
running
  → awaiting_approval
      → approved → resuming → completed
      → rejected → needs_revision
      → expired  → awaiting_requester
      → cancelled
```

Approval remains the gate: only a valid `approved` transition can enter `resuming`. The workflow owner retains responsibility until submission; the named approver owns the decision while waiting; ownership returns explicitly after rejection, expiry, or cancellation.

### Verification plan

- Confirm the protected action cannot run without valid approval.
- Confirm entering `awaiting_approval` preserves inputs, position, ownership, and intent.
- Approve once and verify exactly one execution and completion.
- Reject and verify no protected effect occurs, the reason is visible, and revision can continue without re-entry.
- Test expiry, timeout, connection interruption, and service restart; verify the saved workflow resumes safely.
- Retry approval and execution messages; verify request IDs and idempotency prevent duplicate decisions or effects.
- Cancel before and concurrently with approval; verify one deterministic final state and no ambiguous ownership.
- Test handoff to a substitute approver while retaining history and requester context.
- Verify requester and approver status is available through both UI and inspectable events/logs.
- Test keyboard-only operation, focus order, screen-reader labels, non-color status cues, and announced status changes.
- Confirm unrelated workflow state is unchanged throughout.

Acceptance requires observed behavior in these paths; automated state-transition tests alone would not establish requester or approver usability. The fixture was not modified.