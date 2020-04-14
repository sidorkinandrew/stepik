from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# %matplotlib inline

from IPython.display import SVG
from graphviz import Source
from IPython.display import display

from IPython.display import HTML
style = "<style>svg{width:30% !important;height:30% !important;}</style>"
HTML(style)




dataset_url = 'https://stepik.org/media/attachments/course/4852/titanic.csv'
titanic_data = pd.read_csv(dataset_url)

titanic_data.head()

titanic_data.isnull().sum()

X = titanic_data.drop(['PassengerId','Survived','Name', 'Ticket', 'Cabin'], axis=1)
y = titanic_data.Survived

X = pd.get_dummies(X)

X = X.fillna({'Age': X.Age.median()})

X.isnull().sum()

clf = tree.DecisionTreeClassifier(criterion='entropy')

clf.fit(X,y)

import sklearn
graph = Source(sklearn.tree.export_graphviz(clf, out_file=None,
                                   feature_names=list(X),
                                   class_names=['Negative','Positive'],
                                   filled = True))
display(SVG(graph.pipe(format='svg')))

""" when overfitting = decrease tree max_depth or use more data """

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.33, random_state=42)

X_train.shape

X_test.shape

clf.score(X, y)

clf.fit(X_train, y_train)

clf.score(X_train, y_train)

clf.score(X_test, y_test)

""" big difference in scores = overfitting """

clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)

clf.fit(X_train, y_train)

clf.score(X_train, y_train)

clf.score(X_test, y_test)

""" let's find the best parameter for max_depth """

max_depth_values = range(1, 100)

scores_data = pd.DataFrame()

for max_depth in max_depth_values:
    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=max_depth)
    clf.fit(X_train, y_train)
    train_score = clf.score(X_train, y_train)
    test_score = clf.score(X_test, y_test)
    
    temp_score_data = pd.DataFrame({'max_depth': [max_depth],
                                    'train_score': [train_score],
                                    'test_score': [test_score]})
    scores_data = scores_data.append(temp_score_data)

scores_data.head()

""" https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.melt.html """

scores_data_long = pd.melt(scores_data, id_vars=['max_depth'], value_vars=['train_score', 'test_score'],
                          var_name='set_type', value_name='score')

scores_data_long.head()

"""https://stackoverflow.com/questions/51422146/install-the-latest-version-of-seaborn-0-9-0-through-pip

 pip3 install seaborn==0.9.0
"""

import seaborn

seaborn.__version__

"""https://seaborn.pydata.org/generated/seaborn.lineplot.html"""

sns.lineplot(x="max_depth", y="score", hue="set_type", data=scores_data_long)

"""####
more deep tree increases accuracy on train dataset but does not help generalize it (work more effectively on test/real data)
test_score starts slow  - model is under-fitted (does not learn much yet)
max_depth 3-5 (here) is optimal
increasing depth - increases train score 
but test score decreases - transition from under-fitted to over-fitted

https://scikit-learn.org/stable/modules/cross_validation.html

allows for fitting on several "folds" from the train dataset
"""

from sklearn.model_selection import cross_val_score

clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=4)

cross_val_score(clf, X_train, y_train , cv=5)

cross_val_score(clf, X_train, y_train , cv=5).mean()

scores_data = pd.DataFrame()

for max_depth in max_depth_values:
    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=max_depth)
    clf.fit(X_train, y_train)
    train_score = clf.score(X_train, y_train)
    test_score = clf.score(X_test, y_test)
    
    mean_cross_val_score = cross_val_score(clf, X_train, y_train , cv=5).mean()
    
    temp_score_data = pd.DataFrame({'max_depth': [max_depth],
                                    'train_score': [train_score],
                                    'test_score': [test_score],
                                    'cross_val_score': [mean_cross_val_score]})
    scores_data = scores_data.append(temp_score_data)



""" cv = 5 - K-fold, k = 5"""

scores_data.head()

scores_data_long = pd.melt(scores_data, id_vars=['max_depth'], value_vars=['train_score', 'test_score', 'cross_val_score'],
                          var_name='set_type', value_name='score')

scores_data_long.head()

sns.lineplot(x="max_depth", y="score", hue="set_type", data=scores_data_long)

""" max accuracy when max_depth > 5

cross_val_score is more stable to overfitting

let's find the optimal  cross_val_score
"""

scores_data_long.query("set_type == 'cross_val_score'").head(20)

"""5	cross_val_score	0.800303"""

best_clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=14)

cross_val_score(best_clf, X_test, y_test , cv=5).mean()

from sklearn.model_selection import GridSearchCV

clf = tree.DecisionTreeClassifier()
clf

parametrs = {'criterion': ['gini', 'entropy'], 'max_depth': range(1, 30)}

grid_search_cv_clf = GridSearchCV(clf, parametrs, cv=5)

grid_search_cv_clf.fit(X_train, y_train)

grid_search_cv_clf.best_params_

best_clf = grid_search_cv_clf.best_estimator_

best_clf.score(X_test, y_test)

from sklearn.metrics import precision_score, recall_score

y_pred = best_clf.predict(X_test)

precision_score(y_test, y_pred)

recall_score(y_test, y_pred)

y_predicted_prob = best_clf.predict_proba(X_test)

pd.Series(y_predicted_prob[:, 1]).hist()

y_pred = np.where(y_predicted_prob[:, 1] > 0.9, 1, 0)

pd.Series(y_predicted_prob[:, 1]).unique()

precision_score(y_test, y_pred)

recall_score(y_test, y_pred)

from sklearn.metrics import roc_curve, auc
fpr, tpr, thresholds = roc_curve(y_test, y_predicted_prob[:,1])
roc_auc= auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, color='darkorange', label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()

