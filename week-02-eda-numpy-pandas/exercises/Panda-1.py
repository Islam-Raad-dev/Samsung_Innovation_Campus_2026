import pandas as pd

student_list = pd.read_csv(
    "/home/islam-raad/Projects/Samsung_Innovation_Campus_2026/week-02-eda-numpy-pandas/exercises/data_studentlist.csv"
)

Name = student_list["name"]

print(student_list.to_string())
print("*" * 100)
print(student_list.head(16).isnull().sum(axis=0))
print("*" * 100)
print(student_list.head(16).notnull().sum(axis=0))

mean_age = student_list["age"].mean()

student_list = student_list.fillna({"age": mean_age})

print("*" * 100)

print(student_list["age"].mean())

print("*" * 100)

print(student_list["age"])

df_dup = student_list["age"].duplicated()

print("*" * 100)
print(df_dup)
