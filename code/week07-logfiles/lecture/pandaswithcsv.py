# sample code showing opening a csv file with pandas
# Author Andrew Beatty
import pandas as pd


# this assumes that there is a header row and no index
df = pd.read_csv('../data/grades.csv')


print(df)
