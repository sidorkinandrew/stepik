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