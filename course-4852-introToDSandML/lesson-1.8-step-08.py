import pandas as pd
import numpy as np

# 1.8.7
dataset_url = 'https://stepik.org/media/attachments/course/4852/my_stat_1.csv'
my_stat = pd.read_csv(dataset_url)
my_stat.head()

# 1.8.8
# count mean values of the 'session_value' column per each group, 'group' should not be as index
# rename the resulting column into 'mean_session_value', save the result under the 'mean_session_value_data' dataset

mean_session_value_data = my_stat.groupby('group', as_index=False).agg({'session_value': 'mean'}).rename(columns={'session_value':'mean_session_value'})
