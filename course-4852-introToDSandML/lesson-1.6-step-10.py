import requests, zipfile, io
import pandas as pd
import numpy as np

dataset_url = 'http://stepik.org/media/attachments/course/4852/algae.csv'
r = requests.get(dataset_url)
concentrations = pd.read_csv(io.BytesIO(r.content))

# count different algae groups, range (max - min) for 'sucrose', variance for 'citrate'
concentrations.groupby('group', as_index = False)\
    .agg({'glucose':'count',
          'sucrose': lambda x: x.max() - x.min(),
          'citrate':'var'}) \
    .rename(columns = {'glucose':'count','sucrose':'range','citrate':'variance'}).round(2)