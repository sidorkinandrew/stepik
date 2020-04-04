import requests, zipfile, io
import pandas as pd
import numpy as np

ds_url = 'https://stepik.org/media/attachments/course/4852/dota_hero_stats.csv'
r = requests.get(ds_url)
dota = pd.read_csv(io.BytesIO(r.content))

# group heroes by 'attack_type' and 'primary_attr', select the most used type of hero
dota.groupby(['attack_type', 'primary_attr']).aggregate({'id':'count'}).idxmax()
# or 
dota.groupby(['attack_type', 'primary_attr']).aggregate({'id':'count'}).sort_values('id', ascending=False).head(1)
