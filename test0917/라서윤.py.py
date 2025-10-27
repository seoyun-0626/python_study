'''
타이타닉 데이터를 이용하여,
수업시간에 배운 머신러닝 모델 2가지를 학습 시킨뒤,
성능을 비교/평가하세요.

<코드>
전처리 및 간단한 시각화
최적의 파라미터를 찾기 위한 그리드 서치 시행
다양한 성능평가시 ROC 그래프 필수 포함
'''

import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
titanic = sns.load_dataset('titanic')

print(titanic.head())
titanic.info()

data = titanic[['pclass','sex','age','fare']].copy()
target = titanic['survived']


# 성별, 나이, 객실등급, 요금 으로 생존률 확인 
# 로지스틱회귀, 랜덤포레스트 두가지로 확인예정 

print(titanic.isnull().sum()) # 결측치 확인시 내가 필요한 컬럼에서 age만 결측치 확인
 
print("최소 나이:", titanic['age'].min())
print("최대 나이:", titanic['age'].max())
print()

# 어린이부터 노인까지 나이격차가 커서 평균보단 중앙값이 더 오차가 적을거같아 median선택함
data['age'] = data['age'].fillna(data['age'].median())

# 성별도 영어라 숫자로 전처리 필요함 
# day0904_06 OneHotEncoder

from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse_output=False)

sex_encoded = encoder.fit_transform(data[['sex']])

# 데이터 프레임형태로 변환 
sex_encoded_df = pd.DataFrame(sex_encoded, columns=encoder.get_feature_names_out(['sex']))

print(sex_encoded_df)

# 원래 data에서 sex 빼고, sex_encoded_df 붙이기
data = pd.concat([data.drop(columns=['sex']), sex_encoded_df], axis=1)
print(data.head())

print()
print()

from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42
)

log_reg = LogisticRegression()  

# 그리드 서치   >> 0925_02

from sklearn.model_selection import GridSearchCV

# 로지스틱 회귀에서 쓸 수 있는 주요 파라미터
param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],       # 규제 강도 (작을수록 규제 ↑)
    'solver': ['liblinear', 'lbfgs']    
    # 최적화 방법  liblinear >> 2진분류 적합 lbfgs >> 대규모 다중클래스 분류 잘함 
}

grid_log = GridSearchCV(LogisticRegression(max_iter=1000), 
                        param_grid, 
                        cv=5,           # 5등분 교차검증
                        scoring='accuracy')

# 훈련
grid_log.fit(train_input, train_target)

print("로지스틱 최적 파라미터:", grid_log.best_params_)
print("로지스틱 교차검증 최고 점수:", grid_log.best_score_)  # 0.7934994582881907
# 베스트 찾아오기
dt = grid_log.best_estimator_
print("테스트 정확도:", dt.score(test_input, test_target))  # 0.7932960893854749
print()
print()


# 그래프 찾은 베스트로 적용 

from sklearn.metrics import RocCurveDisplay
import matplotlib.pyplot as plt

print(dt.predict_proba(test_input[:5]))

y_proba = dt.predict_proba(test_input)[:, 1]

RocCurveDisplay.from_predictions(test_target, y_proba)
plt.title('LogisticRegression ROC')
plt.show()


#----------------------------------------------------------------
print('-----------------랜덤포레스트-------------------')

from sklearn.ensemble import RandomForestClassifier   # 0925_04

rf_model = RandomForestClassifier(random_state=42)

param_grid_rf = {
    'n_estimators': [50, 100, 300],   # 트리 개수 늘리기`
    'max_depth': [None,5, 10, 20],        # 트리 깊이 다양하게
    'min_samples_split': [2, 5, 10],        # 분할 기준 더 다양하게
    'min_samples_leaf': [2, 5, 10]           # 최소 잎 개수 추가
}

# 그리드 서치 
rf_grid = GridSearchCV(estimator=rf_model,param_grid=param_grid_rf, n_jobs=-1, verbose=2)

rf_grid.fit(train_input, train_target)
print()
print()

print("랜덤포레스트 최적 파라미터:", rf_grid.best_params_) # 0.8328769821727569
print("랜덤포레스트 교차검증 최고 점수:", rf_grid.best_score_) # 0.8324022346368715

best_rf_model = rf_grid.best_estimator_
print("랜덤포레스트 테스트 정확도:", best_rf_model.score(test_input, test_target))

# 랜덤포래스트 ROC

from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import classification_report, confusion_matrix

print("-------------- RandomForest 성능 평가 --------------")
y_pred_rf = best_rf_model.predict(test_input)

print("\n<Confusion Matrix>")
print(confusion_matrix(test_target, y_pred_rf))

print("\n<Classification Report>")
print(classification_report(test_target, y_pred_rf))

# 생존 1 뽑기
y_proba_rf = best_rf_model.predict_proba(test_input)[:, 1]


# ROC 곡선 그리기
RocCurveDisplay.from_predictions(test_target, y_proba_rf)
plt.title('RandomForest ROC')
plt.show()

# pclass별 생존률
class_survival = titanic.groupby('pclass')['survived'].mean()

# 바그래프 그리기
class_survival.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title("Pclass별 생존률")
plt.xlabel("객실 등급 (Pclass)")
plt.ylabel("생존률")
plt.xticks(rotation=0)
plt.show()
#------------------둘이 같이 띄워 비교하기 ----------------------------------------

from sklearn.metrics import RocCurveDisplay

fig, axes = plt.subplots(1, 2, figsize=(12, 6))


# 위에 구해놓은거 사용 
RocCurveDisplay.from_predictions(test_target, y_proba, ax=axes[0])   # 로지스틱
axes[0].set_title("Logistic Regression ROC")

RocCurveDisplay.from_predictions(test_target, y_proba_rf, ax=axes[1])  # 랜덤포레스트
axes[1].set_title("RandomForest ROC")

plt.show()

from sklearn.metrics import roc_curve, auc

# ---------------- 로지스틱 ----------------
fpr_log, tpr_log, _ = roc_curve(test_target, y_proba)
auc_log = auc(fpr_log, tpr_log)

# ---------------- 랜덤포레스트 ----------------
fpr_rf, tpr_rf, _ = roc_curve(test_target, y_proba_rf)
auc_rf = auc(fpr_rf, tpr_rf)

# ---------------- 합쳐서 그리기 ----------------
plt.figure(figsize=(6,6))
plt.plot(fpr_log, tpr_log, label=f'Logistic Regression (AUC={auc_log:.2f})')
plt.plot(fpr_rf, tpr_rf, label=f'RandomForest (AUC={auc_rf:.2f})')

plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve Comparison')
plt.legend(loc='lower right')
plt.show()

