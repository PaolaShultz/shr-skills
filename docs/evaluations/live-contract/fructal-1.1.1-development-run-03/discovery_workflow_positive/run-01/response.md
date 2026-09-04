The dashboard should become the source of truth; email remains a finance notification channel, not the approval record.

### Proposed flow

1. Customer submits once.
2. The dashboard immediately creates a refund request with:
   - A stable request ID
   - Status: `Awaiting finance approval`
   - Named owner: finance queue or assigned approver
   - Submission timestamp and audit history
3. Finance receives an email containing a link to the request. Approval or rejection happens in the dashboard and records the actor, time, and reason.
4. After approval, processing runs exactly once and transitions through:
   - `Approved — processing`
   - `Refunded`
   - `Failed — action required`
5. The customer and support see the same current status. Support can see the owner, age, last action, and escalation route.

### Safe retry behavior

Generate an idempotency key from the customer submission and retain it across client or server retries. If a timeout occurs:

- Retry performs a lookup/create using the same key.
- If the request already exists, return that request instead of creating another.
- Show: “Request received; checking its status.”
- Disable a fresh submission while the outcome is uncertain.
- Provide “View existing request,” not another submit action.

Processing should also use the request ID as an idempotency key with the payment provider, preventing duplicate refunds even if a worker retries.

### Ownership and recovery

Every nonterminal request must have one visible owner:

- `Awaiting finance approval` → finance queue or named approver
- `Approved — processing` → refund-processing service
- `Failed — action required` → operations/support queue
- `Refunded` or `Rejected` → no active owner; history remains visible

Add an approval deadline and escalation path so requests cannot sit ownerless. Reassignment must be recorded in the audit trail.

### Preserve these constraints

Finance approval remains mandatory, customers cannot approve their own requests, and every consequential action stays attributable. Email notifications may continue, but replies should not alter state.

### Verification before rollout

Test normal approval, rejection, simultaneous submissions, browser and API timeouts, repeated retries, worker restarts, duplicate provider callbacks, finance-email delays, reassignment, and overdue escalation. Confirm that each scenario produces one request, at most one refund, a visible owner, and a complete audit trail.

The fixture only states `state=blocked`, so this is a proposed redesign based on the reported workflow—not a validated description of the current implementation. Nothing was modified.