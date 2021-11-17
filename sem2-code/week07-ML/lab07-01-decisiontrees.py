import pandas
from sklearn import tree
import pydotplus  # pip install pydotplus
from  sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

# I had to install graphviz and add it to my path
import os
os.environ["PATH"] += os.pathsep + 'C:/Users/ABeatty/Desktop/Graphviz/bin/'

df = pandas.read_csv("shows.csv")
#print(df)

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
# this part of the code is just displaying the decision tree
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')
img = pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()

# predicting results
print(dtree.predict([[40, 10, 7, 1]]))

print("[1] means 'GO'")
print("[0] means 'NO'")
