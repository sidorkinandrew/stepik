import pandas as pd
import numpy as np

dataset_url = 'https://stepik.org/media/attachments/course/4852/iris.csv'
df = pd.read_csv(dataset_url, index_col=0)
df.head()

# plot pairs of plots to see corellation between pairs of columns
sns.pairplot(df, hue="species")

# check correlation
print(df.iloc[:,:-1].corr())