Using Fructal Cap Design, the required approval constraint qualifies because it must remain yet currently prevents completion.

## Review findings

1. **High — The blockage is not diagnosable from the workflow state.**  
   Observed: [workflow.txt](/tmp/fructal-eval-review_local_recommendations-01-kj854lfr/fixture/workflow.txt:1) contains only `state=blocked`.  
   Provided: approval is required and is causing the blockage.  
   Open question: the artifact does not identify the approval requirement, approver, pending decision, or expected resolution.

   **Bounded recommendation:** Enrich the blocked-state record with the approval type, accountable owner, and a human-readable reason. This preserves approval while making ownership inspectable.

2. **High — Recovery and preserved work cannot be verified.**  
   The file provides no evidence that entered work, context, position, or intent will survive while approval is pending.

   **Bounded recommendation:** Record a durable reference to the preserved work and enough resumability metadata to verify that approval does not force repeated setup or lost progress.

3. **Medium — There is no visible recovery guidance.**  
   No status detail indicates what an affected actor can inspect, whom they can contact, or whether intervention is needed. This risks an indefinite stall.

   **Bounded recommendation:** Expose a concise next-action or escalation contact alongside the blocked state, without weakening or bypassing the approval requirement.

No files were modified, and no external services were accessed. Because the fixture contains only the blocked-state line, approval provenance, notification behavior, accessibility, cancellation handling, and actual work preservation remain unverified.