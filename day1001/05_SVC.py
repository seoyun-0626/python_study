# SVM (Support Vector Machine)
# 분류: SVC, 회귀: SVR
# 결정 경계를 찾는 모델
# 마진 - 서포트 벡터와 결정 경계와의 거리
# 마진을 최대화하는 것을 목표로 함.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

X, y = make_classification(n_samples=400, n_classes=2, n_features=2, n_redundant=0, random_state=42)

# n_samples 총 셈플 수
# n_classes 클래스 수
# n_features 특성 수 
# n_redundant 불필요한 특성 수

print(X)
print(y)
print()

# 훈련 셋 분리 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 스케일링
scalar = StandardScaler()
X_train_sc = scalar.fit_transform(X_train)
X_test_sc = scalar.transform(X_test)

# 선형 커널
lin_clf = SVC(kernel='linear', C=1.0, random_state=42)
# 모델 ㅅ헤팅 # C 높을수록 예민 (과대적합)
lin_clf.fit(X_train_sc, y_train) # 모델 훈련
y_pred_lin = lin_clf.predict(X_test_sc) # 예측

print('LinearSVC 정확도: ', accuracy_score(y_test, y_pred_lin))
print()
print(classification_report(y_test, y_pred_lin))
print()
print('혼동 행렬: \n', confusion_matrix(y_test, y_pred_lin))
print()

# RBF 커널 (비선형 경계학습)
# Radial Basis Function (방사 기저 함수)
rbf_clf = SVC(kernel='rbf', C=100, gamma=10, random_state=42)
# gamma 값이 높을 수록 (과적합 위협)
rbf_clf.fit(X_train_sc, y_train)
y_pred_rbf = rbf_clf.predict(X_test_sc)

print('\n [RBF SVC] 정확도: ', accuracy_score(y_test, y_pred_rbf))
print()
print(classification_report(y_test, y_pred_rbf))
print()
print('혼동행렬: \n', confusion_matrix(y_test, y_pred_rbf))
print()

# 결정경계 시각화 (비교)
def plot_decision_boundary(model, X_sc, y, title):
    # 그리드 생성
    x_min, x_max = X_sc[:,0].min() -1, X_sc[:,0].max()+1
    y_min, y_max = X_sc[:,1].min() -1, X_sc[:,1].max()+1
    xx,yy = np.meshgrid(
        np.linspace(x_min, x_max, 300),
        np.linspace(y_min, y_max, 300)
    )

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    # 등고선과 산점도
    plt.figure(figsize=(5,4))
    plt.contourf(xx,yy,Z,alpha=0.25)
    plt.scatter(X_sc[:,0], X_sc[:,1],c=y,edgecolors='k',s=30)
    plt.title(title)
    plt.xlabel('x1 (scaled)')
    plt.ylabel('x2 (scaled)')
    plt.tight_layout()
    plt.show()

plot_decision_boundary(lin_clf, X_train,y_train, 'LinearSVC (test)')
plot_decision_boundary(rbf_clf, X_train,y_train, 'RBF SVC (test)')
    
x = np.linspace(-2,2,5)
y = np.linspace(-2,2,5)
print(x)
print(y)

xx,yy = np.meshgrid(x,y)

print(xx)
print(yy)

print(xx.ravel())

Z = rbf_clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
print(Z)

plt.contourf(xx,yy,Z,alpha=0.25)
plt.show()





