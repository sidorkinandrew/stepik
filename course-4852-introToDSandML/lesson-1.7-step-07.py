import pandas as pd
import numpy as np

dataset_url = "https://stepik.org/media/attachments/course/4852/genome_matrix.csv"
df = pd.read_csv(dataset_url, index_col=0)  # custom index
df.head()

# plot colormap using matplotib
heatmap = plt.pcolormesh(df)

# or using sns
heatmap = sns.heatmap(df, cmap='viridis')
heatmap.xaxis.set_ticks_position('top')
heatmap.xaxis.set_tick_params(rotation=90)