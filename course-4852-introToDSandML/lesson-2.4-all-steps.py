import pandas as pd
import numpy as np
import requests, zipfile, io
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
from sklearn.model_selection import cross_val_score



dataset_url = 'https://stepik.org/media/attachments/course/4852/train_iris.csv'
iris_data_train = pd.read_csv(dataset_url, index_col=0)
dataset_url = 'https://stepik.org/media/attachments/course/4852/test_iris.csv'
iris_data_test = pd.read_csv(dataset_url, index_col=0)

# prepare datasets
X_train = iris_data_train.drop(['species'], axis=1)
y_train = iris_data_train.species

X_test = iris_data_test.drop(['species'], axis=1)
y_test = iris_data_test.species

np.random.seed(0)  # external to the cycle
rs = np.random.seed(0)
scores_data =  pd.DataFrame()
max_depth_values = range(1, 101)  # max_depth to test

for current_level in max_depth_values:
    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=current_level, random_state=rs)
    clf.fit(X_train, y_train)
    temp_score_data = pd.DataFrame({'max_depth': [current_level],
                                    'train_score': [clf.score(X_train, y_train)],
                                    'test_score': [clf.score(X_test, y_test)],
                                    'cross_val_score': [cross_val_score(clf, X_train, y_train, cv=5).mean()]})
    scores_data = scores_data.append(temp_score_data)

# plot train, test, cross_validation scores
plt.figure(figsize=(10, 5))
plt.plot(max_depth_values, scores_data.train_score)
plt.plot(max_depth_values, scores_data.test_score)
plt.plot(max_depth_values, scores_data.cross_val_score)

# alternatively for SNS
scores_data_long = pd.melt(scores_data, id_vars=['max_depth'], value_vars=["train_score","test_score"],
                           var_name = "set_type", value_name="score")

scores_data_long.head()

sns.lineplot(x="max_depth", y="score", hue="set_type", data=scores_data_long)



# train a model and use test data to predict values
# test data
from google.colab import files
uploaded = files.upload()
cats_dogs_test = pd.read_json(uploaded[list(uploaded.keys())[0]])
cats_dogs_test.head()


# train data
dataset_url = 'https://stepik.org/media/attachments/course/4852/dogs_n_cats.csv'
cats_dogs_train = pd.read_csv(dataset_url)
cats_dogs_train.head()

# prepare data_sets
X_train = cats_dogs_train.drop("Вид", axis=1)
y_train = cats_dogs_train.Вид

# train model
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(X_train, y_train)

from IPython.display import SVG
from graphviz import Source
from IPython.display import display
from sklearn import tree 

# visualize the Decision Tree result
print(tree.plot_tree(clf.fit(X_train, y_train)))
graph = Source(tree.export_graphviz(clf, out_file=None, feature_names=list(X_train), class_names=['Negative', 'Positive'], filled=True))
display(SVG(graph.pipe(format='svg')))

# make predictions using test data
predicts = clf.predict(cats_dogs_test)
np.count_nonzero(predicts=="собачка") # count guessed values