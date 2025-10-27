import pandas as pd

data = {'name' : [ 'Jerry', 'Riah', 'Paul'],
        'algol' : [ 'A', 'A+', 'B'],
        'baisc' : [ 'C', 'B', 'B+'],
        'c++' : [ 'B+', 'C', 'C+']}

df = pd.DataFrame(data)
print(df)
print()

df = df.set_index('name')
print(df)
print()

print("-------- CSV로 저장하기 --------")
print()

df.to_csv("./data/df_sample.csv")      # df_sample.csv 이 이름으로 저장하겠다는거임 
print("df_smaple.csv 저장완료")
print()

print("-------- JSON로 저장하기 --------")
print()

df.to_json("./data/df_sample.json")
print("df_sample.json 저장완료")
print()

# 인덱스, 컬럼, 데이터로 분리 저장
df.to_json("./data/df_sample_split.json", orient='split')
print("df_sample_split.json 저장완료")
print()

# 각 행을 별도의 객체(딕셔너리)로 저장, 열 이름이 키로
df.to_json("./data/df_sample_records.json", orient='records')
print("df_sample_records.json 저장완료")
print()

# 각 행의 인덱스를 키로 
df.to_json("./data/df_sample_index.json", orient='index')
print("df_sample_index.json 저장완료")
print()

# 각 열의 인덱스를 키로
df.to_json("./data/df_sample_columns.json", orient='columns')
print("df_sample_columns.json 저장완료")
print()

# 밸류만 순서대로 저장 
df.to_json("./data/df_sample_values.json", orient='values')
print("df_sample_values.json 저장완료")
print()

print("-------- Excel로 저장하기 --------")
print()

df.to_excel("./data/df_sample.xlsx")
print("df_sample.xlsx 저장완료")
print()

df.to_excel("./data/df_sample_no_index.xlsx", index=False)
print("df_sample_no_index.xlsx 저장완료")
print()

print("-------- Excel 여러시트 저장하기 --------")
print()

data1 = {'name' : [ 'Jerry', 'Riah', 'Paul'],
        'algol' : [ 'A', 'A+', 'B'],
        'baisc' : [ 'C', 'B', 'B+'],
        'c++' : [ 'B+', 'C', 'C+']}

data2 = {'c0':[1, 2, 3],
         'c1':[4, 5, 6],
         'c2':[7, 8, 9],
         'c3':[10, 11, 12]}

df1 = pd.DataFrame(data1)
df1 = df1.set_index('name')

df2 = pd.DataFrame(data2)
df2 = df2.set_index('c0')

print(df1)
print()
print(df2)
print()

with pd.ExcelWriter("./data/df_excelwriter.xlsx")as my_writer:
    df1.to_excel(my_writer, sheet_name="grade")
    df2.to_excel(my_writer, sheet_name="numbers")

    