import pandas as pd

exam_data = {
  '수학': [90, 80, 70],
  '영어': [98, 89, 95],
  '음악': [85, 95, 100],
  '체육': [100, 90, 90]
  }

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)

# 복제 -> row 삭제
df2 = df.copy()
df2 = df2.drop('우현') # 행 삭제
print(df2)

df3 = df.copy()
df3 = df3.drop(['우현', '인아'], axis=0) # axis=1
print(df3)

df4 = df.copy()
df4 = df4.drop(['우현', '인아'], axis='index') # axis='columns'
print(df4)

df5 = df.copy()
df5 = df5.drop(columns=['수학'])
print(df5)