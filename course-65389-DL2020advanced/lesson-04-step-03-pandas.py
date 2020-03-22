import pandas as pd
import numpy as np

# data = pd.read_csv('https://drive.google.com/uc?id=1il9RDoxwrgUjoOqd9yvdV760_M1AvziI')
# the data is from https://www.kaggle.com/sdolezel/black-friday

from google.colab import files
uploaded = files.upload()
data = pd.read_csv('BlackFriday.csv',)

# task 3
%time len(data[data["City_Category"].isin(['A'])&data["Gender"].isin(['M'])])
# OR
%time data.query('City_Category == "A" & Gender == "M"').shape[0]
%time data['City_Category'].where(data['City_Category']!='A',1).where(data['Gender']=='M',0).where(data['City_Category']=='A',0).sum()
%time sum((data.Gender=='M') &(data.City_Category=='A'))
%time city = data[data['City_Category'] == 'A']; city.groupby(['Gender']).size()
%time data[(data.City_Category == 'A') & (data.Gender=='M')]['Gender'].count()
