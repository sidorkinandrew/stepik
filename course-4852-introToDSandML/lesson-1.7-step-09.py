import pandas as pd
import numpy as np

dataset_url = 'https://stepik.org/media/attachments/course/4852/iris.csv'
df = pd.read_csv(dataset_url, index_col=0)
df.head()

# plot histograms per column to see unimodal or bimodal distribution
for column in df:
    sns.distplot(df[column], kde_kws={"label":column})
