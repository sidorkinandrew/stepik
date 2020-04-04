import requests, zipfile, io
import pandas as pd
import numpy as np

dataset_url = 'https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv'
r = requests.get(dataset_url)
df = pd.read_csv(io.BytesIO(r.content))

# count share of 'free/reduced'-lunch students
print(np.sum(df['lunch'].isin(['free/reduced']) / len(df)))
