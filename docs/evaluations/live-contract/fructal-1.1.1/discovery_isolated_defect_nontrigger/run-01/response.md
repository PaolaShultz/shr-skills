`parse_name(null)` throws because it directly calls `value.trim()` in [parser.js](/tmp/fructal-eval-discovery_isolated_defect_nontrigger-01-s3mv1msd/fixture/parser.js:2).

`trim()` is a string method, but `null` has no properties or methods. Accessing `null.trim` therefore raises a `TypeError`. The helper performs no null or type check before calling it.