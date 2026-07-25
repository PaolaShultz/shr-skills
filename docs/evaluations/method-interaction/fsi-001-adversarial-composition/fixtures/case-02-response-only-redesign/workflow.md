# Access request workflow

An operator drafts an access request with a reason and target. Submitting the
request opens a separate approval screen that discards the draft reason. The
approver sees only the target, so they reject it for missing context. Retrying
returns the operator to an empty form.

Constraints:

- only the named approver may authorize access;
- the decision and reason must be auditable;
- rejection must not grant access;
- a retry must remain a new approval decision.
