import pandas as pd

fish = pd.read_csv('https://bit.ly/fish_csv_data')

print(fish.head())
print()

# fish.to_csv('./data/fish_data.csv',index=False)
# 저장 하고싶으면 실행 한번 하세요 

# 물고기 종류 확인 (7개)
print(pd.unique(fish['Species']))
print()

'''
'Bream' 'Roach' 'Whitefish' 'Parkki' 'Perch' 'Pike' 'Smelt'
참붕어 붉은줄납줄개  백어      파르키    농어   가시고기  빙어
'''

# 인풋데이터
fish_input = fish[['Weight', 'Length','Diagonal','Height','Width']]
print(fish_input.head())
print()

# 타겟 데이터 
fish_target = fish['Species']

# 훈련/테스트 셋 분리 (디폴트 최대 몇? 75:25)
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    fish_input, fish_target, random_state=42)

# 스케일링(표준화)
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

# -------------------------------------------------------
# 로지스틱 회귀로 다중분류 수행 
# C = 계수제곱 규제(L2), 작을수록 규제 커짐. 기본값1
# max_iter 기본값 100

import numpy as np
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=20, max_iter=1000)
lr.fit(train_scaled, train_target)

print('훈련 스코어')
print(lr.score(train_scaled, train_target))
print('테스트 스코어')
print(lr.score(test_scaled, test_target))
print()

print('상위 5개행 예측 결과')
print(lr.predict(test_scaled[:5]))
print()

print('상위 5개행 클래스 확률')
proba = lr.predict_proba(test_scaled[:5])
print(np.round(proba, decimals=3))
print()

print('클래스종류')
print(lr.classes_)

# 파라미터가 7세트 나온다.
# 각 클래스별로 방정식 만들어졌다는 뜻.
print('파라미터 개수')
print(lr.coef_.shape, lr.intercept_.shape)

'''
coef_
→ 각 클래스 × 각 특성(입력 변수)에 대응하는 가중치 전부 보여줘.
→ 모양이 (클래스 수, 특성 수) → 너는 (7, 5).
→ 즉, “클래스마다 특성 5개에 대해 어떤 영향을 주는지” 다 들어 있음.

intercept_
→ 각 클래스별로 하나씩 있는 **편향(bias)**만 보여줘.
→ 모양이 (클래스 수,) → 너는 (7,).
→ 즉, “클래스별 기본 점수” 같은 개념.

'''

'''
로지스틱회기 모델은 - 이진분류, 다중분류가 가능하다.
선형 방정식 - 시그모이드 통과 (확률값으로 표시)
최적화 - 경사하강법 기반 


이진분류
-손실함수 = 바이너리 크로스 엔트로피 (BCE)

다중분류 - 확률값 -> 소프트맥스함수 통과 (클래스별 확률값으로 표시)
-손실함수 = 크로스 엔트로피(CE)

'''

print('상위 5개행 클래스별 z값 출력')
decision = lr.decision_function(test_scaled[:5])  # decision_function()은 샘플이 각 클래스에 대해 계산한 "점수(logit)"를 반환
print(np.round(decision, decimals=2))
print()

'''
1. 점수(logit)가 뭐냐면?
예측할 때는 항상 이런 순서를 거쳐:
입력 × 가중치 + 편향 → 점수(logit)
그 점수를 시그모이드(이진)나 소프트맥스(다중)에 넣음
→ 확률로 변환 (predict_proba)
→ 제일 큰 확률 가진 클래스 선택 (predict)
즉, decision_function은 **1단계 결과(확률로 바꾸기 전의 생 점수)**를 보여주는 거야.
'''

from scipy.special import softmax

print('소프트 맥스 함수에 z값 대입')
proba = softmax(decision, axis=1)
print(np.round(proba, decimals=3))


'''
상위 5개행 클래스 확률 = predict_proba 결과
소프트맥스(z) = decision_function 결과를 softmax에 넣은 값 
이 두개가 같은 값이 나올수밖에 없음 

decision_function → 확률 만들기 전 단계 점수
predict_proba = softmax(decision_function())

logit(z) = 원래 점수

softmax(z) = 그 점수를 “확률 분포”로 바꾼 것
그래서 숫자 값은 달라
하지만 softmax(z) 결과 = predict_proba() 결과이므로 최종 확률은 같아

'''

