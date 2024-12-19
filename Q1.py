import pandas as pd

excel_file_random = "data_random.xlsx" 
excel_file_sorted = "data_sorted.xlsx"
df = pd.read_excel(excel_file_random)
print (df.head())
