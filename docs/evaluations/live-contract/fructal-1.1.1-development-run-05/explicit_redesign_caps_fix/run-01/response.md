Redesign mode.

`workflow.txt` remains unchanged because Redesign is the explicit maximum outcome; implementation was therefore not permitted.

Observed current motion:

```text
state=blocked
```

The required approval is a valid authorization constraint, but the single `blocked` state hides the pending action, owner, and recovery path.

Proposed replacement motion:

1. A request enters `awaiting_approval`, preserving its requester, context, and intended continuation.
2. The designated approver receives one clear choice: `approve` or `reject`, with the consequence visible before commitment.
3. Approval moves the request automatically to `ready`, allowing the original actor to continue without resubmission.
4. Rejection moves it to `changes_requested`, retaining the original work and recording actionable feedback.
5. If approval stalls, the request remains inspectable and offers an explicit reminder or escalation path without bypassing approval.
6. Duplicate decisions are idempotent; cancellation remains available to the requester and does not masquerade as rejection.

Suggested state representation:

```text
state=awaiting_approval
requester=<actor>
approver=<actor>
requested_action=<action>
submitted_at=<timestamp>
decision=
decision_reason=
next_action=await_approver
```

Transitions:

```text
awaiting_approval + approve -> ready
awaiting_approval + reject  -> changes_requested
awaiting_approval + cancel  -> cancelled
changes_requested + resubmit -> awaiting_approval
ready + continue -> completed
```

The approval requirement, decision ownership, auditability, and explicit consent remain unchanged. The redesign removes the ownerless `blocked` state and preserves context through rejection, retry, delay, and handoff.

Verification should cover:

- Approval advances exactly once and preserves the submitted work.
- Rejection retains work and exposes feedback beside the retry action.
- Delayed approval clearly identifies the current owner and escalation route.
- Repeated or stale decisions do not corrupt state.
- Cancellation cannot be mistaken for approval or rejection.
- Each state and action is available through keyboard and assistive technology where a human interface exists.
- Unrelated workflow data remains untouched.

The existing artifact’s SHA-256 remains `8ec4c039b66c98d4e1fe599c4669f86150977fce3408e9e3c479b00362f9e248`. Implementation and runtime validation remain outstanding.