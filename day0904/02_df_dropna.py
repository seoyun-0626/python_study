import seaborn as sns

df = sns.load_dataset('titanic')

print(df.isnull().sum(axis = 0))
print()

print("------------------- 누락데이터 제거 --------------------")

print(df)

# 데이터에 널 값이 하라나도 있는 사람(행)은 데이터는 다 날라감.
df_dropna1 = df.dropna()  #axis=0
df_dropna1.info()
print()

# 데이터에 널 값이 하라나도 있는 컬럼(열)은 데이터는 다 날라감.
df_dropna2 = df.dropna(axis=1)
df_dropna2.info()
print()

# 유효한 데이터 500개 이상은 되어야 살아남음 
df_dropna3 = df.dropna(axis=1, thresh=500)
df_dropna3.info()
print()

# age가 널값이 행만 지워라.
df_age = df.dropna(subset=['age'], axis=0)
df_age.info()
print()

# age, deck 중에 하나라도 널 값이 있으면 지워라.
df_age_deck = df.dropna(subset=['age','deck'], axis=0) # how ='any'
df_age_deck.info()
print()

# age, deck 모두 널값이면 지워라 
df_age_deck = df.dropna(subset=['age','deck'], how='all', axis=0)
df_age_deck.info()
print()

print('---------------- age 널 값을 age 평균값으로 채우기 ------------')
age_mean = round(df['age'].mean(),2)

df['age'] = df['age'].fillna(age_mean)
df.info()
print()

print('--------------- embark_town (최빈값으로 대체) ------------')
print()

#숫자형의 산술정보
print(df.describe())  # 숫자형 데이터 통계 요약
print()

#문자형의 통계정보
print(df.describe(include=object)) # 문자형 데이터 통계 요약
print()

# embark_town의 고윳값별 카운트
em_freq = df['embark_town'].value_counts(dropna=True)
print(em_freq)
print()

# embark_town의 최빈값
most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
print('최빈값은 : ', most_freq)
print()

# embark_town의 최빈값
# .mode()는 시리즈의 최빈값을 시리즈로 반환 
most_freq2 = df['embark_town'].mode()
print(most_freq2)
print()

# embark_town 열을 825 행부터 830 행 조회  ##그냥 기억해보자규~


print(df['embark_town'][825:831]) # 행 번호로 슬라이싱
# 또는 loc/iloc 활용
print(df.loc[825:830, 'embark_town'])   # loc → 끝 인덱스 포함
print(df.iloc[825:831]['embark_town']) # iloc → 끝 인덱스 제외
print()

#위에 내용 사람마다 다르게 뽑았네?
df_et = df['embark_town'].iloc[825:831]
print(df_et)
print(type(df_et))
print()

df_et1 = df.iloc[820:831]
print(df_et1)
print(type(df_et1))
print()

df_et2 = df.loc[825:830, 'embark_town']
print(df_et2)
print(type(df_et2))
print()

df_et3 = df['embark_town'][820:831]
print(df_et3)
print(type(df_et3))
print()

df_et4 = df.iloc[820:830]['embark_town']
print(df_et4)
print(type(df_et4))
print()

# embark_town 열의 NaN 값을 최빈값으로 채워넣기
df['embark_town'] = df['embark_town'].fillna(most_freq)
df['embarked'] = df['embark_town'].fillna('S') # 채우는김에 같이 채워봄.
df.info()
print()

# 채워 넣고 나서 다시 조회 해보기
df_et3 = df['embark_town'][825:831]
print(df_et3)
print()

print('------------근처 값으로 대체 ---------------')
print()

df = sns.load_dataset('titanic')

# 데이터프레임 복제하기
df2 = df.copy()

print(df['embark_town'][825:831])
print()

# 이전행 (828) 값으로 채워라
df['embark_town'] = df['embark_town'].ffill()
print(df['embark_town'][825:831])
print()

# 이후행 (830) 값으로 채워라
df2['embark_town'] = df2['embark_town'].bfill()
print(df2['embark_town'][825:831])
print()

