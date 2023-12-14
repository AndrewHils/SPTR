import numpy as np

matrix = np.array([
    [85, 30, 22, 0.65, 6],
    [60, 20, 10, 0.6, 7],
    [30, 12, 5, 0.45, 5],
    [75, 24, 13, 0.7, 8],
    [40, 15, 7, 0.55, 7]
])

weights = np.array([7, 5, 6, 8, 6])

print('Початкова матриця:')
print(matrix)

norm_matrix = matrix / np.max(matrix, axis=0)

print('Нормалізована матриця:')
print(norm_matrix)

w_matrix = norm_matrix * weights

print('\nМатриця після множення на ваги:')
print(w_matrix)

sum_row = np.sum(w_matrix, axis=1)

print('\nСуми значень кожного рядка:')
for row_sum in sum_row:
    print(row_sum)

max_result = np.max(sum_row)
max_result_pos = np.argmax(sum_row) + 1

# Виведення максимального значення та його позиції
print('\nМаксимальне значення:', max_result, f'у альтернативі A{max_result_pos}')
