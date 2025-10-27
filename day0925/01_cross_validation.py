'''
❤ 교차 검증 (Cross Validation, CV)

- 데이터를 여러 개 fold로 나눠서 번갈아가며 훈련/검증
- 데이터 나누는 운에 따라 성능이 달라지는 걸 줄여줌

👉 쉽게 말하면:
시험 볼 때 문제지를 여러 버전으로 돌려가면서 평균 점수 내는 거랑 비슷.

'''

import pandas as pd

wine = pd.read_csv('https://bit.ly/wine_csv_data')

print(wine.head())
wine.info()
print()
print(wine.describe())
print()

data = wine[['alcohol','sugar','pH']]
target = wine['class']
print(target.unique())

from sklearn.model_selection import train_test_split

# 훈련 - 테스트 나누기 
train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)

# 훈련셋 >> 훈련 - 검증 나누기 
sub_input, val_input, sub_target, val_target= train_test_split(
    data, target, test_size=0.2, random_state=42)

print('훈련-검증 세트 크기')
print(sub_input.shape, val_input.shape)

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42)
dt.fit(sub_input, sub_target)

print('훈련/검증 스코어')
print(dt.score(sub_input, sub_target))
print(dt.score(val_input, val_target))

# ----------------- 교차검증  ---------------------

from sklearn.model_selection import cross_validate

scores = cross_validate(dt, train_input, train_target)
print(scores)
'''
{'fit_time': array([0.00528407, 0.00514531, 0.00556469, 0.00552797, 0.005481  ]), 
'score_time': array([0.00111747, 0.00133824, 0.00122666, 0.00141883, 0.00173163]), 
'test_score': array([0.86923077, 0.84615385, 0.87680462, 0.84889317, 0.83541867])}

fit_time = 훈련 시간
score_time = 평가 시간
test_score = 각 검증 세트에서의 성능 점수
'''

import numpy as np

print('교차검증 평균 스코어')
print(np.mean(scores['test_score']))

from sklearn.model_selection import StratifiedKFold

# 분류 디폴트 = cv=cv=StratifiedKFold(), 회귀 모델KFold
scores = cross_validate(dt, train_input, train_target, cv=StratifiedKFold())

print(np.mean(scores['test_score']))

# StratifiedKFold 옵션 설정
splitter = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
scores = cross_validate(dt, train_input, train_target, cv=splitter)
print(np.mean(scores['test_score']))


splitter = StratifiedKFold(n_splits=20, shuffle=True, random_state=42)
scores = cross_validate(dt, train_input, train_target, cv=splitter)
print(np.mean(scores['test_score']))