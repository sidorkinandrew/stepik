import pandas as pd
from scipy.stats import entropy
import numpy as np
import requests, zipfile, io

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns


dataset_url = 'https://stepik.org/media/attachments/course/4852/cats.csv'
enthropy_dataset = pd.read_csv(dataset_url)
enthropy_dataset

def ent(data):
  return entropy(data.Вид.value_counts() / len(data), base=2)

# calc enthropy
print('Шерстист на 0: ', ent(enthropy_dataset[enthropy_dataset.Шерстист == 0]))
print('Шерстист на 1: ', ent(enthropy_dataset[enthropy_dataset.Шерстист == 1]))
print('Гавкает на 0: ', ent(enthropy_dataset[enthropy_dataset.Гавкает == 0]))
print('Гавкает на 1: ', ent(enthropy_dataset[enthropy_dataset.Гавкает == 1]))
print('Лазает по деревьям на 0: ', ent(enthropy_dataset[enthropy_dataset['Лазает по деревьям'] == 0]))
print('Лазает по деревьям на 1: ', ent(enthropy_dataset[enthropy_dataset['Лазает по деревьям'] == 1]))

# calc information gain
def ig(data, feature):
  ent0 = ent(data[data[feature] == 0])
  ent1 = ent(data[data[feature] == 1])
  n = len(data)
  n0 = len(data[data[feature] == 0])
  n1 = len(data[data[feature] == 1])
  return ent(data) - ent0 * n0 / n - ent1 * n1 / n

# semi-manual
E = -(4/10)*np.log2(4/10) - (6/10)*np.log2(6/10)
sh0 = ent(enthropy_dataset[enthropy_dataset.Шерстист == 0])
sh1 = ent(enthropy_dataset[enthropy_dataset.Шерстист == 1])
print("Information gain for Шерстист:", round(E - (1/10*sh0+9/10*sh1),2))
g0 = ent(enthropy_dataset[enthropy_dataset.Гавкает == 0])
g1 = ent(enthropy_dataset[enthropy_dataset.Гавкает == 1])
print("Information gain for Гавкает:", round(E - (5/10*g0+5/10*g1),2))
l0 = ent(enthropy_dataset[enthropy_dataset['Лазает по деревьям'] == 0])
l1 = ent(enthropy_dataset[enthropy_dataset['Лазает по деревьям'] == 1])
print("Information gain for Лазает по деревьям:", round(E - (6/10*l0+6/10*l1),2))

# automated
for afeature in ["Шерстист","Гавкает","Лазает по деревьям"]:
  print("Information gain for",afeature,"is", round(ig(enthropy_dataset,afeature),2))

# OR alternatively:
from IPython.display import SVG
from graphviz import Source
from IPython.display import display

df = pd.read_csv('https://stepik.org/media/attachments/course/4852/cats.csv', index_col=0)
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
for attribute in ['Шерстист','Гавкает', 'Лазает по деревьям']:
    X = df[[attribute]]
    y = df[['Вид']]
    clf.fit(X,y)
    print(tree.plot_tree(clf.fit(X,y)))
    graph = Source(tree.export_graphviz(clf, out_file=None, feature_names=list(X), class_names=['Negative', 'Positive'], filled=True))
    display(SVG(graph.pipe(format='svg')))