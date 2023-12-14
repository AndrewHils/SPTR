import numpy as np

def matrix_math_n1(matrix):
    min_in_rows = np.min(matrix, axis=1)
    print('Мінімуми у рядках:', min_in_rows)

    max_of_mins = np.max(min_in_rows)
    print('Максимум серед мінімумів рядків:', max_of_mins)

    max_in_columns = np.max(matrix, axis=0)
    print('Максимуми у стовпцях:', max_in_columns)

    min_of_maxs = np.min(max_in_columns)
    print('Мінімум серед максимумів стовпців:', min_of_maxs)

    if max_of_mins != min_of_maxs:
        print("\nСідлової точки не існує, отже рівноваги в чистих стратегіях не існує")

def matrix_math_n2(matrix):
    min_in_columns = np.min(matrix, axis=0)
    print('Мінімуми у стовпцях:', min_in_columns)
    max_of_mins = np.max(min_in_columns)
    print('Максимум серед мінімумів у стовпцях:', max_of_mins)

    max_in_rows = np.max(matrix, axis=1)
    print('Максимуми у рядках:', max_in_rows)
    min_of_maxs = np.min(max_in_rows)
    print('Мінімум серед максимумів у рядках:', min_of_maxs)

    if max_of_mins != min_of_maxs:
        print("\nСідлової точки не існує, отже рівноваги в чистих стратегіях не існує")

matrix_1 = np.array([
    [-8, 6, 0, 7],
    [3, -1, 4, 4],
    [5, 4, 3, 4]
])

matrix_2 = np.array([
    [0.66, 0.34, 0.34, 0.34, 0.34, 0.34],
    [0.12, 0.88, 0.12, 0.12, 0.12, 0.12],
    [0.16, 0.16, 0.84, 0.16, 0.16, 0.16],
    [0.4, 0.4, 0.4, 0.6, 0.4, 0.4],
    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    [0.2, 0.2, 0.2, 0.2, 0.2, 0.8]
])
def main():
    print('Завдання №1\n')
    print('Початкова матриця:')
    print(matrix_1)
    matrix_math_n1(matrix_1)

    print('\nЗавдання №2\n')
    print('Початкова матриця:')
    print(matrix_2)
    matrix_math_n2(matrix_2)

if __name__ == "__main__":
    main()
