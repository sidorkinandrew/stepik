import requests, zipfile, io
import pandas as pd
import numpy as np

dataset_url = 'https://stepik.org/media/attachments/course/4852/titanic.csv'
r = requests.get(dataset_url)
df = pd.read_csv(io.BytesIO(r.content))
# number of columns/rows
print(df.shape)
# types of the columns
for atype in set(df.dtypes):
    print(atype, len(df.select_dtypes([atype]).columns))