Fructal Cap Design applies.

High-priority finding: the required approval must remain, but the report says its record ID is lost during the support handoff. That prevents support from locating or verifying the approval, stalling completion and weakening recovery/ownership.

Evidence and limits:

- Provided constraint: approval is required.
- Reported issue: “the approval record ID is lost during handoff.”
- Unverified: the file does not establish where the ID is dropped, how often this occurs, or whether the approval record itself survives.

Recommendation: preserve and expose the approval record ID in the handoff context, with an inspectable fallback for support when propagation fails. Verify preservation across normal handoff, interruption, and retry paths.

No files were changed. One authorized prepaid read was used; nine remain.