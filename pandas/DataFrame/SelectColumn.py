import pandas as pd

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
