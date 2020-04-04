import requests, zipfile, io
import pandas as pd
import numpy as np

ds_url = 'https://stepik.org/media/attachments/course/4852/titanic.csv'
r = requests.get(ds_url)
df = pd.read_csv(io.BytesIO(r.content))

print(df.shape)
print(df.dtypes)