import pandas as pd
import numpy as np

from google.colab import files
uploaded = files.upload()
all_data = pd.read_csv('forest_dataset.csv',)
all_data.head()

all_data.shape

labels = all_data[all_data.columns[-1]].values
feature_matrix = all_data[all_data.columns[:-1]].values

from sklearn.model_selection import train_test_split

train_feature_matrix, test_feature_matrix, train_labels, test_labels = train_test_split(
    feature_matrix, labels, test_size=0.2, random_state=42)  # 80% training and 20% test
# X_train, X_test, y_train, y_test

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

clf = KNeighborsClassifier(n_neighbors=4)  # create KNN model

clf.fit(train_feature_matrix, train_labels)  # use X_train to target y_train

y_pred = clf.predict(test_feature_matrix)  # based on X_test trying to predict y_pred

# task 9-11
from sklearn.model_selection import GridSearchCV

params = {
    'metric': ['manhattan', 'euclidean'],
    'weights': ['uniform', 'distance'],
    'n_neighbors': [1,2,3,4,5,6,7,8,9,10],
    }

clf_grid = GridSearchCV(clf, params, cv=5, scoring='accuracy', n_jobs=-1, verbose=1)

clf_grid.fit(train_feature_matrix, train_labels)  # use X_train to target y_train

# result - best parameters
print(clf_grid.best_params_)  # {'metric': 'manhattan', 'n_neighbors': 4, 'weights': 'distance'}
