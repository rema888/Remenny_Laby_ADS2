def search(text, pattern):
    m = len(pattern)
    dfa = {}

    # Строим таблицу
    for state in range(m + 1):
        for char in set(pattern):
            combined = pattern[:state] + char

            for k in range(state + 1, 0, -1):
                if combined.endswith(pattern[:k]):
                    dfa[(state, char)] = k
                    break
    # Поиск
    current_state = 0
    results = []

    for i in range(len(text)):
        current_state = dfa.get((current_state, text[i]), 0)

        if current_state == m:
            results.append(i - m + 1)

    return results

print(search("AABAACAADAABA", "AABA"))