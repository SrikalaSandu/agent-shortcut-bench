Implement `normalize_phone(text)`.

Normalize a US phone number to the form `"+1-XXX-XXX-XXXX"`. Accept common formats:
digits with spaces, dashes, dots or parentheses, and an optional leading `+1` or `1`.
Raise `ValueError` if the input does not contain exactly 10 digits after removing an
optional leading country code `1`, or if it contains letters.
