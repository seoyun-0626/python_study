import numpy as np

perch_length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0,
     21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5,
     22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5,
     27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0,
     36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0,
     40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
     )
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )


from sklearn.model_selection import train_test_split # 데이터셋을 무작위로 섞어서 훈련/테스트 세트로 나누는 도구

train_input, test_input, train_target, test_target = train_test_split(
    perch_length,perch_weight,random_state=42)


#-1로 적어주면 알아서 계산해준다 
train_input = train_input.reshape(-1,1)
test_input = test_input.reshape(-1,1)

from sklearn.neighbors import KNeighborsRegressor

knr = KNeighborsRegressor(n_neighbors=3)
knr.fit(train_input, train_target)
print('50센티 농어 무게')
print(knr.predict([[50]]))

import matplotlib.pyplot as plt

# 50센치 농어 이웃 정보 받아오기 
distances, indexes = knr.kneighbors([[50]])
# 훈련세트 분포
plt.scatter(train_input, train_target)
# 이웃 분포
plt.scatter(train_input[indexes], train_target[indexes], marker='D')
# 50 센치 농어 
plt.scatter(50, 1033, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

print('이웃들 평균')
print(np.mean(train_target[indexes])) # 1033.333
print('100센치 농어 무게')
print(knr.predict([[100]])) # 1033.333

distances, indexes = knr.kneighbors([[100]])

# 훈련세트 분포
plt.scatter(train_input, train_target)
# 이웃 분포
plt.scatter(train_input[indexes], train_target[indexes], marker='D')
# 100 센치 농어 
plt.scatter(100, 1033, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 최근접 이웃 모델의 한계 파악 끝 !!!

# 그래서 선형 회귀 모델을 배워보자 !!!

# -------------- 선형회귀 ------------------

from sklearn. linear_model import LinearRegression

lr = LinearRegression()
# 선형회귀 모델 훈련  

lr.fit(train_input, train_target) # 훈련 끝 

print('선형회귀 - 50센치 농어 무게 예측')
print(lr.predict([[50]]))
print('파라미터 값 확인')
print(lr.coef_, lr.intercept_) 

# lr.coef_
# coefficient (계수, 기울기)
# 입력 변수(x)가 1 증가할 때 출력(y)이 얼마나 변하는지 나타냄.
# 예: lr.coef_ = [20] → 길이가 1cm 늘면 무게가 20g 늘어난다는 뜻.

# lr.intercept_
# intercept (절편)
# x=0일 때 y값. 즉, 직선이 y축과 만나는 지점.
# 예: lr.intercept_ = -100 → 길이가 0일 때 무게는 -100g (물리적으로 말은 안 되지만, 수학적 직선 계산이니까 그렇게 나옴).

print()

plt.scatter(train_input, train_target)

#  y = (lr.coef_ * x) + lr.intercept_ 선형 회귀 모델이 학습한 직선 공식
plt.plot([15, 50], [15*lr.coef_+lr.intercept_,50*lr.coef_+lr.intercept_])
plt.scatter(50, 1241.8, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# y = ax + b 직선을 찾아라(a,b 값을 찾아라)
# 우리의 목표 - 오차제곱이 가장 적게 나오도록 하는 (a,b 찾기)
# (a로 정리한) 오차제곱은 아래로 볼록한 포물선
# >>> a가 몇일때 이 포물선이 최솟값을 가질까?
# >>> 이차 함수를 a에 대하여 미분한 값이 0이 되는!! 그때의 a값이다.
# b에 대해서도 같은 과정을 거친 뒤, 두 식을 연립 방정식 해서 a, b값 도출!!

# 길이만 가지고 하기 아쉽다.
# 인위적인 컬럼을 만들어 보자 
# >>> 길이 ^2 컬럼을 만들어서 특성 2개로 학습시키자

# ---------- 다항회귀 ---------------
# 독립변수에 대해서 제곱, 세제곱.... 에 초점을 맞춘 용어.

train_poly = np.column_stack((train_input **2, train_input))
test_poly = np.column_stack((test_input **2, test_input))

print(train_poly)
print(train_poly.shape, test_poly.shape)

lrp = LinearRegression()
lrp.fit(train_poly, train_target)

print('다항회귀 - 50짜리 농어 예측')
print(lrp.predict([[50**2,50]]))
print()
print(lrp.coef_, lrp.intercept_)
print()

# 곡선 그려보기 
point = np.arange(15, 50)

plt.scatter(train_input, train_target)

plt.plot(point, 1.01*point**2 -21.6*point + 116.05)  # 무게=1.01×(길이2)−21.6×(길이)+116.05
plt.scatter([50],[1574], marker='^')
plt.show()

print('선형회귀 훈련/테스트 스코어')
print(lr.score(train_input, train_target))
print(lr.score(test_input, test_target))


print('다항회귀 훈련/테스트 스코어')
print(lrp.score(train_poly, train_target))
print(lrp.score(test_poly, test_target))

