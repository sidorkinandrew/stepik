import pandas as pd
import numpy as np

# data = pd.read_csv('https://drive.google.com/uc?id=1il9RDoxwrgUjoOqd9yvdV760_M1AvziI')
# the data is from https://www.kaggle.com/sdolezel/black-friday

from google.colab import files
uploaded = files.upload()
data = pd.read_csv('BlackFriday.csv',)

# task 2
%time len(set(data.Age))
# OR (quicker)
%time data["Age"].nunique()