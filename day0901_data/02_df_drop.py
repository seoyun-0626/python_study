# 데이터 프레임 == 이차원 자료구조 == 엑셀같은.
# 데이터프레임의 각 열은 각각 시리즈 객체이다.
# 행(row),  열(column), 

import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

print("----- 딕셔너리를 데이터프레임으로 -----")
print()

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9]}

df = pd.DataFrame(dict_data)

print(type(df))
print(df)
print()

print("----- 이중 리스트를 데이터프레임으로 -----")
print()

df2 = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']])
print(df2)
print()

df2 = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                   index=['준서', '예은'],
                   columns=['나이', '성별', '학교'])
print(df2)
print()

print(df2.index)
print(df2.columns)
print()

df2.index=['학생1', '학생2']
df2.columns=['연령', '남녀', '소속'] 
print(df2)
print()

print('-------- rename ---------')
print()

# 새로운 이름의 변수에 담아서 사용 
# df2_rename1 = df2.rename(columns={'연령':'age', '남녀':'gender', '소속':'school'})
# print(df2_rename1)

# 원래 변수에 덮어 씌어서 사용 
# df2 = df2.rename(columns={'연령':'age', '남녀':'gender', '소속':'school'})
df2.rename(columns={'연령':'age', '남녀':'gender', '소속':'school'}, inplace=True)
print(df2)
print()

df2.rename(index={'학생1':'김학생'}, inplace=True)
print(df2)
print()

print('-------- drop ---------')
print()

exam_data = {'수학':[90, 80, 70], '영어':[88, 77, 66], '음악':[30, 40, 50]}

df = pd.DataFrame(exam_data, index=['철수', '영희', '미진'])
print(df)

print('-------- drop / 행삭제---------')
print()

df1 = df.drop('미진') # inplace = True 가능
print(df1)
print()

df2 = df.drop(['철수', '미진'])
print(df2)
print()

df3 = df.drop('철수', axis=0)   # 0 행 / 1 열
print(df3)
print()

df4 = df.drop('철수', axis='index')
print(df4)
print()

df5 = df.drop(index=['철수'])
print(df5)
print()

print('-------- drop / 열삭제 ---------')
print()

print(df)
print()

df2 = df.drop('수학', axis=1)
print(df2)
print()

df3 = df.drop(['수학', '영어'], axis=1)
print(df3)
print()

print(df3.ndim)
print(type(df3))
print()

df4 = df.drop('수학', axis='columns')
print(df4)
print()

df5 = df.drop(columns=['수학'])
print(df5)
print()


