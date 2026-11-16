import pandas as pd
from pathlib import Path

data_dir = Path(".")

for csv_path in sorted(data_dir.glob("*.csv")): #glob() returns all files matching the pattern, sorted() sorts them alphabetically
    pq_path = csv_path.with_suffix(".parquet")
    if pq_path.exists():
        print(f"Skipping {csv_path.name} because {pq_path.name} already exists.")
        continue

    print(f"Converting {csv_path.name} to {pq_path.name}...")
    df = pd.read_csv(csv_path, low_memory=False)
    df.to_parquet(pq_path, index=False)
    print(f"  rows={len(df):,}  cols={df.shape[1]}") #df.shape     e.g. (1630000, 35) -> number of rows and columns
    print(f"  columns: {df.columns.tolist()}\n")
    df = pd.read_parquet(pq_path)
    print(f"Shape: {df.shape}")
    print(f"Data types:\n{df.dtypes}")
    print(f"DF HEAD:\n{df.head()}")
    print(f"Missing:{df.isna().sum()}")        # how many rows have no value for that column
    print(f"Description:\n{df.describe()}")          # gives quick statistical summary of each numeric column, which spots weird values

