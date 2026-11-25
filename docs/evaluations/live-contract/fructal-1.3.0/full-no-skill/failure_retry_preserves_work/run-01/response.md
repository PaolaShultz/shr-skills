**Proposed motion.** I move that the system acknowledge receipt as soon as it has safely stored the title, selected files, return location, and request ID. The acknowledgement should show “Received — scan pending.” Submission should remain blocked until every required scan passes.

If the acknowledgement times out, the form should retain all four items. Retry should use the same request ID to check for a receipt. If one exists, show it and the current scan status. Otherwise, resume the same request using the retained files. A retry must produce at most one submission, require no re-entry or file reselection, and preserve the original return location.

No system changes were made.