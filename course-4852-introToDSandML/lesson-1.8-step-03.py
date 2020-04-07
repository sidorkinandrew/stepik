import pandas as pd
import numpy as np

# 1.8.3
dataset_url = 'https://stepik.org/media/attachments/course/4852/my_stat.csv'
my_stat = pd.read_csv(dataset_url)
my_stat.head()


# task 1.8.3 create 2 given subsets
# select first 10 rows and 1 and 3 column
subset_1 = my_stat.loc[:9,:].iloc[:,[0,2]]

# select all rows except 1 and 5th and 2nd and 4th columns
subset_2 = my_stat.drop([0,4]).iloc[:,[1,3]]

#%timeit subset_2 = my_stat.iloc[:, [1, 3]].drop([0, 4])
#%timeit subset_2 = my_stat.iloc[:, [1, 3]][~my_stat.index.isin([0, 4])]
#%timeit subset_2 = my_stat.drop([0, 4]).iloc[:,[1,3]]
#%timeit subset_2 = my_stat.iloc[~my_stat.index.isin([0, 4]), [1, 3]]
#%timeit subset_2 = my_stat.drop(index=[0, 4], columns=['V1', 'V3'])
#%timeit subset_2 = my_stat.loc[:, ['V2','V4']].drop([0, 4], axis=0)
#%timeit subset_2 = my_stat.iloc[:, [1, 3]].query('index != 0 and index != 4')

#1000 loops, best of 3: 772 µs per loop
#1000 loops, best of 3: 825 µs per loop
#1000 loops, best of 3: 913 µs per loop
#1000 loops, best of 3: 962 µs per loop
#1000 loops, best of 3: 1.12 ms per loop
#1000 loops, best of 3: 1.22 ms per loop
#100 loops, best of 3: 2.92 ms per loop