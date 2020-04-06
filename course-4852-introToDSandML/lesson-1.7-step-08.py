import pandas as pd
import numpy as np

dataset_url = 'https://stepik.org/media/attachments/course/4852/dota_hero_stats.csv'
dota = pd.read_csv(dataset_url)
dota.head()

# plot histogram of the most used number of roles per hero
dota.roles.map(eval).map(len).hist()

# or using sns
sns.distplot(dota.roles.map(eval).map(len))