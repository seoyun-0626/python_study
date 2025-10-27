import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.model_selection import train_test_split, GridSearchCV

# 데이터 불러오기 
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

print(X.head())
X.info()
print(y.head())

# 훈련/테스트 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

# 모델 정의 (두개죠)
rf_model = RandomForestRegressor(random_state=42)
et_model = ExtraTreesRegressor(random_state=42)

# 하이퍼파라미터 그리드 설정
param_grid = {}
#     'n_estimators': [100, 300],   # 트리 개수 늘리기`

# `
#     'max_depth': [None, 10, 20],        # 트리 깊이 다양하게
#     'min_samples_split': [2, 5],        # 분할 기준 더 다양하게
#     'min_samples_leaf': [1, 2]           # 최소 잎 개수 추가
# }

# 그리드 서치 설정
rf_grid = GridSearchCV(rf_model, param_grid, n_jobs=-1, verbose=2)
et_grid = GridSearchCV(et_model, param_grid, n_jobs=-1, verbose=2)
# 모델 학습
print('랜덤포레스트 그리드 서치')
rf_grid.fit(X_train, y_train)


print('엑스트라트리 그리드 서치')
et_grid.fit(X_train, y_train)
print()

# 최적의 파라미터 출력
print('랜덤포레스트 best: ', rf_grid.best_params_)
print('엑스트라 트리 best:' , et_grid.best_params_)

# 최적 모델 
rf_best = rf_grid.best_estimator_
et_best = et_grid.best_estimator_

# 성능 평가  
print('랜덤포레스트 스코어:',rf_best.score(X_test, y_test))
print('엑스트라트리 스코어',et_best.score(X_test, y_test))

# 그레디언트 부스팅 
from sklearn.ensemble import GradientBoostingRegressor

gbr = GradientBoostingRegressor(random_state=42)
gbr.fit(X_train, y_train)

print('그레디언트 부스팅 : ',gbr.score(X_test, y_test))

# XGBoost

from xgboost import XGBRegressor

xgb = XGBRegressor(
    n_estimators=1000,  # 트리 몇 개 만들지
    learning_rate=0.08, # 각 트리의 기여도를 얼마나 줄 건지 (학습률)
    max_depth=6,
    subsample=0.8,  # 전체 데이터 중 80%만 랜덤하게 사용
    colsample_bytree=0.8, # 특성(열) 중 80%만 랜덤 선택
    random_state=42,
    n_jobs=-1,
    verbosity=2)
'''
📌 verbosity 값
0 → silent (출력 없음)
1 → warning만 출력
2 → info (학습 진행상황 로그 출력) ✅
3 → debug (아주 상세한 로그)
'''

xgb.fit(X_train, y_train)
print('XGBoost :', xgb.score(X_test, y_test))


