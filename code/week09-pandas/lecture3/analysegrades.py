# in this program I do some basic analysis of the grades.csv
# author: Andrew Beatty

import pandas as pd

path = '../data/'
filenameForGrades = path + 'grades1.csv'


# make sure you set the header row and index_col
df = pd.read_csv(filenameForGrades,header= 0, index_col=0)
#df = pd.read_csv(filenameForGrades) # will not work as we wish
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
Studentmean = df.
print (df)
