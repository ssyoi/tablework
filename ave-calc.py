import pandas as pd
from glob import glob

files = glob('data/*.csv')

list = []
for f in files:
    list.append(pd.read_csv(f, header=1, names=("X", "Y", "Z", "Volume Fraction")))

for i in range(len(list)):
    list[i] = list[i].drop(["X","Y","Z"], axis=1)
    if i == 0:
        df = list[0]
    else:
        df += list[i]
    print(df)

result = df / len(list)

result.to_excel("data/average.xlsx")
    

print(list)