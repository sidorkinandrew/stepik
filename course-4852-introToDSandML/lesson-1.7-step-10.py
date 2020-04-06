import pandas as pd
import numpy as np

dataset_url = 'https://stepik.org/media/attachments/course/4852/iris.csv'
df = pd.read_csv(dataset_url, index_col=0)
df.head()

# plot violin plot for petal length
sns.violinplot(df["petal length"], orient='v', color="Purple")
