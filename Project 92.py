import numpy as np
import pandas as pd
df=pd.read_csv("Loan_Default.csv")
a=df.drop("Status",axis=1)
y=df["Status"]
print(a.head())