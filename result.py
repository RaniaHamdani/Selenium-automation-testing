import pandas as pd

data = pd.read_csv("C:\Users\21627\Downloads\suites.csv")

data.to_excel("Suites_Chrome.xlsx", index=None, header=True)