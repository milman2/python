import pandas as pd

df = pd.DataFrame([
  [15, '남', '덕영중'],
  [17, '여', '수리중']
  ],
  index=['서준', '예은'],
  columns=['나이', '성별', '학교'])

print(df)
print(df.index)
print(df.columns)

df = df.rename(columns={'나이' : '연령', '성별' : '남녀', '학교' : '소속'}) # inplace=True
print(df)
df = df.rename(index={'서준' : '학생1', '예은' : '학생2'})
print(df)

# row index, column name 변경
df.index = ['Student1', 'Student2']
df.columns = ['Age', 'Sex', 'School']
print(df)
print(df.index)
print(df.columns)