import pandas as pd
import numpy as np

# task 1.8.2 create a DataFrame
data_string = """type    value\n
A    10\n
A    14\n
B    12\n
B    23"""
df = pd.read_csv(io.StringIO(data_string), sep="\s+|\t")  #, names=data_string.split("\n")[0].split(), engine='python')
df.head()
df.columns