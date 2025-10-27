
'''
❤ SGD (Stochastic Gradient Descent)

- 확률적 경사 하강법
- 한 번에 전체 데이터 쓰는 대신, 일부 샘플(또는 1개)만 뽑아서 기울기 계산
- 대용량 데이터에서 속도 빠름
- 분류, 회귀 둘 다 가능

👉 쉽게 말하면:
밥그릇(데이터)이 너무 커서 한 번에 다 먹기 힘들면,
숟가락으로 조금씩 퍼먹으면서 내려가는 방식.

'''

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

# ------------------------------------------------------------

# 확률적 경사하강 
from sklearn.linear_model import SGDClassifier

sc = SGDClassifier(loss='log_loss', max_iter=10, random_state=42)
sc.fit(train_scaled, train_target)

# max_iter = 10 >>>  10에포크 >> “훈련 데이터 전체를 10번 돌려가며 파라미터 업데이트를 해라
print('훈련셋 스코어')
print(sc.score(train_scaled, train_target))
print('테스트셋 스코어')
print(sc.score(test_scaled, test_target))

# 추가 학습 
# 모든 데이터 1개씩 돌아가며 1회 학습 (1 에포크)
sc.partial_fit(train_scaled, train_target)
sc.partial_fit(train_scaled, train_target)


'''
차이: fit vs partial_fit
-----fit----
한 번 부르면 전체 데이터를 전부 사용해서 처음부터 학습
다시 fit을 하면 → 기존 학습 내용 다 잊고 새로 시작

----partial_fit----
데이터를 조금씩 주고, 이전 학습 결과를 이어서 업데이트

'''

print('추가학습 훈련셋 스코어')
print(sc.score(train_scaled, train_target))
print('추가학습 테스트셋 스코어')
print(sc.score(test_scaled, test_target))

import numpy as np

sc = SGDClassifier(loss='log_loss', random_state=42)

train_score = []
test_score = []

classes = np.unique(train_target)

import matplotlib.pyplot as plt

for _ in range(0, 300):
    
    sc.partial_fit(train_scaled, train_target, classes=classes)
    train_score.append(sc.score(train_scaled, train_target))
    test_score.append(sc.score(test_scaled, test_target))


plt.plot(train_score)
plt.plot(test_score)
plt.xlabel('apoch')
plt.ylabel('accuracy')
plt.show()

'''
1 에포크 = 전체 데이터 한 바퀴 학습

1 이터레이션 = 파라미터 업데이트 1번 (배치 단위로 이루어짐)

옵션 max_iter = 10 = 10에포크

'''

# 100번돌려보자 
sc = SGDClassifier(loss='log_loss',max_iter=100,tol=None, random_state=42)  
sc.fit(train_scaled, train_target)
'''
-----tol=None ----

tol=1e-3 → 손실이 0.001 이하로 줄면 학습 멈춤 (기본값)
tol=1e-4 → 더 빡빡하게, 아주 미세하게 줄어들 때까지 학습
tol=None → 아예 멈추는 조건 끄기 (무조건 max_iter만큼 학습)'''

print('100번 훈련셋 스코어')
print(sc.score(train_scaled, train_target))
print('100번 테스트셋 스코어')
print(sc.score(test_scaled, test_target))


# tol값 지정해보기 
sc = SGDClassifier(loss='log_loss',max_iter=200,tol=1e-3,  n_iter_no_change=20, random_state=42)  
sc.fit(train_scaled, train_target)

print('n번 훈련셋 스코어')
print(sc.score(train_scaled, train_target))
print('n번 테스트셋 스코어')
print(sc.score(test_scaled, test_target))
print('훈련 에포크 수')
print(sc.n_iter_) # 몇번 돌았는지 알려주는애 


print(sc.n_iter_no_change)

'''
tol을 아무리 줄여도, 손실이 더 이상 줄지 않는 plateau에 들어가면 n_iter_no_change 조건 때문에 멈춘다.
끝까지 돌리려면 → tol=None
기본 5번동안 변화가없으면 멈추게되어있는데 n_iter_no_change 이값을 20으로 늘려주니 훈련에포크 수가 확 늘어났다. 확인!
'''



