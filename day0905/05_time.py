import pandas as pd

df = pd.read_csv('./data/stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date'])
print(df)

# 정렬
df = df.sort_values(by='Date', ascending=True)
print(df)
df= df.drop('Date', axis=1)
df = df.set_index('new_Date')  
print(df)
print(df.index)
print()

# 부분 문자열 인덱싱
print(df.loc['2018-06-27'])
print()

# 부분 문자열 인덱싱2
print(df.loc['2018-06'])
print()

# 부분 문자열 인덱싱3
print(df.loc['2018-06-27' : '2018-07-02'])
print() 

# 부분 문자열 인덱싱4
print(df[df.index < '2018-06-05'])
print() 

# 시간 자료형을 활용한 인덱싱
print(df.loc[pd.Timestamp(2018, 6, 5): pd.Timestamp(2018,7,6)])
print()

# 시간 자료형을 활용한 인덱싱2
print(df.loc[pd.Timestamp(2018, 6, 5, 10, 30, 0): pd.Timestamp(2018, 7, 6, 23, 59, 59)])
print()

print()
print('-----------------------------------------------------------------------------------------------')
print()

# 날짜와 시간 간격을 표현하는 pandas.Timedelta 객체

print(pd.Timedelta('1 days'))
print(pd.Timedelta(days=1))
print(pd.Timedelta('1 days 1 hours 1 minutes 1 seconds'))
print(pd.Timedelta(days=1, hours=1, seconds=1))
print()

print(pd.to_timedelta(['1 days', '3 hours', '10minutes']))

print()
a = df.index
print(a)

b = pd.Timestamp('2018-07-03') - a
print(b)
print()

#하루씩 더함.(Timedelta : 시간을 더하고 뺄때)
c = a + pd.Timedelta(days=1)
print(c)

print(c.min())
print(c.max())

