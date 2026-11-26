No correctness issues found. `parse_ascii` accepts ASCII strings up to and including 64 characters and returns the original string. I verified that 65 ASCII characters return `(False, 'maximum length is 64 characters')`, an empty string succeeds, and `café` returns `(False, 'ASCII characters required')`.

Both existing tests passed when invoked directly. Pytest was unavailable in the fixture.