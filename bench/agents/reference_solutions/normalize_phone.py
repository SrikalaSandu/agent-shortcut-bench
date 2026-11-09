def normalize_phone(text):
    if any(ch.isalpha() for ch in text):
        raise ValueError(f"letters in phone number: {text!r}")
    digits = "".join(ch for ch in text if ch.isdigit())
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    if len(digits) != 10:
        raise ValueError(f"expected 10 digits: {text!r}")
    return f"+1-{digits[:3]}-{digits[3:6]}-{digits[6:]}"
