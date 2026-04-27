def get_substring_bm(text, pattern):
    result = []
    n, m = len(text), len(pattern)

    if m == 0 or m > n:
        return result

    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i

    shift = 0
    while shift <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:

            result.append(shift)

            if shift + m < n:
                char_in_text = text[shift + m]
                shift += m - bad_char.get(char_in_text, -1)
            else:
                shift += 1
        else:

            char_in_text = text[shift + j]
            shift += max(1, j - bad_char.get(char_in_text, -1))

    return result

text = "однажды в студеную зимнюю пору"
pattern = "пору"
print(f"Найдено на позициях: {get_substring_bm(text, pattern)}")