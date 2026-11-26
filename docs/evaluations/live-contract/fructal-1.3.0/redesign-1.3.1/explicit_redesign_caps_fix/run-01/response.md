Replace `state=blocked` with a pending approval request that tells the requester **who owns the next step, what they must decide, and how to resume**. This is a Fructal Cap Design proposal. The explicit Redesign cap limits the deliverable to the design and verification plan.

The supplied requirement places approval before the protected action. Inspection found only `state=blocked` in `workflow.txt`. A reader cannot tell from that file whether anyone has received the request or how to recover it. The approver, the exact action requiring approval, and whether a request already exists are open questions.

**Proposed workflow**

1. When work reaches the gate, preserve its position and the version submitted for approval. Give the requester a stable request ID, a description of the protected action, and the current owner. For the existing blocked item, first reconcile it with any outstanding request. If ownership is unknown, assign a routing owner to resolve it.
2. Give the authorized approver the same request ID and version, with explicit choices to approve or request changes. While the decision is pending, keep unrelated work available. If changes are requested, return ownership to the requester with the reason and a way to revise in place. A revision requires approval of the new version.
3. After approval, return the requester to the saved position with a **Continue** action that names the effect. Allow withdrawal before commitment. If continuation is interrupted, show its recorded status and reconcile any uncertain outcome before retrying, so one approval cannot accidentally produce the effect twice.

**Verification plan**

- Exercise approval, requested changes, revision, and withdrawal. Check the owner and next action at each handoff. Verify that an unauthorized decision, stale approval, or withdrawn request cannot release the protected action.
- Start with the current blocked item, simulate a lost response during submission and continuation, then reopen it. Verify one request ID, preserved work and position, and at most one protected effect.
- Complete the handoff by keyboard and with a screen reader. Check that the owner, decision, reason, and recovery action are discoverable. Compare unrelated workflow state before and after each path.

Implementation and runtime verification remain pending under the Redesign cap.