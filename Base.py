import pandas as pd
file = pd.read_excel('D:\Desktop\Sample.xlsx')
pd.set_option('display.max_columns', None)
print(file.to_string(index=False))
