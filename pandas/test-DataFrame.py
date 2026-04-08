import pandas as pd

# DataFrame/Construction.py

# row index / column name
df = pd.DataFrame([
  [15, '남', '덕영중'],
  [17, '여', '수리중']
  ],
  index=['서준', '예은'],
  columns=['나이', '성별', '학교'])
print(df)
print(df.index)
print(df.columns)

# row index, column name 변경
df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']
print(df)
print(df.index)
print(df.columns)

df = df.rename(columns={'연령': '나이', '남녀': '성별', '소속': '학교'})
print(df)
df = df.rename(index={'학생1': '서준', '학생2': '예은'})
print(df)

# DataFrame/drop.py
# DataFrame/SelectRow.py
# DataFrame/SelectColumn.py
# DataFrame/SelectData.py
# DataFrame/AddColumn.py
# DataFrame/AddRow.py
# DataFrame/ChangeValues.py
# DataFrame/transpose.py

# DataFrame/reindex.py
# DataFrame/reset_index.py
# DataFrame/sort_index.py
# DataFrame/sort_values.py
