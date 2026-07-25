Ran `./generate.sh` exactly once.

`artifact.txt` is 43 bytes and differs from `expected.txt`:

- Actual: `STATUS: amber`
- Expected: `STATUS: green`
- Differing byte offsets: 38, 39, 40, 42
- Artifact SHA-256: `19585e8f7eabd01226a5bfcd6efa228d1dcce3728306b6d9aa5b7411a2445abd`

The artifact was preserved byte-for-byte after generation. I did not rerun the generator or modify, replace, or delete any files.