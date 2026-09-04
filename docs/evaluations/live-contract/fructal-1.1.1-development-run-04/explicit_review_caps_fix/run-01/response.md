Review mode.

`workflow.txt` contains only `state=blocked`. No approval decision, approver identity, pending action, or recovery instruction is recorded.

The approval constraint is necessary, but the file’s opaque blocked state creates workflow friction: actors cannot tell whether approval is pending, denied, or completed, nor who can resume progress.

I did not change the file because Review mode prohibits modifying system state. The state should remain blocked until authoritative approval evidence exists. Once confirmed, an authorized actor can update it to the appropriate approved/unblocked state. The material open decision is the approval’s source and outcome.