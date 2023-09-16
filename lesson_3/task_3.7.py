# 3.7. Удалите повторяющиеся значения из списка


x = [1, 2, 3, 4, 5, 3, 2, 1]


unique_values = []

for value in x:
    if value not in unique_values:
        unique_values.append(value)

print(unique_values)
