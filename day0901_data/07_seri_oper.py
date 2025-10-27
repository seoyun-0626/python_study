import pandas as pd
import numpy as np
pd.set_option('display.unicode.east_asian_width',True)

#시리즈 산술연산

student1 = pd.Series({'국어':100, '수학':95, '영어':90})
print(student1)
print()

percentage = student1 / 200

print(percentage)
print(type(percentage))
print()

student2 = pd.Series({'국어':80, '수학':75, '영어':60})
# 이름 맞는 친구들 찾아서 연산
# (순서 바꿔도 찾아서 연산)

addition = student1 + student2

print(addition)
print()

# 뺄셈, 곱셈, 나눗셈도 가능
subtraction = student1 - student2
multiplication = student1 * student2
division = round(student1 / student2)

df = pd.DataFrame([addition, subtraction, multiplication, division],
                  index=['덧셈', '뺄셈', '곱셈', '나눗셈'])

print('--원본--')
print(df)
print("\n--전치--")
print(df.T)
print()

print('----- Nan 이 나오는 경우 -----')
print()

student1 = pd.Series({'국어':np.nan, '수학':95, '영어':90})
student2 = pd.Series({'국어':80, '수학':75})

addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = round(student1 / student2)

df = pd.DataFrame([addition, subtraction, multiplication, division],
                  index=['덧셈', '뺄셈', '곱셈', '나눗셈'])

print(df)
print()

print('----- 연산메서드 (넌값 채우기) -----')
print()

student1 = pd.Series({'국어':np.nan, '수학':95, '영어':90})
student2 = pd.Series({'국어':80, '수학':75})

sr_add = student1.add(student2,fill_value=0) # 덧셈
sr_sub = student1.sub(student2,fill_value=0) # 뺄셈
sr_mul = student1.mul(student2,fill_value=0) # 곱셈
sr_div = round(student1.div(student2,fill_value=0)) # 나눗셈

df = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div],
                  index=['덧셈','뺄셈','곱셈','나눗셈'])

print(df)


