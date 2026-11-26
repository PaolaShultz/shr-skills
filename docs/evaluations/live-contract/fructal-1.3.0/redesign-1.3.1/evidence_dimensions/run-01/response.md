The note supports a finding of **reported context loss**. Blocked recovery is a separate claim from the requester and remains unverified.

| Classification | Evidence |
|---|---|
| Provided artifact | The requester supplied [support-note.txt](/tmp/fructal-eval-evidence_dimensions-01-v70r0q2v/fixture/support-note.txt:1). |
| Observed by direct inspection | The file contains one line: “Operators report that retries lose context.” It contains no statement about a recovery outcome. |
| Reported by operators | The note attributes context loss during retries to operators. Reading it verifies the attribution, not the behavior of a retry. |

The requester identifies the retained policy: failed requests must remain resumable across the support-to-service handoff. If the reported context loss occurs, the receiving service may lack information needed to resume a request. Whether any request actually failed to resume remains open.