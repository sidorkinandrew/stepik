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

# task 8
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

clf = KNeighborsClassifier(n_neighbors=4)  # create KNN model

clf.fit(train_feature_matrix, train_labels)  # use X_train to target y_train

y_pred = clf.predict(test_feature_matrix)  # based on X_test trying to predict y_pred

accuracy_score(test_labels, y_pred)  # y_test, y_pred