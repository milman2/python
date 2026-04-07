import pandas as pd

dict_data = {
  'c0': [1, 2, 3],
  'c1': [4, 5, 6],
  'c2': [7, 8, 9],
  'c3': [10, 11, 12],
  'c4': [13, 14, 15]
  }

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)

# reset_index : 행 인덱스를 정수형으로 초기화
ndf3 = df.reset_index()
print(ndf3)

# 행 인덱스를 정수형으로 초기화 하고, 기존 인덱스의 열 이름 지정
ndf4 = df.reset_index(names=['C00'])
print(ndf4)

# 행 인덱스를 초기화하고, 기존 인덱스를 삭제
ndf5 = df.reset_index(drop=True)
print(ndf5)
