import pandas as pd

df01 = pd.read_csv("test01.csv")
df02 = pd.read_csv("test02.csv")

df01 = df01.add_prefix("1_")
df02 = df02.add_prefix("2_")

df01 = df01.drop(["1_y", "1_z"], axis=1)
df02 = df02.drop(["2_y", "2_z"], axis=1)

result = df01.join(df02)

ave = result.mean(axis=1)
ave = pd.DataFrame(ave, columns=["X"])

print(df01)
print(df02)
print(result)
print(ave)

ave.to_csv("average.csv", index = False)