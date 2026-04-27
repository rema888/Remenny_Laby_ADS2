def f(matrix):

    n = len(matrix)
    memo = {}

    def connect(visited, current_city):

        state = (tuple(sorted(visited)), current_city)

        if state in memo:
            return memo[state]

        if len(visited) == n:
            return matrix[current_city][0]

        min_dist = float('inf')

        for next_city in range(n):
            if next_city not in visited:
                dist = matrix[current_city][next_city] + connect(visited + [next_city], next_city)

                if dist < min_dist:
                    min_dist = dist

        memo[state] = min_dist
        return min_dist

    return connect([0], 0)

distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# 0-1-3-2-0 = 10+25+30+15
print(f"Результат: {f(distances)}")