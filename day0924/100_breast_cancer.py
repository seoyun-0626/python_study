from sklearn.datasets import load_breast_cancer
import pandas as pd

# 1. 유방암 데이터셋 불러오기 (사이킷런 내장 데이터)
cancer = load_breast_cancer()

print(cancer.keys())            # 데이터셋에 들어 있는 키 값 확인 (data, target, feature_names 등)
print(cancer.data.shape)        # (샘플 수, 특성 수) → 569개 샘플, 특성 30개
print(cancer.feature_names)     # 특성 이름들 출력 (예: mean radius, mean texture 등)
print(cancer.target_names)      # 타깃 클래스 이름 출력 (['malignant', 'benign'])


# 2. 입력 데이터(DataFrame으로 변환)
# cancer.data = 특성 값들 (numpy 배열)
# cancer.feature_names = 열 이름으로 사용
data = pd.DataFrame(cancer.data, columns=cancer.feature_names)
# 정답(label) 컬럼 추가 (악성=0, 양성=1)

# target =cancer['target']  에러에러 
target = cancer['target']

from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)

# 최종 분리된 데이터셋 크기 확인
print(train_input.shape, test_input.shape) # (455, 30) (114, 30)
print()

# --- 결정트리 ----
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42)
dt.fit(train_input, train_target)

# 결정트리 훈련/테스트 스코어 
print(dt.score(train_input, train_target))
print(dt.score(test_input, test_target))

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(20,15))
plot_tree(dt, filled=True,feature_names=cancer.feature_names)

plt.show()

print(data.shape)     # (569, 30)

print(target.shape) # (569,)

print(data.head())
print(data.info())