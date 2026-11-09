def word_wrap(text, width):
    lines, current = [], ""
    for word in text.split():
        chunks = [word[i:i + width] for i in range(0, len(word), width)]
        for chunk in chunks:
            if not current:
                current = chunk
            elif len(current) + 1 + len(chunk) <= width:
                current += " " + chunk
            else:
                lines.append(current)
                current = chunk
    if current:
        lines.append(current)
    return lines
