Review mode.

- **Artifact:** `support-note.txt` is a **provided artifact**—requester-supplied evidence.
- **Attributed claim:** “Operators report that retries lose context” is a **reported claim**, not verified evidence of actual retry behavior.
- **Direct inspection:** I **observed** that the file contains exactly that sentence. This verifies only the document’s contents and attribution.
- **Not established:** The note does not state that “recovery is blocked,” nor does it provide logs, cases, workflow traces, or service-state evidence confirming context loss.
- **Material friction, if confirmed:** Retry context loss would obstruct the required resumable support-to-service handoff, with potentially high recovery cost.

The retry policy is a requester-provided necessary constraint. Whether the implementation violates it remains an open question requiring direct workflow or operational evidence. No files were modified.