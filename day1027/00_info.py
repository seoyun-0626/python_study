'''
<머신러닝>
KNN - 최근접 이웃 - 예측, 분류
리니어 리그레션, 로지스틱 리그레션
디씨전트리 - 랜덤포레스트 - 엑스트라트리 - XGBoost 등등
SVM (써포트 벡터 머신)

뉴런 
인공신경망(Artifixial Neural Network) ANN
'''
# pip install keras
# pip install tensorflow

# -----------------------------------------------------

# 패션 MNIST 데이터셋
# 10 종류의 패션 아이템 
# keras - 딥러닝 고수준 API

import keras

print('\n----- 데이터셋 로드 -----')
(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()

# 데이터 크기 확인
print('\n----- 훈련셋 크리 -----')
print(train_input.shape, train_target.shape) # (60000, 28, 28) (60000,)
print('\n----- 테스트셋 크기 -----')
print(test_input.shape, test_target.shape) # (10000, 28, 28) (10000,)

# 이미지로 뽑아보기
import matplotlib.pyplot as plt 

fig, axs = plt.subplots(1, 10, figsize=(10,3))
for i in range(10):
    axs[i].imshow(train_input[i], cmap='gray_r')
    axs[i].axis('off')
# plt.show()    

print('\n----- 첫 10개 타겟값 -----')
print(train_target[:10])

'''
0       1      2       3      4     5      6       7       8      9
티셔츠  바지  스웨터  드레스   코트  센달   셔츠   스니커즈   가방  앵클부츠
'''

import numpy as np

# 클래스별 데이터 개수 확인
print('\n----- 클래스별 데이터 개수 확인 -----')
print(np.unique(train_target, return_counts=True))

# ---------- 로지스틱 회귀로 패션 아이템 분류하기 ----------

# 스케일링 (이미지의 경우 보통 0~1 사이로 스케일링)
train_scaled = train_input / 255.0
# 인풋 사이즈로 리셰입
train_scaled = train_scaled.reshape(-1, 28*28)

print('\n----- 훈련셋 크기 -----')
print(train_scaled.shape) # (60000, 784)


from sklearn.model_selection import cross_validate
from sklearn.linear_model import SGDClassifier # 확률적 경사 하강법

# max_iter 10, 20 으로 변경 시도 
print('\n ----- SGDcalssifier 컴파일 및 교차검증 -----')
sc = SGDClassifier(loss='log_loss', max_iter=20, random_state=42)
scores = cross_validate(sc, train_scaled, train_target)

print('\n ----- 테스트 스코어 -----')
print(np.mean(scores['test_score']))