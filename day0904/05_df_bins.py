from cProfile import label
import pandas as pd
import numpy as np
pd.set_option('display.unicode.east_asian_width', True)  # 한글 칼럼 맞춤
pd.set_option('display.colheader_justify', 'center')     # 헤더 중앙 정렬



df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# horsepower 열의 누락데이터('?') nan 으로 바꾼뒤 drop 한 다음, 
# horsepower 열의 타입을 float 으로 변환!!!

df['horsepower'] = df['horsepower'].replace('?',np.nan)
df = df.dropna(subset=['horsepower'],axis=0)
df['horsepower'] = df['horsepower'].astype('float')

df.info()
print()
print(df.head(50))
print()

print("--------------- horsepower구간 나누기 ----------------")
print()

# 각 구간에 속하는 데이터 개수(count), 경계값 리스트(bin_dividers) 반환
# ex)   bins = 3 으로 하면 세 구간으로 균등 분할 

count,bin_dividers = np.histogram(df['horsepower'], bins=[0,100,200,300])
print(bin_dividers)
print()
print(count)
print()
print(df.describe())

bin_names = ['저출력', '보통출력', '고출력']
print()

# pd.cut 함수로 각 데이터를 3개의 bin에 할당
df['hp_bin'] = pd.cut(x=df['horsepower'],
                      bins=bin_dividers,
                      labels= bin_names,
                      include_lowest=True)
print(df.head(10))



#----------------- 더미변수 ---------------------

# hb_bin 컬럼의 볌주형 데이터를 더미 변수로 변환 
horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15))
print(type(horsepower_dummies))
print()

# hb_bin 컬럼의 볌주형 데이터를 더미 변수로 변환 (float)
horsepower_dummies = pd.get_dummies(df['hp_bin'], dtype=float)
print(horsepower_dummies.head(15))
print()

horsepower_dummies_drop = pd.get_dummies(df['hp_bin'], dtype=float,
                                         drop_first=True)
print(horsepower_dummies_drop.head(15))
print()

#----------------------------------------------------------------

# sklearn 라이브러리 불러오기
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
onehot_encoder = preprocessing.OneHotEncoder(sparse_output=False)

# label encoder로 문자열 범주를 숫자형 범주로 변환

onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15))
print(onehot_labeled)
print(type(onehot_labeled))

# 2차원 행렬로 형태 변경
onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled),1)
print(onehot_reshaped)
print(type(onehot_reshaped))
print()

onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted) # 희소행렬 반환
print()
# print(onehot_fitted.toarray())
print()

# OneHotEncoder(sparse_output=False) 옵션을 주면 바로 어레이로 반환 
encoded_df = pd.DataFrame(onehot_fitted, columns=onehot_encoder.get_feature_names_out(df[['hp_bin']].columns))
print(encoded_df)
print()







