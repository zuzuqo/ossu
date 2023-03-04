import pandas as pd

wwc = pd.read_csv('wwc2019.csv')
print(wwc)

for c in wwc.columns:
    print(c)
