import pandas as pd
import numpy as np

# data = pd.read_csv('https://drive.google.com/uc?id=1il9RDoxwrgUjoOqd9yvdV760_M1AvziI')
# the data is from https://www.kaggle.com/sdolezel/black-friday

from google.colab import files
uploaded = files.upload()
data = pd.read_csv('BlackFriday.csv',)

# task 4
%time len(data[data["Gender"].isin(['F'])&data["Age"].isin(['46-50'])&data["Purchase"].gt(20000)])
# OR a bit quicker
%time data.query('Age == "46-50" and Gender == "F" and Purchase > 20000').shape[0]
# slower
%time len(data[(data.Age == '46-50') & (data.Gender=='F') & (data.Purchase > 20000)])
%time data[(data.Gender=='F') & (data.Age == '46-50') & (data.Purchase > 20000)]['Gender'].count()


