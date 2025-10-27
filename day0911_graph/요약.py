# ===============================================================
# Matplotlib / Pandas 시각화 정리
# ===============================================================

import matplotlib.pyplot as plt
import pandas as pd

# ---------------------------------------------------------------
# 1. 기본 plot
# ---------------------------------------------------------------
plt.plot([1,2,3], [4,5,6], color='blue', label='직선')
plt.title('기본 plot')        # 그래프 제목
plt.xlabel('x축')             # x축 라벨
plt.ylabel('y축')             # y축 라벨
plt.legend()                  # 범례
plt.show()

# ---------------------------------------------------------------
# 2. figure / subplots
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6,4))   # 도화지(fig) + 좌표(ax)
ax.plot(range(1,10), range(11,29,2), marker='D', label='내 그래프')
ax.set_title('엄청난') 
ax.set_xlabel('대단한 x축')
ax.set_ylabel('놀라운 y축')
ax.legend()
plt.show()

# ---------------------------------------------------------------
# 3. 여러 개 subplot
# ---------------------------------------------------------------
fig, axes = plt.subplots(2,2, figsize=(10,8))
axes[0,0].plot(range(1,10), range(11,20), marker='s')
axes[0,0].set_title('1번 그래프')
axes[0,0].legend(labels=['1번 데이터'])
plt.show()

# ---------------------------------------------------------------
# 4. pandas plot
# ---------------------------------------------------------------
# DataFrame / Series 직접 시각화 가능
s = pd.Series([4,5,6], name='score')
s.plot(marker='o', color='red', linestyle='dotted', label='연습직선')
plt.legend()
plt.show()

# df.plot(kind=...) → 범용 함수
# kind='line','bar','hist','box','scatter','pie' 등 지원
# df.boxplot() → 박스플롯 전용 함수 (옵션 더 많음)

# ---------------------------------------------------------------
# 5. 옵션 정리
# ---------------------------------------------------------------
# color = 'red'                 → 선/점 색상
# marker = 'o','s','D','*'      → 점 모양
# linestyle = '-', '--', ':'    → 선 스타일
# vert=False                    → 박스플롯 가로 회전
# sym='r+'                      → 이상치(outlier) 표시 (빨간색 + 모양)
# startangle=90                 → 파이차트 시작 각도
# autopct='%1.1f%%'             → 파이차트 퍼센트 표시
# cmap='viridis'                → 색상 팔레트 (컬러맵)
# plt.style.use('ggplot')       → 전체 스타일 변경
# plt.annotate('텍스트', xy=(x,y)) → 주석/화살표 달기
