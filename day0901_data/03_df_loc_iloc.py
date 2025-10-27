import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

exam_data = {'수학':[90, 80, 70], '영어':[88, 77, 66], '음악':[30, 40, 50]}

df = pd.DataFrame(exam_data, index=['철수', '영희', '미진'])
print(df)
print()

print("----- 행 선택 -----")
print()

label1 = df.loc['철수']
label2 = df.iloc[0]
label3 = df.loc[['철수']]

print(label1)
print()
print(label2)
print()
print(label3)
print()

print(type(label1))
print(type(label2))
print(type(label3))
print()

label4 = df.loc[['철수', '영희']]
label5 = df.iloc[[0, 1]]

print(label4)
print()
print(label5)
print()

label6 = df.loc['철수':'영희'] # 영희 포함  # loc = “이름표로 찾기”
label7 = df.iloc[0:1] # 1 미포함  # iloc = “번호표로 찾기”


print(label6)
print()
print(label7)
print()
print(type(label6))
print(type(label7)) # 한줄이지만 범위로 뽑았으므로 데이터프레임
print()

print("----- 열 선택 -----")
print()

math1 = df['수학'] # 권장.
print(math1)
print(type(math1))
print()

eng = df.영어
print(eng)
print(type(eng))
print()

math_eng = df[['수학', '영어']]
print(math_eng)
print(type(math_eng))
print()

math2 = df[['수학']]
print(math2)
print(type(math2))
print()

print("----- 고급 슬라이싱 -----")
print()

df3 = df.iloc[0:3:2]
print(df3)
df3 = df.iloc[::2]
print(df3)
df3 = df.iloc[::-1]
print(df3)
df3 = df.iloc[0:2]
print(df3)
print()

df3 = df.iloc[0:2,0:2]
print(df3)
df3 = df.iloc[:,0:2]
print(df3)
df3 = df.iloc[0:2]
print(df3)

