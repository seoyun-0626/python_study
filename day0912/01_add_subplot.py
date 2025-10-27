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

# --------------- figure만 만들어 놓고 axes를 그때그때 추가하기 -----------

# fig,axes = plt.subplots(2,2, figsize=(10,8))
# axes[0,1].plot(자료,디자인)
# axes[0,1].set_title('타이틀')

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1) # 그래프 추가하게 되면 (1,2,1) 등으로 수정해야 함 

ax.plot(sr_one, marker='o', markerfacecolor='orange', markersize=5,
        color='olive', linewidth=2, label='서울->경기')

ax.legend()

#--------------------------------------------------
# y축 범위 (5만~80만)
# 타이틀 '서울 -> 경기 이동인구' 사이즈 20
# 엑스라벨 '기간', 사이즈 12
# 와이라벨 '이동인구수', 사이즈 12
# 엑스 눈금 라벨 75도 회전 

# y축 범위 설정 (5만 ~ 80만)
ax.set_ylim(50000,800000)

# 그래프 타이틀 (폰트 크기 20)
ax.set_title('서울 -> 경기 이동인구', size=20)

# x축 라벨 (폰트 크기 12)
ax.set_xlabel('기간', size=12)

# y축 라벨 (폰트 크기 12)
ax.set_ylabel('이동인구수', size=12)

# x축 눈금 위치 지정 (0부터 끝까지 5칸 간격으로)
ax.set_xticks(range(0, len(sr_one.index), 5))

# x축 눈금 라벨 지정 (sr_one 인덱스 중 5개 단위마다 표시, 75도 회전, 색상 보라색)
ax.set_xticklabels(sr_one.index[::5], rotation=75, color='magenta')

# x축 눈금 스타일 설정
# labelsize=10 → 눈금 글자 크기
# color='salmon' → 눈금선 색
# length=10 → 눈금 길이
# width=3 → 눈금 두께
ax.tick_params(axis='x', labelsize=10, color='salmon', length=10, width=3)
#------------------------------------------------

# ax2 = fig.add_subplot(1,2,2)
# ax2.plot([1,2,3],[4,5,6])

plt.show()


# ---------여러 그래프 그려보기 add_subplot-----------

# 1970~2017 문자열 리스트로 뽑아올겁니다.
col_years = list(map(str,range(1970,2018)))
df_3 = df_seoul.loc[['충청남도','경상북도','강원도'], col_years]
print(df_3.head())

fig = plt.figure(figsize=(18,5))
ax = fig.add_subplot(1,1,1)

ax.plot(col_years,df_3.loc['충청남도', :], marker='1',
        color='olive', label='서울 -> 충남')

ax.plot(col_years,df_3.loc['경상북도', :], marker='1',
        color='magenta', label='서울 -> 경북')

ax.plot(col_years,df_3.loc['강원도', :], marker='1',
        color='skyblue', label='서울 -> 강원')

ax.set_title('서울 -> 충남, 경북, 강원 인구이동' ,size=20)
ax.set_xlabel('기간',size=12)
ax.set_ylabel('이동 인구수', size=12)
# ax.set_xticks()
ax.set_xticklabels(col_years,rotation=90)
ax.tick_params(axis='x', labelsize=10, color='red')
ax.tick_params(axis='y', labelsize=10)

# x 눈금 5년단위로 
ax.set_xticks(range(0, len(col_years), 5))
ax.set_xticklabels(col_years[::5])

ax.legend()
plt.show()

#----------------- 세 지역을 시리즈로 빼네서 해보기 --------------------------

sr1 = df_seoul.loc['충청남도']
sr2 = df_seoul.loc['경상북도']
sr3 = df_seoul.loc['강원도']

fig, ax = plt.subplots(figsize=(18,5))
ax.plot(sr1)
ax.plot(sr2)
ax.plot(sr3)
ax.legend(labels=['충청남도', '경상북도', '강원도'])

ax.set_title('서울-> 충남/경북/강원 인구이동', size=20)

#--------------4분할 그래프 ----------------

col_years = list(map(str,range(1970,2018)))
df_4 = df_seoul.loc[['충청남도','경상북도','강원도','전라남도'], col_years]

plt.style.use('ggplot')

fig = plt.figure(figsize=(16,8))
plt.suptitle('전체 그래프 제목', fontsize=16)

ax1 = fig.add_subplot(2,2,1)   # (221) 이런식으로 콤마 생략가능
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.plot(col_years,df_4.loc['충청남도'], marker='*', color='olive', label='충남전입')
ax2.plot(col_years,df_4.loc['경상북도'], marker='^', color='orange', label='경북전입')
ax3.plot(col_years,df_4.loc['강원도'], marker='o', color='salmon', label='강원전입')
ax4.plot(col_years,df_4.loc['전라남도'], marker='d', color='skyblue', label='전라전입')

ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()

ax1.set_title('서울-> 충남 인구이동', size=15)
ax2.set_title('서울-> 경북 인구이동', size=15)
ax3.set_title('서울-> 강원 인구이동', size=15)
ax4.set_title('서울-> 전남 인구이동', size=15)

ax1.tick_params(axis='x', labelrotation=90)
ax2.tick_params(axis='x', labelrotation=90)
ax3.tick_params(axis='x', labelrotation=90)
ax4.tick_params(axis='x', labelrotation=90)

plt.tight_layout() 
plt.show()


