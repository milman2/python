import pandas as pd

exam_data = {
  '이름': ['서준', '우현', '인아'],
  '수학': [90, 80, 70],
  '영어': [98, 89, 95],
  '음악': [85, 95, 100],
  '체육': [100, 90, 90]
  }

df = pd.DataFrame(exam_data)
df = df.set_index('이름') # multi-index : df.set_index(['수학', '음학'])
print(df)

# transpose
df = df.transpose() # 메소드 활용
print(df)

df = df.T # 클래스 속성 활요
print(df)