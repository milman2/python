import pandas as pd

# dict -> DataFrame
dict_data = {'c0': [1, 2, 3], 'c1': [4, 5, 6], 'c2': [7, 8, 9], 'c3': [10, 11, 12], 'c4': [13, 14, 15]}
df = pd.DataFrame(dict_data)
print(type(df))
print(df)

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

# 성적 데이터 처리 예
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

# 행 인덱스를 사용하여 행 1개를 선택
label1 = df.loc['서준'] # 열 이름을 사용하여 열 1개를 선택
position1 = df.iloc[0] # 행 번호를 사용하여 행 1개를 선택
print(label1)
print('\n')
print(position1)

# 행 인덱스를 사용하여 행 여러 개를 선택
label2 = df.loc[['서준', '인아']]
position2 = df.iloc[[0, 2]]
print(label2)
print('\n')
print(position2)

# 행 인덱스의 범위를 지정하여 행 선택
label3 = df.loc['서준':'인아']
position3 = df.iloc[0:2]
print(label3)
print('\n')
print(position3)

# 성적 데이터 처리 예
exam_data = {
  '이름': ['서준', '우현', '인아'],
  '수학': [90, 80, 70],
  '영어': [98, 89, 95],
  '음악': [85, 95, 100],
  '체육': [100, 90, 90]
  }
df = pd.DataFrame(exam_data)
print(df)
print('\n')
print(type(df))

# '수학' 점수 데이터만 선택
math1 = df['수학']
print(math1)
print('\n')
print(type(math1)) # '수학'은 Series이 Name 속성

# '영어'
english = df.영어
print(english)
print('\n')
print(type(english)) # '영어'도 Series이 Name 속성

# '음악', '체육' : 여러 컬럼 => 배열
music_gym = df[['음악', '체육']]
print(music_gym)
print('\n')
print(type(music_gym)) # '음악', '체육'은 DataFrame이 columns 속성


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

# 열 추가
df['국어'] = 80
print(df)
df['미술'] = [80, 80, 100]
print(df)

exam_data = {
  '이름': ['서준', '우현', '인아'],
  '수학': [90, 80, 70],
  '영어': [98, 89, 95],
  '음악': [85, 95, 100],
  '체육': [100, 90, 90]
  }
df = pd.DataFrame(exam_data)

# 행 추가
df.loc[3] = 0
print(df)
df.loc[4] = ['동규', 90, 80, 85, 95]
print(df)

# 행 복사
df.loc['행5'] = df.loc[3]
print(df)

exam_data = {
  '이름': ['서준', '우현', '인아'],
  '수학': [90, 80, 70],
  '영어': [98, 89, 95],
  '음악': [85, 95, 100],
  '체육': [100, 90, 90]
  }
df = pd.DataFrame(exam_data)
df = df.set_index('이름') # multi-index : df.set_index(['수학', '음학'])
# 값 변경
df.iloc[0][3] = 80 # ChainedAssignmentError
print(df)
df.iloc[0, 3] = 80
print(df)

import warnings
warnings.filterwarnings('ignore')
df.loc['서준']['체육'] = 90 # ChainedAssignmentError
print(df)

df.loc['서준', '체육'] = 100
print(df)

df.loc['서준', ['음악', '체육']] = 50
print(df)

df.loc['서준', ['음악', '체육']] = 100, 50
print(df)

# 행,열 전치
df = df.transpose() # 메소드 활용
print(df)

df = df.T # 클래스 속성 활요
print(df)

#
dict_data = {
  'c0': [1, 2, 3],
  'c1': [4, 5, 6],
  'c2': [7, 8, 9],
  'c3': [10, 11, 12],
  'c4': [13, 14, 15]
  }
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)

# reindex
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(index=new_index)
print(ndf)

ndf2 = df.reindex(index=new_index, fill_value=0)
print(ndf2)

ndf3 = df.reset_index()
print(ndf3)

ndf4 = df.reset_index(names='C00')
print(ndf4)

ndf5 = df.reset_index(drop=True)
print(ndf5)

# sort_index
ndf = df.sort_index(ascending=False)
print(ndf)

ndf2 = df.sort_index(ascending=True)
print(ndf2)

# sort_values
ndf = df.sort_values(by='c1', ascending=False)
print(ndf)

ndf2 = df.sort_values(by=['c3', 'c4'], ascending=[False, True])
print(ndf2)
