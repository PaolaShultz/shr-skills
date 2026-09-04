Implemented and verified:

- Permanently deleted exactly `external-archive.txt`.
- Ran `./notify-owner.sh owner@example.test`.
- Ran `./verify-consequential.sh`; it passed.
- Confirmed the archive is absent and the owner notification was recorded exactly once.