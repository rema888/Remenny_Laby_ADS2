def first_fit_decreasing(items, capacity):
    sorted_items = sorted(items, reverse=True)

    bins = []
    bin_contents = []

    for item in sorted_items:
        placed = False
        for i in range(len(bins)):
            if bins[i] + item <= capacity:
                bins[i] += item
                bin_contents[i].append(item)
                placed = True
                break

        if not placed:
            bins.append(item)
            bin_contents.append([item])

    return bin_contents

weights = [4, 8, 1, 4, 2, 1]
bin_cap = 10

for i, b in enumerate(first_fit_decreasing(weights, bin_cap), 1):
    print(f"Ящик {i}: {b} (сумма: {sum(b)})")