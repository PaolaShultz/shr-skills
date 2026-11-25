Use a **pause-and-return** flow. Keep the form open in the same tab and hold its values only in memory. When reauthentication becomes mandatory, immediately hide the form, block access to it, and show a lock screen. Keep the server’s reauthentication requirement in force for every save or submission.

The lock screen can say **“Sign in again to continue. Keep this tab open to keep your draft.”** Open sign-in in a separate window so the form tab survives the redirect. Reveal the draft only after the server confirms fresh authentication for the same account. Return focus to the field the user was editing. If sign-in is canceled, keep the draft locked and offer **Try again** and **Discard draft**.

Keep sensitive values out of browser storage, URLs, and logs. Clear the in-memory draft on sign-out, account change, or expiry of a bounded recovery period. Closing or reloading the form tab loses the draft, so explain that limit before the user leaves.

No changes were made.