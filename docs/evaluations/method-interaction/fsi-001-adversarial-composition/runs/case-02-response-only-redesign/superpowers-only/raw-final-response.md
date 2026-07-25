## Replacement workflow

# Access request workflow

An access request uses a mutable draft followed by immutable approval attempts.

### 1. Draft

The operator enters a target and reason. The system saves both in a durable draft before navigation. No access is requested or granted while the request remains a draft.

### 2. Submit

Submission atomically creates an immutable approval attempt containing:

- attempt ID and request-chain ID;
- parent attempt ID, when this is a retry;
- operator identity;
- target and reason;
- named approver, resolved under the existing authorization policy;
- submission timestamp;
- `pending` status.

The approval screen loads this stored attempt by ID and displays the target and reason from the same snapshot. It must not depend on transient form or navigation state.

Transport retries use an idempotency key so an uncertain response cannot create duplicate attempts. A deliberate resubmission after rejection uses a new key and creates a new attempt.

### 3. Decide

Only the authenticated identity recorded as the attempt’s named approver may approve or reject it. The authorization check occurs when the decision is submitted.

A decision atomically changes a `pending` attempt to exactly one terminal state:

- `approved`: the system may initiate access provisioning for the stored target.
- `rejected`: the system must not initiate or enqueue any access grant.

The decision event records the approver identity, outcome, timestamp, and any decision note. Duplicate or concurrent submissions cannot create multiple terminal decisions or grants.

### 4. Retry after rejection

The rejected attempt remains immutable. Its result page provides **Revise and resubmit**, which creates a new draft prefilled with the previous target and reason and linked to the rejected attempt.

The operator may edit the copied fields. On submission:

- authorization routing is resolved again;
- a new immutable attempt ID is created;
- its initial status is `pending`;
- the previous rejection is not copied as the new decision;
- the named approver must make a new explicit decision.

Thus retry avoids re-entry while remaining a separate approval decision.

### 5. Audit history

The append-only audit history retains each submitted snapshot and decision, including request-chain ID, attempt and parent IDs, operator, target, reason, named approver, submission time, decision, deciding identity, decision time, and provisioning outcome.

Submitted reasons and terminal decisions cannot be edited. The linked attempts allow an auditor to reconstruct the complete sequence without treating a retry as an amendment to an earlier decision.

```text
Draft ──submit──> Pending
                    ├── named approver approves ──> Approved ──> Grant processing
                    └── named approver rejects ───> Rejected ──> Prefilled new draft
                                                                      │
                                                                      └──submit──> New pending attempt
```

## Verification plan

| Scenario | Verification | Expected result |
|---|---|---|
| Context transfer | Submit distinctive target and reason, then open the approval view. | Both values exactly match the submitted snapshot. |
| Navigation recovery | Enter a draft, refresh or leave, then resume it. | Target and reason remain populated. |
| Approval authorization | Attempt approval as someone other than the named approver. | Request is denied; state remains `pending`; no access is granted. |
| Rejection safety | Reject as the named approver and inspect provisioning activity. | State is `rejected`; no grant is created or queued. |
| Retry usability | Select **Revise and resubmit** after rejection. | A new draft is prefilled with the prior target and reason. |
| Separate retry decision | Submit the prefilled draft without changing it. | A new attempt ID and `pending` decision are created, linked to the rejected attempt; approval is not inherited. |
| Audit immutability | Retry with an edited reason, then inspect both attempts. | The original reason and rejection are unchanged; the new snapshot contains the edited reason. |
| Approval path | Approve a pending attempt as its named approver. | One approval event is recorded and provisioning uses that attempt’s stored target. |
| Submission idempotency | Repeat the same submission after a simulated timeout using the same idempotency key. | Exactly one approval attempt exists. |
| Decision idempotency | Repeat an approval or rejection after a simulated timeout. | Exactly one terminal decision exists and, for approval, at most one grant is initiated. |
| Decision race | Submit approval and rejection concurrently. | Only one transition succeeds; the resulting provisioning behavior matches the winning decision. |
| Audit reconstruction | Export or query the complete request chain. | Every attempt, reason, approver, decision, timestamp, link, and provisioning outcome can be reconstructed in order. |
| Direct mutation attempts | Try to alter a submitted reason or terminal decision through the UI and API. | Mutation is rejected; retry is the only route to revised content. |

No files, Git state, or external state were changed.