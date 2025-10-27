import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

plt.style.use('default')

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df)
print()

#연비(mpg)와 차중(weight) 열에 대한 산점도 그리기
df.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, marker='*', figsize=(10,5))
plt.title('Scatter Plot - mpg vs. weight')
# plt.show()

plt.figure(figsize=(10,5))
plt.scatter(df['weight'],df['mpg'],c='salmon',s=10)
plt.title('Scatter Plot - mpg vs. weight')
plt.xlabel('weight')
plt.ylabel('mpg')
# plt.show()

plt.figure(figsize=(10,5))
sns.scatterplot(data=df, x='weight', y='mpg', color='coral', s=20)
plt.title('Scatter Plot - mpg vs. weight')
# plt.show()

# ------------ 버블 차트 --------------

# cylinders 개수의 상대적 비율을 계산하여 시리즈 생성 
print(df['cylinders'].unique())
cylinders_size = (df['cylinders'] / df['cylinders'].max()) * 300
print(cylinders_size)

df.plot(kind='scatter', x='weight', y='mpg', c='coral', figsize=(10,5),
        s=cylinders_size, alpha=0.3)
# s 기본값 = 20(포인트) (1포인트 = 1/72인치)
plt.title('Scatter Plot - mpg vs. weight - cylinders')
# plt.show()

# --------- 저장하기 ---------------

df.plot(kind='scatter', x='weight', y='mpg', marker = '+',   
        cmap ='plasma',c=cylinders_size, s=50, figsize=(10,5), alpha=0.3)  
# cmap='색상 팔레트'  종류 - virdis, plasma, rainbow, coolwarm, jet, ....
plt.title('Scatter Plot - mpg vs. weight - cylinders')
plt.savefig('./data/scatter.png')
plt.savefig('./data/scatter_transparent.png', transparent=True) #transparent = 투명 / 배경없애고 점/선 글자만남기는 옵션
plt.show()





