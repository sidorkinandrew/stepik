import pandas as pd
import numpy as np

# 1.8.7
dataset_url = 'https://stepik.org/media/attachments/course/4852/my_stat_1.csv'
my_stat = pd.read_csv(dataset_url)
my_stat.head()

# 1.8.7 
# fill missing values in 'session_value' column with 0
my_stat.session_value.fillna(0, inplace=True)

# fill negative values of 'n_users' column with the median of the column (not including negatives)
%timeit my_stat.loc[my_stat["n_users"] < 0, "n_users"] =  my_stat[my_stat["n_users"] >= 0].n_users.median()

# OR 
my_stat = pd.read_csv(dataset_url)
%timeit -n 1 my_stat.n_users = my_stat.n_users.apply(lambda x: x if x >= 0 else my_stat.n_users[my_stat.n_users >= 0].median())
my_stat = pd.read_csv(dataset_url) 
%timeit -n 1 my_stat.n_users.where(my_stat.n_users >= 0, my_stat.n_users[my_stat.n_users >= 0].median(), inplace=True)
my_stat = pd.read_csv(dataset_url) 
%timeit -n 1 my_stat.loc[my_stat.n_users < 0, 'n_users'] = my_stat.query('n_users >= 0').n_users.median()

