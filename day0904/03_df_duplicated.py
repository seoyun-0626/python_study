import pandas as pd

df = pd.DataFrame({'c1':['a','a','b','a','b',],
                   'c2':[1,1,1,2,2],
                   'c3':[1,1,2,2,2]})

print(df)
print()

print("-------------- 중복데이터 확인 -----------------")
print()

# 데이터 프레임 전체 행 중에서 중복값 찾기
df_dup_first = df.duplicated()  # 디폴트옵션 keep ='first'
print(df_dup_first)
print()

# 데이터 프레임 전체 행 중에서 중복값 찾기 (keep='last') 
df_dup_last = df.duplicated(keep='last') 
print(df_dup_last)
print()

# 데이터 프레임 전체 행 중에서 중복값 찾기 (keep='False') 
df_dup_False = df.duplicated(keep=False) 
print(df_dup_False)
print()

# 데이터프레임의 특정 컬럼 데이터에서 중복값 찾기
col_dup = df['c2'].duplicated()
print(col_dup)
print()

# 데이터프레임의 특정 컬럼 데이터에서 중복값 찾기
col_dup2 = df.duplicated(subset=['c2'])
print(col_dup2)
print()

# 데이터프레임의 여러 컬럼 데이터에서 중복값 찾기
col_dup3 = df.duplicated(subset=['c2','c3'])
print(col_dup3)
print()

'''
    c1  c2  c3
0   a   1   1
1   a   1   1
2   b   1   2
3   a   2   2
4   b   2   2  

'''

print("-------중복데이터 제거 -----------")
print()

print(df)
print()

# 데이터프레임에서 중복 행을 
df2 = df.drop_duplicates()  #(기본값, keep='first')
print(df2)
print()

df3 = df.drop_duplicates(keep='last')  
print(df3)
print()

df4 = df.drop_duplicates(keep=False) # 중복값 다 제거
print(df4)
print()

df5 = df.drop_duplicates(subset=['c2', 'c3']) # c2,c3 기준으로 중복 행 제거
print(df5)
print()

df6 = df.drop_duplicates(subset=['c2','c3'],keep=False) # c2,c3기준으로 중복값 다날려 
print(df6)
print()




