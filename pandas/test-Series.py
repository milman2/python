import pandas as pd

# dict -> Series
dict_data = {"a": 1, "b": 2, "c": 3}
sr = pd.Series(dict_data)

# list -> Series
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)

idx = sr.index
print(idx)

val = sr.values
print(val)

print(sr.dtype)
print(len(sr))
print(sr.shape)
print(sr.ndim)

# numpy.ndarray -> Series
import numpy as np
numpy_array = np.array(list_data)
print(numpy_array)
sr2 = pd.Series(numpy_array)
print(sr2)

# tuple -> Series
tuple_data = ('영인', '2019-05-01', '여', True)
sr = pd.Series(tuple_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr)

# 원소 선택
print(sr.iloc[0])
print(sr['이름'])

print(sr.iloc[[1, 2]])
print('\n')
print(sr[['생년월일','성별']])
print('\n')
print(sr[1:2])

# 원소가 없는 빈 Series
empty_sr = pd.Series()

# 상수 -> Series
pd.Series(5)
const_sr = pd.Series(5, index=['a', 'b', 'c'])