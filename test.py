import os
import pandas as pd
from glob import glob

files = glob('data/*.csv')

list = []
for f in files:
    list.append(pd.read_csv(f, header=1, names=("X", "Y", "Z", "Volume Fraction")))

print(list)