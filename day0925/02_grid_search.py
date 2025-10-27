'''
❤ 그리드 서치 (Grid Search)

- 하이퍼파라미터 후보를 전부 탐색 (완전 탐색)
- GridSearchCV: 교차검증까지 포함해서 최적 조합 선택

👉 쉽게 말하면:
슈퍼마켓에서 진열된 모든 옷을 다 입어보고
제일 잘 맞는 사이즈를 고르는 방식.
'''

import pandas as pd
import numpy as np

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

# 그리드 서치
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

params = {'min_impurity_decrease':[0.0001,0.0002,0.0003,0.0004,0.0005]}

# n_jobs -- CPU 코어 개수 최대
gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)

# 파라미터를 돌아가며 교차검증 실행 
# 가장 최적의 파라미터 조합 결과 나오면, 그 조합으로 모델 최종 훈련 
gs.fit(train_input, train_target)

# 가장 좋은 조합 (모델) 받아오기 
dt = gs.best_estimator_
print('그리드 서치 종료 후 훈련셋 스코어')
print(dt.score(train_input, train_target))

print('각 조합에 대한 검증 점수 , 가장 좋은 점수를 낸 하이퍼파라미터 조합')
print(gs.best_params_)

print('가장 점수가 좋은 조합, 위의 best_params_로 이미 학습이 끝난 최적 모델 객체')
print(gs.best_estimator_)

print('각 조합에 대한 검증 점수')
print(gs.cv_results_['mean_test_score'])

print('교차 검증에서 나온 최고 평균 점수 , 교차 검증에서 나온 최고 평균 점수')
print(gs.best_score_)  

print('가장 점수가 높은 조합 - 방법 2')
print(gs.cv_results_['params'][gs.best_index_])

# 여러 파라미터 서치하기
params = {'min_impurity_decrease': np.arange(0.0001,0.001,0.0001,),  # 9가지 
          'max_depth': range(5,20,1),  # 15가지
          'min_samples_split': range(2,100,10)} # 10까지 

gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
gs.fit(train_input, train_target)

# 교차검증 고생했다.
print('가장 점수가 높은조합')
print(gs.best_params_)

print('가장 높은 검증 점수')
print(np.max(gs.cv_results_['mean_test_score']))
print(gs.best_score_)  

# 가장 좋은 조합 (모델) 받아오기 
dt = gs.best_estimator_
print('그리드 서치 종료 후 훈련셋 스코어')
print(dt.score(train_input, train_target))
print('그리드 서치 종료 후 테스트셋 스코어')
print(dt.score(test_input, test_target))

'''
-------cv_results_에 자동으로 생기는 주요 키들-------

mean_fit_time	  : 각 파라미터 조합을 학습(fit)하는 데 걸린 평균 시간

std_fit_time	  : 학습 시간의 표준편차

mean_score_time	  : 검증 점수 계산(score)하는 데 걸린 평균 시간

std_score_time	  : 그 표준편차

params 각 조합에   : 사용된 하이퍼파라미터 딕셔너리

mean_test_score	  :각 조합의 교차검증 평균 점수

std_test_score	  :교차검증 점수의 표준편차

rank_test_score   :점수가 높은 순위 (1이 최고)

'''


# gs.cv_results_ 자체가 딕셔너리(dictionary) 라서, keys() 하면 그 안에 들어있는 **항목 이름(키 목록)**을 볼 수 있어.
print()
for key in gs.cv_results_.keys(): print(key)

# ------- 랜덤 서치 ----------------

from scipy.stats import uniform, randint

params = {'min_impurity_decrease': uniform(0.0001, 0.001),
          'max_depth': randint(20,50),
          'min_samples_split': randint(2, 25),
          'min_samples_leaf': randint(1,25)}

from sklearn.model_selection import RandomizedSearchCV

rs = RandomizedSearchCV(DecisionTreeClassifier(random_state=42),params,
                        n_iter=100, n_jobs=-1, random_state=42)
rs.fit(train_input, train_target)


'''
GridSearchCV : 모든 경우 다 해봄 (완벽하지만 느림)

RandomizedSearchCV : 일부만 랜덤으로 뽑아서 해봄 (빠름, 근사해도 충분할 때 좋음)
'''

print('가장 좋은 조합')
print(rs.best_params_)

print('가장 높은 검증 점수')
print(np.max(rs.cv_results_['mean_test_score']))
print(rs.best_score_)

dt = rs.best_estimator_
print('테스트셋 스코어')
print(dt.score(test_input, test_target))


