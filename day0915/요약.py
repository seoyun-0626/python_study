import seaborn as sns
import matplotlib.pyplot as plt

# ======================
# 📌 기본 설정
# ======================
sns.set_style('darkgrid')  # 스타일: white, whitegrid, dark, darkgrid, ticks

# ======================
# 📌 Subplot 만들기
# ======================
# 1) 단순 행렬 배치
fig, axes = plt.subplots(1,2, figsize=(10,5))  # axes[0], axes[1] 접근
# 2) 자유 배치 (mosaic)
fig, axes = plt.subplot_mosaic(
    [['top_left','top_right'],
     ['bottom_left','bottom_right']],
    figsize=(12,6), constrained_layout=True
)
# axes['top_left'] 이런 식으로 접근

# ======================
# 📌 산점도 / 회귀선(추세선)
# ======================
sns.regplot(x='age', y='fare', data=titanic, ax=axes[0])       # 회귀선 포함
sns.regplot(x='age', y='fare', data=titanic, fit_reg=False)    # 회귀선 제거
sns.scatterplot(x='age', y='fare', hue='sex', data=titanic)    # 그룹별 색상

# ======================
# 📌 히스토그램 (histplot)
# ======================
sns.histplot(x='age', data=titanic, bins=10)                           # 기본
sns.histplot(x='age', hue='survived', data=titanic)                    # 그룹별
sns.histplot(x='age', hue='survived', multiple='dodge', data=titanic)  # 나란히
sns.histplot(x='age', hue='survived', multiple='stack', data=titanic)  # 쌓기
sns.histplot(x='age', hue='survived', multiple='fill', bins=10, data=titanic) # 비율

# ======================
# 📌 커널 밀도 (KDE plot)
# ======================
sns.kdeplot(x='age', data=titanic)                                       # 기본
sns.kdeplot(x='age', hue='survived', data=titanic)                       # 그룹별
sns.kdeplot(x='age', hue='survived', fill=True, data=titanic)            # 색 채우기
sns.kdeplot(x='age', hue='survived', multiple='stack', data=titanic)     # 쌓기
sns.kdeplot(x='age', hue='survived', multiple='fill', bw_adjust=2.0, data=titanic) # 비율+스무딩

# ======================
# 📌 제목/레이아웃
# ======================
fig.suptitle('Titanic - Age Distribution')   # 전체 제목
axes['top_left'].set_title("Histogram")      # 개별 제목
plt.tight_layout()                           # 자동 여백 조정
plt.show()


'''
📌 Seaborn에서 지금까지 정리한 핵심

1.스타일 설정

sns.set_style('darkgrid') : 그래프 기본 배경/격자 설정


2.subplot 관리

plt.subplots() : 배열 인덱스로 접근 (axes[0], axes[1])

plt.subplot_mosaic() : 이름 붙여서 딕셔너리로 접근 (axes['top_left'])


3.산점도 & 회귀선

sns.scatterplot() : 분포 확인, 그룹별 색/모양/크기

sns.regplot() : 산점도 + 추세선 (fit_reg, ci, order 옵션 기억)


4.히스토그램 (histplot)

bins : 구간 개수

hue, multiple(dodge/stack/fill) → 그룹 비교

palette, element, kde=True 등 옵션


5.커널 밀도 (kdeplot)

히스토그램의 매끄러운 곡선 버전

fill=True, multiple(stack/fill), bw_adjust(곡선 부드럽기)


6.제목/레이아웃

fig.suptitle() : 전체 제목

axes.set_title() : subplot 제목

plt.tight_layout() / constrained_layout=True : 여백 자동 조정

'''