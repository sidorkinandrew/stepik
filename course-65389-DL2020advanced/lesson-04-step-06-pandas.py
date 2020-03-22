import pandas as pd
import numpy as np

# data = pd.read_csv('https://drive.google.com/uc?id=1il9RDoxwrgUjoOqd9yvdV760_M1AvziI')
# the data is from https://www.kaggle.com/sdolezel/black-friday

from google.colab import files
uploaded = files.upload()
data = pd.read_csv('BlackFriday.csv',)

# task 6
%time men_26_35 = len(data[data["Gender"].isin(["M"])&data["Age"].isin(["26-35"])]); women_after_36 = len(data[data["Gender"].isin(["F"])&data["Age"].isin(['36-45', '46-50', '51-55', '55+'])]); (women_after_36+men_26_35)/len(data)
%time q = "(((Gender == 'M') & (Age == '26-35')) | ((Gender == 'F') & (Age in ['36-45', '46-50', '51-55', '55+'])))"; data.query(q).shape[0] / data.shape[0]
%time data.query('(Gender=="F" and Age in ("36-45", "46-50", "51-55", "55+") or (Gender=="M" and Age=="26-35"))').shape[0] /data.shape[0]
# OR slower
%time data.query("Gender=='F'and Age>'36' or Gender=='M' and Age=='26-35'").shape[0]/len(data)
%time task4 = pd.crosstab(data['Age'], data['Gender'], normalize=True); task4['F']['36-45':].values.sum()+task4['M']['26-35']
%time len(((data.Gender=='M')&(data.Age=='26-35')) | ((data.Gender=='F') &(data.Age>'36'))) / len(data)
%time data[((data.Gender == "M") & (data.Age == "26-35")) | ((data.Gender == "F") & (~data.Age.isin(["0-17", "18-25", "26-35"])))].shape[0] / data.shape[0]
%time data[((data.Gender=='M') & (data.Age == '26-35')) | ((data.Gender=='F') & ((data.Age > '36')))].shape[0]
%time (len(data[(data.Gender == 'F')&(data.Age > '26-35')]) + len(data[(data.Gender == 'M')&(data.Age == '26-35')]))/len(data)
