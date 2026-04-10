import seaborn as sns
import pandas as pd

# 데이터셋을 로컬에 저장
df = sns.load_dataset("titanic")
df.to_csv("pandas/data/titanic.csv", index=False)

# 이후에는 로컬에서 불러오기
df = pd.read_csv("pandas/data/titanic.csv")