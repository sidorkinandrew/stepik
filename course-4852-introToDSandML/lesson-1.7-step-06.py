import requests, zipfile, io
import pandas as pd
import numpy as np

# download then upload dataset first
from google.colab import files
uploaded = files.upload()

# dataset is a long byte-string
df = [i.split(b" ") for i in uploaded[list(uploaded.keys())[0]].split(b"\r\n")]
df = pd.DataFrame(df[1:-1], columns=['x','y'], dtype=np.float64)
df.head()

# plot scatter graph via matplotlib
plt.scatter(df.x,df.y)
# or using sns
sns.scatterplot(df.iloc[:, 0], df.iloc[:, 1])