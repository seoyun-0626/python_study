# PCA (principal Component Analysis)

import numpy as np

# 과일사진 불러오기
fruits = np.load('./data/fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100*100)

# 주성분 분석
# 2차원 데이터를 기대
# 사진인지 아닌지 상관 없음

from sklearn.decomposition import PCA

pca = PCA(n_components=50)
pca.fit(fruits_2d)

# 주성분 모양 50, 10000
print(pca.components_.shape)

import matplotlib.pyplot as plt

def draw_fruits(arr, ratio=1):
    n = len(arr) # dms 샘플개수
    # 한 줄에 10개씩 이미지를 그립니다. (rows=총 몇줄?)
    rows = int(np.ceil(n/10))
    # 행이 1개 이면 열 개수는 샘플개수. 그렇지 않으면 10열.
    cols = n if rows < 2 else 10
    fig, axs = plt.subplots(rows, cols,
                            figsize=(cols*ratio, rows*ratio), squeeze=False)
    for i  in range(rows):
        for j in range(cols):
            if i*10 + j < n:
                axs[i,j].imshow(arr[i*10 + j], cmap='gray_r')
            axs[i,j].axis('off')
    plt.show()      

print('주성분 뽑아보기')
print(pca.components_)

# 주성분 그려보기
draw_fruits(pca.components_.reshape(-1,100,100))          

print('원본 배열 크기')
print(fruits_2d.shape) # 300, 10000

# 주성분으로 차원 축소
fruits_pca = pca.transform(fruits_2d)

print('차원 축소 후 크기')
print(fruits_pca.shape) # (300, 50)     pca = PCA(n_components=50) >>이거때문에 50개인거임
print(fruits_pca[0])

# 다시 복원해서 그려보기
fruits_inverse = pca.inverse_transform(fruits_pca)
print('복원 후 크기 - 원본 비슷하게')
print(fruits_inverse.shape)  # (300, 10000)

fruits_reconstruct = fruits_inverse.reshape(-1, 100, 100)

for start in [0,100,200]:
    draw_fruits(fruits_reconstruct[start:start+100])
    print()

# (설명된 분산) 50개의 주성분이 원본을 얼마나 잘 표현 했을까?
print('주성분별 설명 펴센티지')
print(pca.explained_variance_ratio_)
print('50성분이 원본을 얼마나 표현했나?')
print(np.sum(pca.explained_variance_ratio_)) # 92%

# 주성분 Top10이면 
plt.plot(pca.explained_variance_ratio_)
# plt.show()

'''
KMeans = 놀이터에서 친구끼리 모이는 거.  (비슷한 친구끼리 알아서 모이기)
PCA = 레고 박스에서 중요한 블록만 꺼내도 어떤 집인지 알 수 있는 거. (데이터 압축기술)
'''

#===========================================================

# 차원을 축소해서 분류 시키기 (로지스틱 리그레션 -지도학습 )
# 원본 그대로 분류 시키기 
# 두 개를 비교 (누가 더 빠른가. 스코어는 어떤가?)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(max_iter=1000,random_state=42)

# 타겟 데이터 생성 (사과, 파인애플, 바나나)
target= np.array([0] * 100 + [1] * 100 + [2] * 100)

# 교차검증
from sklearn.model_selection import cross_validate

scores = cross_validate(lr, fruits_2d, target)
print('원본 교차검증 점수')
print(np.mean(scores['test_score']))
print('원본 교차검증 훈련시간')
print(np.mean(scores['fit_time']))

# 50차원으로 축소한 데이터 스코어
scores = cross_validate(lr, fruits_pca, target)
print('50차원 축소 교차검증 점수')
print(np.mean(scores['test_score']))
print('50차원 축소 교차검증 훈련시간')
print(np.mean(scores['fit_time']))

# 원본의 50%를 설명할 수 있을 만큼의 주성분 개수 생성 
pca = PCA(n_components=0.5)
pca.fit(fruits_2d)

print('(50%를 위해) 찾은 주성분 개수')
print(pca.n_components_) # 2개!! 만 있어도 원본의 50프로 설명 가능!


fruits_pca = pca.transform(fruits_2d)
print(fruits_pca.shape) #(300,2)

scores = cross_validate(lr, fruits_pca, target)
print('2차원 축소 교차검증 점수')
print(np.mean(scores['test_score']))
print('2차원 축소 교차검증 훈련시간')
print(np.mean(scores['fit_time']))

from sklearn.model_selection import StratifiedKFold, cross_validate

# StratifiedKFold 정의 (데이터 분할할 때 무작위 + 고정)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# 1. 원본 (10000차원)
lr = LogisticRegression(max_iter=1000, random_state=42)
scores = cross_validate(lr, fruits_2d, target, cv=cv, return_estimator=True)
iters_10000 = [int(est.n_iter_[0]) for est in scores['estimator']]
print("원본(10000차원) fold별 반복 횟수:", iters_10000, "평균:", np.mean(iters_10000))

# 2. PCA 50차원
pca50 = PCA(n_components=50)
fruits_pca50 = pca50.fit_transform(fruits_2d)

lr = LogisticRegression(max_iter=1000, random_state=42)
scores = cross_validate(lr, fruits_pca50, target, cv=cv, return_estimator=True)
iters_50 = [int(est.n_iter_[0]) for est in scores['estimator']]
print("PCA 50차원 fold별 반복 횟수:", iters_50, "평균:", np.mean(iters_50))

# 3. PCA 2차원
pca2 = PCA(n_components=0.5)   # 원본 분산의 50% 설명하는 성분 수 → 2개
fruits_pca2 = pca2.fit_transform(fruits_2d)

lr = LogisticRegression(max_iter=1000, random_state=42)
scores = cross_validate(lr, fruits_pca2, target, cv=cv, return_estimator=True)
iters_2 = [int(est.n_iter_[0]) for est in scores['estimator']]
print("PCA 2차원 fold별 반복 횟수:", iters_2, "평균:", np.mean(iters_2))

# 주성분 2개로 축소해서 -> kmeans 나누고 -> 2차원에 그려보기 
# k평균으로 2차원 그림으로 분류하기 

from sklearn.cluster import KMeans
km = KMeans(n_clusters = 3, random_state=42)
km.fit(fruits_pca) # 2차원으로 축소된 데이터 학습

# 결과확인
print(np.unique(km.labels_, return_counts=True))

print('km.labels_확인')
print(km.labels_)

# 그림 그리기 
for label in range(0,3):
    draw_fruits(fruits[km.labels_ == label])

# 2차원으로 축소된 자표로 산점도 그려보기
# for label in range(0,3):

print(fruits_pca)

for label in range(0,3):
    data = fruits_pca[km.labels_ == label]
    plt.scatter(data[:,0], data[:,1])
plt.legend(['apple', 'banana', 'pineapple'])
plt.show()


