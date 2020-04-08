import pandas as pd
import numpy as np

# 1.11.5
dataset_url = 'https://stepik.org/media/attachments/course/4852/submissions_data_train.zip'
submissions_train = pd.read_csv(dataset_url)
submissions_train.head()

# 1.11.5 locate the course creator user_id
karp = submissions_train.pivot_table(index='user_id',
                              columns='submission_status',
                              values='step_id',
                              aggfunc='count', fill_value=0).reset_index()
karp[karp['correct']==max(karp['correct'])]