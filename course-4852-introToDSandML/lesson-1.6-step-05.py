import requests, zipfile, io
import pandas as pd
import numpy as np

ds_url = 'https://stepik.org/media/attachments/course/4852/dota_hero_stats.csv'
r = requests.get(ds_url)
dota = pd.read_csv(io.BytesIO(r.content))

# group heroes by 'legs' column and count them in categories
dota.groupby(['legs']).aggregate({'legs':'count'})