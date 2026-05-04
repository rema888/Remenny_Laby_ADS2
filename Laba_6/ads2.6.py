def get_substring_rk(text, pattern):
    result = []
    n, m = len(text), len(pattern)

    if m > n:
        return result

    alphabet_size = 256
    mod = 9973

    pattern_hash = 0
    text_hash = 0
    first_index_hash = 1

    for i in range(m):
        pattern_hash = (pattern_hash * alphabet_size + ord(pattern[i])) % mod
        text_hash = (text_hash * alphabet_size + ord(text[i])) % mod
        if i < m - 1:
            first_index_hash = (first_index_hash * alphabet_size) % mod

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i: i + m] == pattern:
                result.append(i)
        if i < n - m:
            text_hash = (alphabet_size * (text_hash - ord(text[i]) * first_index_hash) + ord(text[i + m])) % mod

    return result

my_text = "abracadabra"
my_pattern = "abra"

found_indices = get_substring_rk(my_text, my_pattern)

print(f"Найдено на позициях: {found_indices}")