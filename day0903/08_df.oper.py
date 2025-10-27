import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width',300)
pd.set_option('display.max_rows',100)

# survived      : 생존 여부 (0=사망, 1=생존)                [int64]
# pclass        : 선실 등급 (1등석, 2등석, 3등석)            [int64]
# sex           : 성별 (male, female)                       [object]
# age           : 나이 (결측치 있음, 소수점 포함 가능)       [float64]
# sibsp         : 함께 탑승한 형제/자매 + 배우자 수          [int64]
# parch         : 함께 탑승한 부모 + 자녀 수                 [int64]
# fare          : 운임 요금                                  [float64]
# embarked      : 승선 항구 (C=셰르부르, Q=퀸스타운, S=사우샘프턴) [object]
# class         : 선실 등급 (First, Second, Third)          [category]
# who           : 인물 구분 (man=남자, woman=여자, child=아이) [object]
# adult_male    : 성인 남성 여부 (True/False)               [bool]
# deck          : 선실 갑판(Deck) 위치 (A~G, 결측치 많음)   [category]
# embark_town   : 탑승 도시 이름 (Cherbourg, Queenstown, Southampton) [object]
# alive         : 생존 여부 (yes/no)                        [object]
# alone         : 혼자 탑승 여부 (True/False)               [bool]


'''
타이타닉 로드하기 (시본)
데이터 구조 확인하기
승객의 평균 나이, 평균 요금
age 결측지를 age의 평균으로 채워보시고
deck 컬럼제거
age, parch, class 열만 선택하여 보기
FamiliySize라는 컬럼에 sibsp + parch + 자기자신 (로 해서 총 가족 인원수 컬럼 만들어보기)
IsChild 라는 True/False 컬럼 만들어보기 ( 13 살 미만 )
남성과 여성의 평균 나이비교
선생님 터미널 결과처럼 id라는 이름으로 정수 인덱스 설정하기 
하고싶은 분석 해보기
'''

print("---타이타닉 데이터 로드하기----- ")
print()
df = sns.load_dataset('titanic')  
print() 

print("---데이터 구조 확인----- ")
print()
print(df.head(10))
df.info()
print(df.tail(10))
print(df.describe())
print()

print("---승객의 평균 나이,평균 요금----- ")
print()
print("평균나이:",df['age'].mean().round(2), 'years old')
print("평균요금:",df['fare'].mean().round(2), 'USD')
# 80세 노인분 생존여부 
print(df[df['age'] == 80])
print()

print("---age 결측지를 age의 평균으로 채워보시고----- ")
print()
df['age'] = df['age'].fillna(df['age'].mean())
df.info()
print()

print("---deck 컬럼제거----- ")
print()
df = df.drop('deck', axis =1)
print()

print("---age, parch, class 열만 선택하여 보기----- ")
print()
print(df[['age', 'parch','class']].head(10))    #여러개 선택하려면 이중리스트 
print()

#age, parch, class 열만 선택하여 랜덤추출
print(df[['age', 'parch','class']].sample(10))
print()

print("---FamiliySize라는 컬럼에 sibsp + parch + 자기자신 (로 해서 총 가족 인원수 컬럼 만들어보기)----- ")  #각 승객기준이라서 +1인거임 
print()
df['FamiliSize'] = df['sibsp'] + df['parch'] + 1
print(df.head(10))
print()

print("---IsChild 라는 True/False 컬럼 만들어보기 ( 13 살 미만 )----- ")
print()
df['IsChild'] = df['age']< 13
print(df['IsChild'])
print(df['age'] < 13)

print("---남성과 여성의 평균 나이비교----- ")
print()
# 불타입의 시리즈를 데이터 [] 에 넣으면 True에 해당하는 데이터만 필터링 
male_mean= df[df['sex'] == 'male']['age'].mean().round(2)
female_mean = round(df[df['sex'] == 'female']['age'].mean(),2)

print("남성 평균 나이:", male_mean)
print("여성 평균 나이:", female_mean)
print()


print("---id라는 이름으로 정수 인덱스 설정하기 ----- ")
print()

df.index.name = "-id-"
print(df)
print()
df = df.reset_index(names = 'id')
print(df)
print()
df = df.set_index('id')
print(df)









