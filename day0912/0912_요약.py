# ===============================================================
# Matplotlib & Pandas 시각화 정리
# ===============================================================

import matplotlib.pyplot as plt
import pandas as pd


from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus']= False  ## 폰트매니저 부터 한글보이게 하기위한거 

# ---------------------------------------------------------------
# 1. 기본 plot (선 그래프)
# ---------------------------------------------------------------
plt.plot([1,2,3],[4,5,6], color='blue', marker='o', linestyle='--', label='직선')  
# color='blue'  → 선 색상
# marker='o'    → 점 모양 (o, s, D, *, + ...)
# linestyle='--'→ 선 스타일 ('-', '--', ':', '-.')
# label='직선'  → 범례 이름
plt.title('그래프 제목')   # 그래프 제목
plt.xlabel('x축 라벨')    # x축 라벨
plt.ylabel('y축 라벨')    # y축 라벨
plt.legend()              # 범례 표시
plt.show()

# ---------------------------------------------------------------
# 2. Figure / Axes
# ---------------------------------------------------------------
fig = plt.figure(figsize=(10,5))      # 도화지(figure) 생성
ax = fig.add_subplot(1,1,1)           # 1행 1열 중 첫 번째 subplot
ax.plot([1,2,3],[4,5,6], marker='o')  # 좌표축(ax)에 그래프 그리기
plt.show()

# ---------------------------------------------------------------
# 3. Subplots (여러 그래프 한 화면에)
# ---------------------------------------------------------------
fig, axes = plt.subplots(2,2, figsize=(10,8))   # 2행 2열 서브플롯 생성
axes[0,0].plot([1,2,3],[4,5,6])                 # [0,0] 위치에 그래프
axes[0,0].set_title("첫번째 그래프")             # 그래프 제목
plt.tight_layout()                              # 겹치지 않게 자동 조정
plt.show()

# ---------------------------------------------------------------
# 4. Pandas plot 사용하기
# ---------------------------------------------------------------
df = pd.read_csv('./data/auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 히스토그램 (연비 분포)
df['mpg'].plot(kind='hist', bins=10, color='coral', figsize=(8,5))
plt.title('Histogram')
plt.xlabel('mpg')
plt.show()

# 산점도 (연비 vs 차중)
df.plot(kind='scatter', x='weight', y='mpg', c='coral', s=20, marker='*', figsize=(8,5))
plt.title('Scatter Plot - mpg vs. weight')
plt.show()

# ---------------------------------------------------------------
# 5. 스타일 / 옵션
# ---------------------------------------------------------------
plt.style.use('ggplot')  # 전체 스타일 테마 변경 (bmh, dark_background, classic...)

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(df['mpg'], color='olive', label='연비')

ax.set_title('제목', size=20)       # 제목 + 크기
ax.set_xlabel('기간', size=12)      # x축 라벨
ax.set_ylabel('이동 인구수', size=12) # y축 라벨

ax.set_xticks(range(0,len(df),50))                  # 눈금 위치
ax.set_xticklabels(df.index[::50], rotation=75)     # 눈금 라벨 (75도 회전)
ax.tick_params(axis='x', labelsize=10, color='red') # 눈금 스타일
ax.legend()
plt.show()

# ---------------------------------------------------------------
# 6. 주석 / 화살표 달기
# ---------------------------------------------------------------
plt.plot([1,2,3],[3,2,5], marker='o')
plt.annotate('여기!', xy=(2,2), xytext=(1,4), 
             arrowprops=dict(arrowstyle='->', color='red'))
plt.show()

# ---------------------------------------------------------------
# 7. 원그래프 (Pie chart)
# ---------------------------------------------------------------
df['count'] = 1
df_origin = df.groupby('origin').sum(numeric_only=True)
df_origin.index = ['USA','EU','JAPAN']

df_origin['count'].plot(kind='pie',
                        autopct='%1.1f%%',        # 퍼센트 표시
                        startangle=90,            # 시작 각도
                        colors=['chocolate','bisque','cadetblue'], # 색상 지정
                        figsize=(6,6))
plt.title('Model Origin', size=20)
plt.ylabel('')   # y축 라벨 제거
plt.show()

# ---------------------------------------------------------------
# 8. 박스플롯 (Boxplot)
# ---------------------------------------------------------------
color = {
    'boxes':'SeaGreen',   # 박스 테두리
    'whiskers':'Olive',   # 수염(꼬리)
    'medians':'red',      # 중앙선
    'caps':'blue'         # 위아래 캡
}

df.plot(kind='box', column=['mpg'], by='origin',
        color=color, sym='r+', vert=False, figsize=(8,5))
# sym='r+' → 이상치(outlier)를 빨간 + 표시
# vert=False → 가로 박스플롯
plt.title('Boxplot - MPG by Origin')
plt.show()

# ---------------------------------------------------------------
# 9. 누적 영역 / 스택 그래프
# ---------------------------------------------------------------
col_years = list(map(str, range(2010,2018)))
df_seoul = pd.read_excel('./data/시도별_전출입_인구수.xlsx')
df_seoul = df_seoul.ffill()
mask = (df_seoul['전출지별']=='서울특별시') & (df_seoul['전입지별']!='서울특별시')
df_seoul = df_seoul[mask].drop(['전출지별'], axis=1).rename({'전입지별':'전입지'},axis=1).set_index('전입지')
df_4 = df_seoul.loc[['충청남도','경상북도','강원도','전라남도'], col_years].T.astype(int)

df_4.plot(kind='area', stacked=True, alpha=0.2, figsize=(10,5))
plt.title('서울 -> 타도시 인구이동', size=20)
plt.ylabel('이동 인구수', size=15)
plt.xlabel('기간', size=15)
plt.legend(fontsize=12)
plt.show()

# ---------------------------------------------------------------
# 10. 저장하기
# ---------------------------------------------------------------
plt.scatter(df['weight'], df['mpg'], c='salmon', s=10)
plt.title('Scatter 저장 예시')

plt.savefig('./data/scatter.png', dpi=300)  # 해상도 높게 저장
plt.savefig('./data/scatter_transparent.png', transparent=True) 
# transparent=True → 배경 투명 저장
plt.show()
