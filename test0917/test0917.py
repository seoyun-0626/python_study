import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus']= False

#--------------------------------------------------------------------------------

# CSV 불러오기
df_all = pd.read_csv('C:/Users/admin/OneDrive/바탕 화면/python1/data/apartment_2015_2025_clean.csv')

# 데이터 기본 확인
print(df_all.head())
print('==========정보=============')
print(df_all.info())

# 컬럼별 결측치 개수
print("\n=====컬럼별 결측치 개수=====")
print(df_all.isnull().sum())

df_all['연도'] = df_all['계약년월'].astype(str).str[:4].astype(int)

def get_city(x):
    if "서울특별시" in x: return "서울"
    elif "인천광역시" in x: return "인천"
    elif "경기도" in x: return "경기"
    elif "부산광역시" in x: return "부산"
    else: return "기타"

df_all['지역'] = df_all['시군구'].apply(get_city)

counts = df_all['지역'].value_counts()
print("=====지역별 거래건수======")
print(counts)

# 연도 + 지역별 평균 거래금액 집계
yearly_avg = df_all.groupby(['연도','지역'])['거래금액(만원)'].mean().reset_index()

print("=====연도 + 지역별 평균 거래금액 집계=====")
print(yearly_avg)
print()

# 서울, 인천, 경기, 부산 각각 라인그래프

plt.figure(figsize=(15,10))

# 서울
plt.subplot(3,2,1)
seoul = yearly_avg[yearly_avg['지역']=='서울']
sns.lineplot(data=seoul, x='연도', y='거래금액(만원)', marker='o')
plt.title("서울 아파트 평균 거래금액 추이 (2015~2025)")
plt.ylabel("거래금액(만원)")
plt.grid(True, linestyle='--', alpha=0.6)

# 인천
plt.subplot(3,2,2)
incheon = yearly_avg[yearly_avg['지역']=='인천']
sns.lineplot(data=incheon, x='연도', y='거래금액(만원)', marker='o')
plt.title("인천 아파트 평균 거래금액 추이 (2015~2025)")
plt.ylabel("거래금액(만원)")
plt.grid(True, linestyle='--', alpha=0.6)

# 경기
plt.subplot(3,2,3)
gyeonggi = yearly_avg[yearly_avg['지역']=='경기']
sns.lineplot(data=gyeonggi, x='연도', y='거래금액(만원)', marker='o')
plt.title("경기 아파트 평균 거래금액 추이 (2015~2025)")
plt.ylabel("거래금액(만원)")
plt.grid(True, linestyle='--', alpha=0.6)

# 부산
plt.subplot(3,2,4)
busan = yearly_avg[yearly_avg['지역']=='부산']
sns.lineplot(data=busan, x='연도', y='거래금액(만원)', marker='o')
plt.title("부산 아파트 평균 거래금액 추이 (2015~2025)")
plt.ylabel("거래금액(만원)")
plt.grid(True, linestyle='--', alpha=0.6)

# 기타
plt.subplot(3,2,5)
etc = yearly_avg[yearly_avg['지역']=='기타']
sns.lineplot(data=etc, x='연도', y='거래금액(만원)', marker='o')
plt.title("기타 아파트 평균 거래금액 추이 (2015~2025)")
plt.ylabel("거래금액(만원)")
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()

# 한 그래프에 전체 변화 담아보기 

plt.figure(figsize=(12,6))

sns.lineplot(data=yearly_avg, x='연도', y='거래금액(만원)', hue='지역', marker='o')

plt.title("2015~2025 지역별 아파트 평균 거래금액 추이", fontsize=14)
plt.ylabel("평균 거래금액(만원)")
plt.xlabel("연도")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title="지역")
plt.show()

# # 2015년 vs 2025년 평균 비교
df_2015 = df_all[df_all['연도'] == 2015]
df_2025 = df_all[df_all['연도'] == 2025]

print('========2015')
print(df_2015.head())
print('========2025')
print(df_2025.head())
print()

# 지역별 평균 계산
avg_2015 = df_2015.groupby('지역')['거래금액(만원)'].mean()
avg_2025 = df_2025.groupby('지역')['거래금액(만원)'].mean()

print('=======지역평균2015')
print(avg_2015)
print('=======지역평균2025')
print(avg_2025)

# 합치기
avg_compare = pd.concat([avg_2015, avg_2025], axis=1)
avg_compare.columns = ['2015년', '2025년']

# 상승률 
avg_compare['상승률(%)'] = ((avg_compare['2025년'] - avg_compare['2015년']) / avg_compare['2015년']) * 100

print("=======상승률=========")
print(avg_compare)

# 상승률 그래프
avg_compare['상승률(%)'].plot(kind='bar', figsize=(10,6), color='orange')

plt.title("2015 → 2025 지역별 아파트 평균 거래금액 상승률", fontsize=14)
plt.ylabel("상승률(%)")
plt.xlabel("지역")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

ax = avg_compare[['2015년','2025년']].plot(kind='bar', figsize=(10,6))

plt.title("2015년 vs 2025년 지역별 평균 아파트 거래금액 비교", fontsize=14)
plt.ylabel("평균 거래금액(만원)")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title="연도")

# 상승률 텍스트 표시
for i, (idx, row) in enumerate(avg_compare.iterrows()):
    # 막대 두 개의 중간 위치에 텍스트 배치
    # enumerate(avg_compare.iterrows())는 **"avg_compare의 각 행을 돌리면서, 막대 위치(i)와 데이터(row)를 동시에 얻는 코드"**야.
    x_pos = i
    y_pos = max(row['2015년'], row['2025년']) + 2000  # 막대보다 살짝 위
    plt.text(x_pos, y_pos, f"{row['상승률(%)']:.1f}%", 
             ha='center', va='bottom', fontsize=10, color="red")
print(df_all['거래금액(만원)'].max())



plt.show()

