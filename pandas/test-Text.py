import pandas as pd
import numpy as np

fruit_names = pd.Series(['Apple', 'Banana', 'Cherry'])
print(fruit_names)

pd.Series(['Apple', 'Banana', 'Cherry'], dtype='string')
pd.Series(['Apple', 'Banana', 'Cherry'], dtype=pd.StringDtype())

fruit_names.astype('string')

ser = pd.Series(["Apple_사과", "Banana_바나나", "Cherry_체리", np.nan],
                index=["First ", " Second", " Third", "Fourth"])
print(ser)
ser2 = pd.Series(["Apple_사과", "Banana_바나나", "Cherry_체리", np.nan],
                index=["First ", " Second", " Third", "Fourth"], dtype='string')
print(ser2)

# 소문자/대문자로 변환
print(ser.str.lower())
print(ser.str.upper())
print(ser.str.len())

# 문자열 분할
print(ser.str.split('_')) # list로 반환
print(type(ser.str.split('_')['First '])) # list
print(ser.str.split('_', expand=True)) # DataFrame으로 확장
print(ser.str.split('_').str.get(1)) # 특정 요소 선택

# 행 인덱스 추출
idx = ser.index
print(idx)

# 문자열 교체
print(ser.str.replace('_', ':', regex=False)) # regex=False로 정규식이 아닌 단순 문자열로 처리
print(ser.str.replace('[^a-zA-Z\s]', '', regex=True))

# 특정 문자 포함 여부 확인
contains_A = ser.str.contains('A', na=False) # na=False로 NaN 값을 False로 처리
print(contains_A)

# 패턴 포함 여부 확인
contains_pattern = ser.str.contains(r'[A|B][a-z]+')
print(contains_pattern)

# 전체 문자열 패턴 일치 여부 확인
fullmatch_pattern = ser.str.fullmatch(r'[A|B][a-z]+')
print(fullmatch_pattern)

