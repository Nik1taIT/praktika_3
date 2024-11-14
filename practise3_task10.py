things = {'ключ': 3, 'булава': 1, 'монетки': 24, 'ліхтар': 1, 'камень': 10}

print("Обладнення:")
total_items = 0
for item, count in things.items():
    print(f"{count} {item}")
    total_items += count

print(f"Total number of things: {total_items}")
