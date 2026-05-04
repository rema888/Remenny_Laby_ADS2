def kmp_search(text, pattern):

    pi = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    # ABCAB
    # Префиксы: A, AB, ABC, ABCA
    # Суффиксы: B, AB, CAB, BCAB => pi[4] = 2
    # Итоговая префикс-функция для ABCABD: [0,0,0,1,2,0]

    result = []
    j = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            result.append(i - j + 1)
            j = pi[j-1]
    return result

my_text = "abcabeabcabcabd"
my_patt = "abcabd"

found_indices = kmp_search(my_text, my_patt)

print(f"Найдено на позициях: {found_indices}")