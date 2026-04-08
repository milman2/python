import pandas as pd

exam_data = {
  '이름': ['서준', '우현', '인아'],
  '수학': [90, 80, 70],
  '영어': [98, 89, 95],
  '음악': [85, 95, 100],
  '체육': [100, 90, 90]
  }
df = pd.DataFrame(exam_data)
# df = df.set_index('이름')

# 열 추가
df['국어'] = 80
print(df)
df['미술'] = [80, 80, 100]
print(df)