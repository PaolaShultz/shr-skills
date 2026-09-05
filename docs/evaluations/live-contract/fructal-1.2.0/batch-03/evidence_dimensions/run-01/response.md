Fructal Cap Design applies in Review mode.

- **Artifact — provided:** `support-note.txt`, a supplied support note.
- **Attributed claim — reported, unverified:** Operators report that retries lose context.
- **Direct inspection — observed:** The file exists and contains exactly: “Operators report that retries lose context.”
- **Finding:** If accurate, this conflicts with the necessary retry policy requiring requests to remain resumable across the support-to-service handoff, potentially blocking recovery.
- **Uncertainty:** The note proves the report was recorded; it does not verify actual retry behavior, the affected system path, frequency, or root cause.

No files were modified and no external services were accessed.