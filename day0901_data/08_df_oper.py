import pandas as pd
import seaborn as sns
pd.set_option('display.unicode.east_asian_width',True)
pd.set_option('display.max_column', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

# 타이타닉 데이터 불러오기

titanic = sns.load_dataset('titanic')
print(titanic.head(100))
titanic.info()


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

df = titanic.loc[:,['age','fare']]
print(df)
print()
print(df.head(10))
print()

print("----- 데이터 프레임에 숫자 연산 -----")
print()

addition = df + 10
print(addition.head())

print("----- 데이터프레임끼리 연산 -----")
print()

print(df.tail())
print()
print(addition.tail())
print()

subtraction = df - addition
print(subtraction.tail())
print()

# nan 값 채우기
sample1 = subtraction.tail().fillna(0)
print()
print(sample1)
print()
sample1.info()

print(df.tail())
print()
print(addition.tail())
print()

# 양 쪽 모두 Nan 이어서 fill_value 안됨.
sample2 = df.sub(addition, fill_value =0)
print(sample2.tail())
print()

print(titanic.head())
print()
titanic.info()
titanic['age'] = titanic['age'].fillna(0)
print()
titanic.info()

