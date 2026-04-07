import pandas as pd
import numpy as np
import seaborn as sns

# Series + Operator(+-*/) + Number
student1 = pd.Series({'국어': 80, '영어': 90, '수학': 70})
print(student1)

percentage = student1 / 200
print(percentage)
print(type(percentage))

# Series  + Operator(+-*/) + Series
student1 = pd.Series({'국어': 100, '영어': 80, '수학': 90})
student2 = pd.Series({'수학': 80, '국어': 90, '영어': 80})

addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(addition)
print(type(addition))

result = pd.concat([addition, subtraction, multiplication, division],
                   keys=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)

student1 = pd.Series({'국어': np.nan, '영어': 80, '수학': 90})
student2 = pd.Series({'수학': 80, '국어': 90})
addition = student1.add(student2, fill_value=0) #addition = student1 + student2
subtraction = student1.sub(student2, fill_value=0) # subtraction = student1 - student2
multiplication = student1.mul(student2, fill_value=0) # multiplication = student1 * student2
division = student1.div(student2, fill_value=0) # division = student1 / student2
result = pd.DataFrame([addition, subtraction, multiplication, division],
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)

# DataFrame + Operator(+-*/) + Number
# DataFrame + Operator(+-*/) + DataFrame
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head()) #

addition = df + 10
print(addition.tail()) # 마지막 5행만 표시

subtraction = addition - df
print(subtraction.tail())

sample1 = addition.tail()
sample2 = subtraction.tail().fillna(0)

df_add = sample1.add(sample2, fill_value=0)
df_sub = sample1.sub(sample2, fill_value=0)
df_mul = sample1.mul(sample2, fill_value=0)
df_div = sample1.div(sample2, fill_value=0)
