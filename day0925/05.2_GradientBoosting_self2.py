import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor


print('-----데이터--------')
# 입력(X)과 출력(y) → y = x^2
X = np.array([[-2], [-1], [0], [1], [2]])  # 입력
y = np.array([4, 1, 0, 1, 4])  # 출력 

print('----------평균만 찍기---------')
from sklearn.dummy import DummyRegressor

dummy = DummyRegressor(strategy="mean")
dummy.fit(X, y)
print("Step 0 예측:", dummy.predict(X))   # 4,1,0,1,4의 평균 값 그냥 2 /// Step 0 예측: [2. 2. 2. 2. 2.]

# 오차는 실제값 - 예측값 
# 그 다음에 오차만 가지고 새로운 트리를 학습함 


# 트리1개 
gbr3 = GradientBoostingRegressor(n_estimators=1, learning_rate=1.0, max_depth=1)   #1 예측: [4.  1.5 1.5 1.5 1.5]
gbr3.fit(X, y)
print(" 1 예측:", gbr3.predict(X))


# 트리 2개
gbr3 = GradientBoostingRegressor(n_estimators=2, learning_rate=1.0, max_depth=1)  # y - (평균예측 + 첫 번째 트리 출력)
gbr3.fit(X, y)
print(" 2 예측:", gbr3.predict(X))

# 트리3개 
gbr3 = GradientBoostingRegressor(n_estimators=3, learning_rate=1.0, max_depth=1)
gbr3.fit(X, y)
print(" 3 예측:", gbr3.predict(X))

# 트리 5개 
gbr3 = GradientBoostingRegressor(n_estimators=5, learning_rate=1.0, max_depth=2)
gbr3.fit(X, y)
print(" 5 예측:", gbr3.predict(X))


#시각화 

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

x_test = np.linspace(-2, 2, 100).reshape(-1, 1)

# 단계별 모델 정의
models = [
    ("1 tree", GradientBoostingRegressor(n_estimators=1, learning_rate=1.0, max_depth=1, random_state=0)),
    ("3 trees", GradientBoostingRegressor(n_estimators=3, learning_rate=1.0, max_depth=1, random_state=0)),
    ("10 trees", GradientBoostingRegressor(n_estimators=10, learning_rate=1.0, max_depth=1, random_state=0))
]

# 모델 학습 + 트리 시각화
for label, model in models:
    model.fit(X, y)
    
    n_trees = model.n_estimators
    plt.figure(figsize=(4*n_trees, 4))
    
    for i in range(n_trees):
        plt.subplot(1, n_trees, i+1)
        plot_tree(model.estimators_[i, 0], filled=True, feature_names=["X"], rounded=True)
        plt.title(f"{label} - 트리 {i+1}")
    
    plt.tight_layout()
    plt.show()