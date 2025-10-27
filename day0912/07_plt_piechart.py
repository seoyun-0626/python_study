import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/auto-mpg.csv',header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

plt.style.use('default')

print(df)
print()

df['count'] = 1
print(df)
print()

df_origin = df.groupby('origin').sum(numeric_only=True)  # sum(numeric_only=True) -->>숫자형 컬럼만 합계 내라
print(df_origin)
print()

df_origin.index = ['USA', 'EU', 'JAPAN']
print(df_origin)
print()

print('나는 %d 살 입니다.' %23)
df_origin['count'].plot(kind='pie', figsize=(7,5), autopct='%1.1f%%',
                        startangle=90,
                        colors=['chocolate','bisque','cadetblue'])
plt.title('Model Origin', size=20)
plt.legend(labels=df_origin.index)
plt.show()
