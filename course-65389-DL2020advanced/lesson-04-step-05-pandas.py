import pandas as pd
import numpy as np

# data = pd.read_csv('https://drive.google.com/uc?id=1il9RDoxwrgUjoOqd9yvdV760_M1AvziI')
# the data is from https://www.kaggle.com/sdolezel/black-friday

from google.colab import files
uploaded = files.upload()
data = pd.read_csv('BlackFriday.csv',)

# task 5
%time len(data["Product_Category_3"].isnull())
# OR
%time data["Product_Category_3"].isnull().sum()
%time len(data) - data['Product_Category_3'].count()
%time data['Product_Category_3'].value_counts(dropna=False)
%time data[data['Product_Category_3'].isnull()].shape[0]
%time data.query('Product_Category_3 != Product_Category_3').shape[0]
%time sum(np.isnan(data.Product_Category_3))
%time sum(data.Product_Category_3.isnull() == True)
%time data.isna().sum()