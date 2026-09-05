Fructal Cap Design applies: the provided retry policy must preserve resumability across handoff, while reported context loss would obstruct recovery.

- **Artifact — provided:** `support-note.txt`, supplied by the requester.
- **Attributed claim — reported, unverified:** “Operators report that retries lose context.”
- **Direct inspection — observed:** The file contains exactly that sentence. It does not mention blocked recovery, identify the affected requests or handoff stage, or provide evidence that the retry policy is violated.
- **Open question:** The requester’s statement that “recovery is blocked” is not supported by the inspected document and remains unverified.

Priority finding: reported context loss merits investigation because it could break required resumability, but this artifact alone does not establish the cause, frequency, recovery impact, or actual policy noncompliance. No changes were made in Review mode.