import pandas as pd

df = pd.read_csv('./data/stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date'])
df = df.drop(columns=['Date'])
df = df.set_index('new_Date').sort_index()

ts = df.head(10)
print(ts)

# ----------------------------------------------------------------

print(ts.shift(1))
print()

print(ts.shift(-2))
print()

print(ts.shift(3, freq="D"))   # 날짜에 3일씩 더해짐 
print()

print(ts.asfreq('5D'))  # 5일단위로 보겠다.
print()

print(ts.asfreq('5D', method='bfill'))
print()

# Resampling
print(ts.resample('3B')) #영업일 기준이므로 주말은 제외하게됨 
print()
print(type(df.index))

print("3영업일 합계")
print(ts.resample("3B").sum())
print()
print("3영업일 평균")
print(ts.resample("3B").mean())
print()
print("3영업일 중앙값 ")
print(ts.resample("3B").median())
# min,max,count...

print(ts.rolling(window=3).sum())
print()
print(ts.rolling(window='3D').sum())






