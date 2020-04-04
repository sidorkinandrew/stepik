import requests, zipfile, io
import pandas as pd
import numpy as np

url = 'https://stepik.org/media/attachments/course/4852/accountancy.csv'
r = requests.get(url)
accounting = pd.read_csv(io.BytesIO(r.content))

# compare average salary per 'executor' per 'type' and select top in each category
accounting.groupby(['Type','Executor']).\
		aggregate({'Salary':'mean'}).sort_values(['Type','Salary']).\
		groupby('Type').head(1)
