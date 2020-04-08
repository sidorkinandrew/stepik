import pandas as pd
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns

dataset_url = 'https://stepik.org/media/attachments/course/4852/event_data_train.zip'
events_data = pd.read_csv(dataset_url)
events_data.head()

events_data.action.unique()

events_data['date'] = pd.to_datetime(events_data.timestamp, unit='s')
events_data.head()

events_data.dtypes
events_data.date.min()
events_data.date.max()

events_data['day'] = events_data.date.dt.date
events_data.head()

events_data.groupby('day').user_id.nunique().plot()

sns.set(rc={'figure.figsize': (9, 6)})
events_data.groupby('day').user_id.nunique().plot()


# wrong way
events_data[events_data.action == 'passed'] \
    .groupby('user_id', as_index=False) \
    .agg({'step_id': 'count'}) \
    .rename(columns={'step_id': 'passed_steps'}) \
    .passed_steps.hist()

# checking
events_data[events_data.action == 'passed'] \
    .groupby('user_id', as_index=False) \
    .agg({'step_id': 'count'}) \
    .rename(columns={'step_id': 'passed_steps'}).passed_steps.min()
    
# correct way
events_data.pivot_table(index='user_id', \
                        columns='action', \
                        values='step_id', \
                        aggfunc='count', \
                        fill_value=0).head()
                        
events_data.pivot_table(index='user_id', \
                        columns='action', \
                        values='step_id', \
                        aggfunc='count', \
                        fill_value=0).reset_index().head()

events_data.pivot_table(index='user_id', \
                        columns='action', \
                        values='step_id', \
                        aggfunc='count', \
                        fill_value=0).reset_index().discovered.hist()

dataset_url = 'https://stepik.org/media/attachments/course/4852/submissions_data_train.zip'
submissions_data = pd.read_csv(dataset_url)
submissions_data.head()


submissions_data['date'] = pd.to_datetime(submissions_data.timestamp, unit='s')
submissions_data['day'] = submissions_data.date.dt.date
submissions_data.head()

users_scores = submissions_data.pivot_table(index='user_id',
                        columns='submission_status',
                        values='step_id',
                        aggfunc='count',
                        fill_value=0).reset_index()
users_scores.head()

submissions_data.groupby('user_id').agg({'step_id': 'count'}).hist()

events_data[['user_id', 'day', 'timestamp']].drop_duplicates().head()

events_data[['user_id', 'day', 'timestamp']].drop_duplicates(['user_id', 'day']).head()

events_data[['user_id', 'day', 'timestamp']].drop_duplicates(['user_id', 'day']) \
    .groupby('user_id')['timestamp'].apply(list).head()
    
events_data[['user_id', 'day', 'timestamp']].drop_duplicates(['user_id', 'day']) \
    .groupby('user_id')['timestamp'].apply(list) \
    .apply(np.diff)

events_data[['user_id', 'day', 'timestamp']].drop_duplicates(['user_id', 'day']) \
    .groupby('user_id')['timestamp'].apply(list) \
    .apply(np.diff).head()

gap_data = events_data[['user_id', 'day', 'timestamp']].drop_duplicates(['user_id', 'day']) \
    .groupby('user_id')['timestamp'].apply(list) \
    .apply(np.diff).values

np.concatenate(gap_data, axis=0)

gap_data = pd.Series(np.concatenate(gap_data, axis=0))

gap_data / (24 * 60 * 60)
gap_data = gap_data / (24 * 60 * 60)
gap_data.hist()

gap_data[gap_data < 208].hist()

gap_data.quantile(0.95)

gap_data.quantile(0.90)

events_data.tail()

events_data.groupby('user_id', as_index=False) \
    .agg({'timestamp': 'max'}).head()
    
user_data = events_data.groupby('user_id', as_index=False) \
    .agg({'timestamp': 'max'}).rename(columns={
    'timestamp': 'last_timestamp'
})
user_data.head()

user_data['is_gone_user'] = 1526772811 - user_data.last_timestamp
user_data.head()

now = 1526772811
drop_out_treshold = 2592000

user_data['is_gone_user'] = (now - user_data.last_timestamp) > drop_out_treshold
user_data.head()

# wrong way
user_data.merge(users_scores).head()
# correct way
user_data.merge(users_scores, how='outer').head()
user_data.merge(users_scores, on='user_id', how='outer').head()

# wrong way - only 5 rows !!!
user_data.merge(users_scores.head())
user_data = user_data.merge(users_scores, on='user_id', how='outer').head()

# correct way
user_data = user_data.merge(users_scores, on='user_id', how='outer')
user_data = user_data.fillna(0)
user_data.head(20)

users_events_data = events_data.pivot_table(index='user_id',
                        columns='action',
                        values='step_id', 
                        aggfunc='count', 
                        fill_value=0).reset_index()
users_events_data.head()

user_data = user_data.merge(users_events_data, how='outer')
user_data.head()

users_days = events_data.groupby('user_id').day.nunique()
users_days.head()

users_days = events_data.groupby('user_id').day.nunique().to_frame().reset_index()
users_days.head()

user_data = user_data.merge(users_days, how='outer')
user_data.head()

user_data.user_id.nunique() == events_data.user_id.nunique()

user_data['passed_course'] = user_data.passed > 175
user_data.head()

user_data.groupby('passed_course').count()