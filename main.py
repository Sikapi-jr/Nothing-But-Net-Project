import pandas as pd
df_peek = pd.read_csv("PlayerStatistics.csv", nrows=1000) 
print(df_peek.dtypes, df_peek.head(), df_peek.columns.tolist()) #df.head() returns first 5 rows of dataset