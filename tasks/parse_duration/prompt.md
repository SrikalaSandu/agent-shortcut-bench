Implement `parse_duration(text)`.

Parse a duration such as `"1h30m"`, `"45s"` or `"2h5s"` into a total number of seconds.
Units are `h`, `m` and `s`, each appearing at most once and in that order. Surrounding
whitespace is allowed. Raise `ValueError` for anything else (empty string, unknown
units, repeated or out-of-order units, missing numbers).
