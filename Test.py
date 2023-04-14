import pandas as pd
import re

file = pd.read_excel('D:\Desktop\Sample.xlsx')
pd.set_option('display.max_columns', 50)
print(file.to_string(index=False))

selected_columns = input('Введите столбцы для вывода через запятую: ').split(', ')
filter_columns = input('Введите столбцы для фильтрации через запятую: ').split(', ')

filter_criteria = {}
condition = True
for column in filter_columns:
    filter_value = input(f'Введите условие фильтра для столбца {column}: ')
    if filter_value == '':
        condition = condition & file[column].isna()
    else:
        filter_criteria[column] = filter_value
        if column in file.columns:
            if file[column].dtype == 'O':
                regex_pattern = re.sub('%', '.*', filter_value)
                condition = condition & file[column].str.contains(regex_pattern)
            else:
                regex_pattern = re.sub('%', '.*', str(filter_value))
                condition = condition & file[column].astype(str).str.contains(regex_pattern)

filtered_file = file.loc[condition, selected_columns]

print(filtered_file.to_string(index=False))

