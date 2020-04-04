import requests, zipfile, io
import pandas as pd
import numpy as np

ds_url = 'https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv'
r = requests.get(ds_url)
df = pd.read_csv(io.BytesIO(r.content))

# compare mean and variance of scores for 'standard' and 'free/reduced' students
standart_lunches = df[df['lunch'].isin(['standard'])]
reduced_lunches  = df[df['lunch'].isin(['free/reduced'])]
print(reduced_lunches.mean() - standart_lunches.mean())  # 'free/reduced' have less scores
print(reduced_lunches.var() - standart_lunches.var())  # 'free/reduced' have more varianced values
