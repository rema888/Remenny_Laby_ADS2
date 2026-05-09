def bm(text, pattern):
    n, m = len(text), len(pattern)
    # Создаем словарь только для тех букв, что есть в шаблоне
    skip = {c: i for i, c in enumerate(pattern)}
    res = []
    i = 0

    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            res.append(i)
            i += 1
        else:
            i += max(1, j - skip.get(text[i + j], -1))
    return res

text = "однажды в студеную зимнюю пору"
pattern = "пору"
print(f"Найдено на позициях: {bm(text, pattern)}")