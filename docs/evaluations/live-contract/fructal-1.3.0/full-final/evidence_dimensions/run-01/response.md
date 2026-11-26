The note supports an operator report of context loss during retries. Whether that loss blocks recovery across the support-to-service handoff remains open.

- **Provided artifact and constraint.** The requester supplied [support-note.txt](/tmp/fructal-eval-evidence_dimensions-01-movj3w_p/fixture/support-note.txt) and separately identified the retry policy requiring failed requests to remain resumable across the handoff.
- **Observed wording.** I read the file. Its full text is “Operators report that retries lose context.”
- **Reported claim.** The note attributes context loss to operators. The requester also describes recovery as blocked, but that detail appears only in the request. Neither outcome was directly observed.
- **Inferred consequence.** If the service needs the reported missing context to resume a failed request, its loss could prevent the service from completing recovery.