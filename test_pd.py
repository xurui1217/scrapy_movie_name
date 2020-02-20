import pandas as pd
import numpy as np

df = pd.DataFrame(pd.read_csv('movie.csv'))
df = df[0:10]
# print(item[0])
df_np = np.array(df)
print(df_np)
df_lis = df_np.tolist()
print(df_lis)
