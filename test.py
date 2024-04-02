import pandas as pd

df = pd.read_csv('./People_data/강우협_275940033494646785.csv')

df = df['Total_credit'][len(df) -1]
print(df)