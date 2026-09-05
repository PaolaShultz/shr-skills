Fructal Cap Design applies: required approval is the necessary constraint; hiding the record ID obstructs completion and recovery.

The local evidence is limited to [workflow.txt](/tmp/fructal-eval-related_review_recommendations-01-nkbhbe7m/fixture/workflow.txt:1), which confirms `state=blocked`. The two ID defects are provided findings rather than independently observable in this fixture.

- **P1 — Approval status lacks the record ID.** Approvers cannot reliably identify the blocked record, creating lookup effort and misapproval risk. Recommend displaying the canonical record ID in the status message with an accessible copy action. Keep it visible wherever the blocked status appears.

- **P1 — Support view conceals the same ID.** Support cannot correlate the report with the underlying record, delaying diagnosis and handoff. Recommend exposing the canonical ID as selectable text in the relevant support view, subject to existing authorization and redaction rules.

- **Related consistency recommendation.** Use the same label, value, and accessible representation in both surfaces, backed by the authoritative identifier rather than separately formatted substitutes. Add focused checks that blocked approval messages and authorized support views expose matching IDs, including keyboard and screen-reader access.

No files were changed, consistent with Review mode.