# reading an excel file with pandas
# Author: Andrew Beatty
import pandas as pd

filename = '../data/grades.xlsx'
df_grades = pd.read_excel(filename, sheet_name='grades')
df_names = pd.read_excel(filename, sheet_name='names')

print (df_grades)
print (df_names)
