import pandas as pd
import numpy as np

# 1.8.6
dataset_url = 'https://stepik.org/media/attachments/course/4852/my_stat.csv'
my_stat = pd.read_csv(dataset_url)
my_stat.head()

# 1.8.6
# rename columns
%timeit my_stat.columns = ['session_value','group','time','n_users']
%timeit my_stat.columns = {'session_value':'V1', 'group':'V2', 'time':'V3', 'n_users':'V4'}
%timeit my_stat.rename(columns={'V1': 'session_value', 'V2': 'group', 'V3': 'time', 'V4': 'n_users'}, inplace=True)