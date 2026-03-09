def egg_drop_two_eggs(floors=100):
    x = 0
    steps_sum = 0

    while steps_sum < floors:
        x += 1
        steps_sum += x

    return x

min_drops = egg_drop_two_eggs(100)
print(f"Минимальное количество бросков: {min_drops}")