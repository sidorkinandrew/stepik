import requests, zipfile, io
import pandas as pd
import numpy as np

dataset_url = 'http://stepik.org/media/attachments/course/4852/algae.csv'
r = requests.get(dataset_url)
concentrations = pd.read_csv(io.BytesIO(r.content))

# calculate minimum, average and maximum concentration of 'alanin' for 'Fucus'-es, round the result to 2 decimal digits
concentrations.query("genus == 'Fucus'")['alanin'].agg(['min', 'mean', 'max']).round(2)