import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt


print('--------데이터준비 -------------')
# 간단한 데이터: y = x^2 (포물선)
X = np.array([[-2], [-1], [0], [1], [2]])
y = np.array([4, 1, 0, 1, 4])

# 처음에는 모든 입력에 대해 y의 평균(=2)만 찍음. (당연히 오차가 큼!)

# 1. 처음에는 아주 단순한 예측기(상수값만 예측하는 모델)로 시작
from sklearn.dummy import DummyRegressor
dummy = DummyRegressor(strategy="mean")  # 평균값만 예측
dummy.fit(X, y) 
print("Step 0 예측:", dummy.predict(X))   # Step 0 예측: [2. 2. 2. 2. 2.]

# 첫 번째 작은 트리가 생겨서 **잔차(실제값 - 평균)**를 보정해 줌.

gbr3 = GradientBoostingRegressor(n_estimators=3, learning_rate=1.0, max_depth=1)
gbr3.fit(X, y)
print("Step 3 예측:", gbr3.predict(X))   # Step 3 예측: [4.      0.71875 0.71875 0.71875 3.84375]
# 세 번째 트리까지 더하면서, 점점 예측값이 실제 포물선 모양에 가까워짐.


# 시각화 
print('------시각화-----')

x_test = np.linspace(-2, 2, 100).reshape(-1, 1)

# 단계별 모델
models = [
    ("1 tree", GradientBoostingRegressor(n_estimators=1, learning_rate=1.0, max_depth=1)),
    ("3 trees", GradientBoostingRegressor(n_estimators=3, learning_rate=1.0, max_depth=1)),
    ("10 trees", GradientBoostingRegressor(n_estimators=10, learning_rate=1.0, max_depth=1))
]

plt.scatter(X, y, color="black", label="실제 데이터")

for label, model in models:
    model.fit(X, y)
    y_pred = model.predict(x_test)
    plt.plot(x_test, y_pred, label=label)

plt.legend()
plt.show()