import pandas as pd

exam_data = {
  '이름': ['서준', '우현', '인아'],
  '수학': [90, 80, 70],
  '영어': [98, 89, 95],
  '음악': [85, 95, 100],
  '체육': [100, 90, 90]
  }
df = pd.DataFrame(exam_data)
df = df.set_index('이름')

# 특정 원소 1개 선택
a = df.loc['서준', '음악'] # '서준'의 '음악' 점수 선택
print(a)
b = df.iloc[0, 2]
print(b)

# 특정 원소 2개 이상 선택
a = df.loc['서준', ['음악', '체육']] # '서준'의 '음악' 점수 선택
print(a)
b = df.iloc[0, [2, 3]]
print(b)
a = df.loc['서준', '음악':'체육']  # df.loc에서 범위를 지정할 때는 끝점이 포함됨
print(a)
b = df.iloc[0, 2:]
print(b)

# 2개 이상의 행과 열로부터 원소 선택
a = df.loc[['서준', '우현'], ['음악', '체육']]
print(a)
b = df.iloc[[0, 1], [2, 3]]
print(b)
a = df.loc['서준':'우현', '음악':'체육']  # df.loc에서 범위를 지정할 때는 끝점이 포함됨
print(a)
b = df.iloc[0:2, 2:]
print(b)
