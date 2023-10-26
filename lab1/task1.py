import pandas as pd

df = pd.read_excel('task.xlsx', sheet_name='task1')
result_df = df * df.iloc[-1]
result_df = result_df.iloc[:-1]
sum_column = result_df.sum(axis=1)

def print_results():
    print('Оцінки критеріїв для альтернатив та їх вага: ')
    print(df)
    print('Значення привабливості альтернатив на основі оцінок їх критеріїв та ваги: ')
    print(result_df)
    print(sum_column)
    print("Альтернатива з максимальним значенням привабливості: ")
    print('A{}'.format(sum_column.idxmax() + 1))

print_results()