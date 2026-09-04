Redesign mode remains the maximum outcome. I inspected [workflow.txt](/tmp/fructal-eval-explicit_redesign_caps_fix-01-jqvhezp6/fixture/workflow.txt); its complete observed state is:

```text
state=blocked
```

The required approval is a provided constraint, but the file exposes no owner, request status, next action, retained context, or recovery path. This turns approval into an indefinite stop.

Replacement motion:

1. Submission enters `pending_approval`, recording the requester, approver, submission context, and timestamp.
2. The approver receives one clear choice: approve or request changes.
3. Approval advances automatically to `ready`.
4. Requested changes move to `needs_revision`, preserve the submitted work, and show the reason plus a direct resubmission path.
5. Cancellation moves to `cancelled`; expiration or delivery failure stays recoverable with a visible retry/escalation action.
6. Every transition records actor, time, decision, and current owner so handoffs remain inspectable.

The approval requirement remains unchanged; only the obstructive motion around it changes. A minimal state representation could be:

```text
state=pending_approval
owner=<approver>
requested_by=<requester>
requested_at=<timestamp>
next_action=approve_or_request_changes
```

Verification should cover approval to `ready`, rejection with retained work and reason, resubmission, cancellation, notification failure/retry, duplicate decisions, and an abandoned request with a visible owner and escalation route. Confirm that unauthorized actors cannot approve and that transition history remains intact.

I did not implement or alter `workflow.txt`: implementation would exceed the explicitly selected Redesign-mode boundary. The material open decision is who owns approval and what escalation or expiry policy applies.