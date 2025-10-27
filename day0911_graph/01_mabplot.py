import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus']= False
pd.set_option('display.width', 500)

#------------------------------------------------------------------------

df = pd.read_excel('data/시도별_전출입_인구수.xlsx')

print(df.head())
print()

df = df.ffill() 
print(df.head())
print()

# 전출지 = 서울,  전입지 = 서울빼고   --->> 서울을 나간사람들

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul = df_seoul.rename({'전입지별':'전입지'},axis=1)
df_seoul = df_seoul.set_index('전입지')
print(df_seoul)
print()

sr_one = df_seoul.loc['경기도']
print(sr_one)
print()

#--------------------------------------------------------------------------

# plt.plot(sr_one)
# plt.show()
# plt.plot(sr_one.index, sr_one.values)
# plt.show()

plt.plot(sr_one.index, sr_one.values, linestyle='dotted')
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
# plt.show()

#--------------------------------------------------------------------------

plt.figure(figsize=(14,7))
plt.plot(sr_one.index, sr_one.values, linestyle='dotted')
plt.xticks(rotation=90)
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.legend(labels=['서울 -> 경기'])
# plt.show()


#--------------------------------------------------------------------------

plt.style.use('ggplot')

plt.figure(figsize=(14,5))
plt.plot(sr_one.index, sr_one.values,
         marker='*',
         markerfacecolor='red',
         markeredgecolor='blue',
         markeredgewidth=2,
         markersize=10,
         label='서울 -> 경기')

# 엑스틱스로 로테이션 90 ,10
# 타이틀 '서울 -> 경기 인구 이동' , 사이즈 30
# 엑스축라벨 '기간' , 사이즈 20
# 와이축라벨 '이동인구수', 사이즈 20
# 볌례 폰트사이즈 15

plt.xticks(rotation='vertical', size=10)
plt.title('서울 -> 경기 인구이동', size=30)
plt.xlabel('기간', size=20)
plt.ylabel('이동 이구수', size=20)
plt.legend(fontsize=15)
# plt.show()

# 마커 종류  D d s o p > v < 1 2 3 4 x * + _ .

# bmh ggplot dark_background . . . 

# ------------------- 주석 붙이기 ---------------------------

plt.figure(figsize=(14,5))
plt.plot(sr_one.index, sr_one.values, marker='*',markeredgecolor='blue', markersize=10)
plt.xticks(rotation=70, size=10)
plt.title('서울 -> 경기 인구 이동', size=20, pad=10, color='salmon', fontweight='bold')
plt.xlabel('기간', size =20, labelpad=10, color='navy', fontweight='bold')
plt.ylabel('이동 인구수', size=20, labelpad=10,color='skyblue',fontweight='bold')
plt.legend(labels=['서울 -> 경기'], loc='best', fontsize=15)

plt.ylim(50000,800000)
# plt.xlim(0,50)

# 주석표시 화살표
plt.annotate('',
             xy=(20,620000), # 화살표 머리 
             xytext=(2,290000), # 화살표 시작
             xycoords='data', # 좌표 단위:데이터 값 기준
             arrowprops=dict(arrowstyle='->', color='skyblue', lw=5)
             ) 

plt.annotate('',
             xy=(45,470000),
             xytext=(30,600000),
             xycoords='data',
             arrowprops=dict(arrowstyle='->', color='red', lw=5)
             )
plt.annotate('인구 이동 증가(1970-1995)',
             xy =(6,390000),
             fontsize=12,
             rotation=24      
             )
             
plt.annotate('인구 이동 증가(1995-2017)',
             xy =(33,520000),
             fontsize=12,
             rotation=-11                 
             )





plt.show()



