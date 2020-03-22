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

from sklearn.linear_model import LogisticRegression

# create model
clf = LogisticRegression(C=3)
# train model
clf.fit(train_feature_matrix, train_labels)
# predict using trained model
y_pred = clf.predict(test_feature_matrix)

from sklearn.metrics import accuracy_score

accuracy_score(test_labels, y_pred)

from sklearn.model_selection import GridSearchCV

# re-create model using another solver
clf = LogisticRegression(solver='saga')

# describe the grid
param_grid = {
    'C': np.arange(1, 5), # possible [1, 2, 3, 4]
    'penalty': ['l1', 'l2'],
}

# create cross-validation object GridSearchCV
search = GridSearchCV(clf, param_grid, n_jobs=-1, cv=5, refit=True, scoring='accuracy')

# train/search
search.fit(feature_matrix, labels)

# print best params
print(search.best_params_)

accuracy_score(labels, search.best_estimator_.predict(feature_matrix))

