import pandas as pd
import csv

df = pd.read_csv("Dataset.csv")
print(df.shape)

del df["planet_mass"]

print(df.shape)

df = df.rename({
    " ":"Serial no.",
    },axis="columns")
df.to_csv("Main.csv")

df2 = pd.read_csv("Main.csv")
print(df.shape)