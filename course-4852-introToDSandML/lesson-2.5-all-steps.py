import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split

dataset_url = 'https://stepik.org/media/attachments/course/4852/songs.csv'
songs_data = pd.read_csv(dataset_url)

X = songs_data.drop(['artist','lyrics','genre','song'],axis = 1)
y = songs_data.artist

X = pd.get_dummies(X)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3, random_state = 42, shuffle = True)
X_train.head()

# optimizing max_depth
np.random.seed(0)
rs = np.random.seed(0)
scores_data =  pd.DataFrame()
max_depth_values = range(1, 101)
best_params = {'label':'cross_val_score','best_value':0,'max_depth':0}
for current_depth in max_depth_values:
    clf = tree.DecisionTreeClassifier(max_depth=current_depth, random_state=rs).fit(X_train, y_train)
    scores_data = scores_data.append(pd.DataFrame({'max_depth': [current_depth],
                                    'train_score': [clf.score(X_train, y_train)],
                                    'test_score': [clf.score(X_test, y_test)],
                                    'cross_val_score': [cross_val_score(clf, X_train, y_train, cv=13).mean()]}))
    if scores_data[best_params['label']].iloc[-1] > best_params["best_value"]:
          best_params["best_value"] = scores_data[best_params['label']].iloc[-1]
          best_params["max_depth"] = current_depth

print(f'max_depth is {best_params["max_depth"]} with the best_score {best_params["best_value"]} for "{best_params["label"]}" as score criteria')
clf = DecisionTreeClassifier(max_depth = best_params["max_depth"], random_state=42)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

precision = precision_score(y_test, predictions, average='micro')
print(f"precision gained {precision}")