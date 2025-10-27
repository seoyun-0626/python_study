from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

# 데이터셋 준비
dataset = load_diabetes()

X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
y = pd.Series(dataset.target, name='target')

print(X.head())
print(y.head())

# 데이터셋 분리
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 모델 (확률적 경사하강)
reg = SGDRegressor(
    loss='squared_error',
    penalty='l2', # 규제 방법
    alpha=0.0001, # 규제 강도
    max_iter=2000, # 최대 반복 횟수 (2000번 안넘음)
    tol=1e-3, # 손실 줄어드는 폭이 0.001보다 작으면 멈춤
    random_state=42 # 무작위 과정을 고정해서 매번 실행할 때 같은 결과가 나오도록 하는 설정 (랜덤재현)
    ) 

# 학습 
reg.fit(X_train_scaled, y_train)

# 예측
y_pred = reg.predict(X_test_scaled)

# 성능지표
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse=np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("[Regression Metrics]")
print(f'MAE : {mae:.4f}') # 평균 절대 오차
print(f'MSE : {mse:.4f}') # 평균 제곱 오차
print(f'RMSE : {rmse:.4f}') # 루트 평균 제곱 오차
print(f'R^2 : {r2:.4f}') # 결정계수 (1에 가까울수록 좋음)
print(f'score : {reg.score(X_test_scaled, y_test):.4f}') # 결정계수 

'''
MAE (Mean Absolute Error) = 42.90
👉 평균적으로 예측이 실제값에서 약 42.9만큼 벗어났다는 뜻. (단위는 y와 같음)

MSE (Mean Squared Error) = 2883.72
👉 오차 제곱을 평균낸 값. 큰 오차에 더 큰 패널티를 줌.

RMSE (Root Mean Squared Error) = 53.70
👉 MSE의 제곱근. 실제 데이터 단위로 해석 가능. 즉, 예측값이 실제값과 평균적으로 약 53.7 차이남.

R² (결정계수) = 0.4557
👉 모델이 데이터를 설명하는 비율. 45.6% 정도만 설명한다는 뜻.
(1.0에 가까울수록 잘 맞추는 거고, 0이면 그냥 평균 찍은 수준, 음수면 평균보다도 못함)

score = 0.4557
👉 model.score() 호출하면 회귀에서는 자동으로 R²을 반환하기 때문에 R²랑 같은 값이 나옴.

'''