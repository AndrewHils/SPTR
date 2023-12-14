import numpy as np
from scipy.optimize import linear_sum_assignment

def results(matrix, row_i, col_i):
    print("Найкраще призначення:")
    for i in range(len(row_i)):
        print(
            f"Робітник {row_i[i] + 1} = Верстат {col_i[i] + 1},",
            f" відоток браку буде становити {matrix[row_i[i],col_i[i]]}%"
        )
    print(f"Мінімальний сумарний відсоток становить {matrix[row_i,col_i].sum()}%")

matrix = np.array([
        [2.3, 1.9, 2.2, 2.7],
        [1.8, 2.2, 2.0, 1.8],
        [2.5, 2.0, 2.2, 3.0],
        [2.0, 2.4, 2.4, 2.8]
])
num_columns = len(matrix[0])
def main():
    print("Початкова Матриця :")
    print(matrix)

    min_in_rows = np.min(matrix, axis=1, keepdims=True)

    res_matrix = matrix - min_in_rows
    print("\nПоточна матриця :")
    print(res_matrix)

    min_values = []
    for col in range(num_columns):
        column_values = [row[col] for row in res_matrix]
        min_value = min(column_values)
        min_values.append(min_value)

    for col in range(num_columns):
        for row in range(len(res_matrix)):
            res_matrix[row][col] -= min_values[col]

    print("\nМінімальні значення в стовпцях")
    print(min_values)
    print("\n")

    row_i,col_i = linear_sum_assignment(matrix)
    results(matrix,row_i,col_i)

if __name__ == '__main__':
    main()