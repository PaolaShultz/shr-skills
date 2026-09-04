Review mode.

`workflow.txt` contains only:

```text
state=blocked
```

Finding: the required approval is not the problem; the workflow’s state lacks the approval status, owner, request reference, and recovery action. There is no evidence that approval was requested, granted, or denied, so changing the state would risk bypassing the constraint.

Recommended bounded correction: record the workflow as `pending_approval` only after confirming the authoritative approval request and owner. If approval was already granted, update the state from that evidence.

No file was modified because Review mode prohibits system changes. The unresolved decision is the actual approval status and its source of truth.