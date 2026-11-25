`parse_name(null)` throws because [parser.js, line 2](/tmp/fructal-eval-isolated_defect_nontrigger-01-eqaxahg7/fixture/parser.js:2) reads `value.trim` before checking for `null`. I reproduced the TypeError with the existing test and confirmed that `' Ada '` returns `'Ada'`.

The fix is to handle `null` before calling `trim()`. The test does not specify what `parse_name(null)` should return.