def lottery(s):
    seen = set()
    result = []
    for char in s:
        if char.isdigit() and char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result) if result else "One more run!"