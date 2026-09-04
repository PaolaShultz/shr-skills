Implement mode — capped at Redesign by the no-modification boundary.

The fixture contains only `state=blocked`. The required approval and its operational details are requester-provided; no approver, ownership, timeout, or recovery behavior is documented. No files were modified.

Replacement motion:

1. Preserve submitted work and record a resumable checkpoint.
2. Replace generic `blocked` with `awaiting_approval`, showing the request, responsible approver, submission time, and current status.
3. Notify the approver while letting the requester leave and return without losing context.
4. Provide clear outcomes:
   - **Approved:** automatically resume from the checkpoint.
   - **Changes requested:** return to the requester with feedback and retained work; resubmission creates a new review revision.
   - **Cancelled:** close the request without discarding its history.
   - **Delayed:** remind or escalate to a defined backup owner; never bypass approval.
5. Make status and ownership inspectable to both parties, with accessible notifications and one source of truth.

This preserves the approval constraint while removing the ownerless dead end. The key unresolved decisions are who may approve, who receives escalation, and what delay triggers it.

Verification should cover approval and automatic continuation, rejection and resubmission, cancellation, timeout escalation without constraint bypass, interruption and return with retained work, duplicate decisions being idempotent, and consistent accessible status for requester and approver. This is a design proposal only; it was not implemented or validated.