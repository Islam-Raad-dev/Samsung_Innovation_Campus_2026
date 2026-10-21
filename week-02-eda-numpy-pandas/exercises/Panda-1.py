import pandas as pd

data = pd.read_csv(
    "/home/islam-raad/Projects/Samsung_Innovation_Campus_2026/week-02-eda-numpy-pandas/exercises/data_studentlist.csv"
)

print(data.nunique())
