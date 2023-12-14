import numpy as np

matrix = np.array([
    [3, 7, 2, 9],
    [8, 3, 6, 7],
    [4, 8, 3, 5],
    [9, 6, 5, 4]
])

weights = np.array([8, 9, 6, 7])

print('Початкова матриця:')
print(matrix)

w_matrix = matrix * weights

print('\nМатриця після множення на ваги:')
print(w_matrix)

sum_row = np.sum(w_matrix, axis=1)

print('\nСуми значень кожного рядка:')
for row_sum in sum_row:
    print(row_sum)

max_result = np.max(sum_row)
max_result_pos = np.argmax(sum_row) + 1  # Додаємо 1, оскільки індекси починаються з 0

# Виведення максимального значення та його позиції
print('\nМаксимальне значення:', max_result, f'у альтернативі A{max_result_pos}')
