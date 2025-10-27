# 그라디언트 부스팅 원리

# 그라디언트 부스팅
# 히스토그램 기반 그.부 (데이터 변수 구간으로 나눔 - 분할조건 빨리 찾기)

#<비슷한 놈들> - 삼대장 
# (히스토그램 기반 가능)
# XGBoost - 그.부를 기반하여 화려한 옵션
# lightGBM - XGBoost 경량버전 빠름
# CatBoost - 범주형 처리에 특화 (범주 전처리 안해도 됨)

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

wine = pd.read_csv('https://bit.ly/wine_csv_data')

data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']

train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)

# --------------------------------------------------------

# 그라디언트 부스팅 모델

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_validate

gb = GradientBoostingClassifier(random_state=42)
# 교차검증
scores = cross_validate(gb, train_input, train_target,
                        return_train_score=True, n_jobs=-1)

print(np.mean(scores['train_score']), np.mean(scores['test_score']))

# 옵션 설정해보기 
gb = GradientBoostingClassifier(n_estimators=500, learning_rate=0.2,
                                random_state=42)

scores = cross_validate(gb, train_input, train_target,
                        return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))

gb.fit(train_input, train_target)

print('-------훈련 테스트 스코어-------')
print(gb.score(train_input, train_target))
print(gb.score(test_input, test_target))

# 특성 중요도
print(gb.feature_importances_)

# 히스토그램 기반 GB 모델

from sklearn.ensemble import HistGradientBoostingClassifier

hgb = HistGradientBoostingClassifier(random_state=42)
# 교차검증
scores = cross_validate(hgb, train_input, train_target,
                        return_train_score=True, n_jobs=-1)

print(np.mean(scores['train_score']), np.mean(scores['test_score']))

hgb.fit(train_input, train_target)
print('히스트 GB 훈련/테스트 스코어')
print(hgb.score(train_input, train_target))
print(hgb.score(test_input, test_target))