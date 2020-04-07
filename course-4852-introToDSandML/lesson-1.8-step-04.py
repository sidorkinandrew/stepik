import pandas as pd
import numpy as np

# 1.8.4
dataset_url = 'https://stepik.org/media/attachments/course/4852/my_stat.csv'
my_stat = pd.read_csv(dataset_url)
my_stat.head()

# 1.8.4
# select rows with 'V3' == 'A' and ' V1' > 0
%timeit subset_1 = my_stat[(my_stat["V1"] > 0) & (my_stat["V3"].isin(['A']))]

# select rows with 'V2' != 10 or 'V4' >= 1
%timeit subset_2 = my_stat[(my_stat["V4"] >= 1) | (my_stat["V2"] != 10)]