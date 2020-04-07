import pandas as pd
import numpy as np

# 1.8.5
dataset_url = 'https://stepik.org/media/attachments/course/4852/my_stat.csv'
my_stat = pd.read_csv(dataset_url)
my_stat.head()

# 1.8.5
# create another column as a sum of 1st and 4th columns
%timeit my_stat['V5'] = my_stat['V1'] + my_stat['V4']
# create another column calculating logarithm of the second column
%timeit my_stat['V6'] = np.log(my_stat['V2'])