import pandas as pd

# df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': ['25', '30']})
# print(df)

# df = pd.DataFrame({'Sr No.': ['1', '2', '3'], 'Name': ['Alice', 'Bob', 'Jake'], 'Age': ['25', '30', '28']})
# print(df)
# print(df.shape)
# print(df.columns)
# print(df.head(2))

df = pd.read_csv("pandas/addresses.csv", header=None, names=["First", "Last", "Address", "City", "State", "Zip"])
# print(df.head())
# print(df[["City", "First"]])
# print(df.iloc[0])
# print(df["City"])
# print(df[["City"]])
print(df[df["State"] == " NJ"])
# print(df["State"].unique())