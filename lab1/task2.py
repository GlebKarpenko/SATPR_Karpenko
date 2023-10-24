import pandas as pd

df = pd.read_excel('task.xlsx', sheet_name='task2')
weight_df = df.iloc[-1]
result_df = df.iloc[:-1]

def normalize_maximizing(columns):
    return (columns - columns.min()) / (columns.max() - columns.min())

def normalize_minimizing(columns):
    return (columns.max() - columns) / (columns.max() - columns.min())

result_df.iloc[:, 0] = normalize_maximizing(result_df.iloc[:, 0])
result_df.iloc[:, 1] = normalize_minimizing(result_df.iloc[:, 1])
result_df.iloc[:, [2, 3, 4]] = normalize_maximizing(result_df.iloc[:, [2, 3, 4]])

functions_df = weight_df * result_df
functions_df = functions_df.sum(axis=1)

def print_results():
    print('Оцінки критеріїв для альтернатив та їх вага: ')
    print(df)
    print('Нормалізовані оцінки альтернатив: ')
    print(result_df)
    print("Функції користності для кожної альтернативи: ")
    print(functions_df)
    print("Найоптимальніша альтернатива за функцією корисності: ")
    print('A{}'.format(functions_df.idxmax() + 1))

print_results()