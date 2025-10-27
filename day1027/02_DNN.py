import keras

print('\n----- 데이터셋 로드 -----')
(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()

train_scaled = train_input / 255.0
train_scaled = train_scaled.reshape(-1, 28*28)

from sklearn.model_selection import train_test_split

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)

# 한 층을 더 추가 해보자.
inputs = keras.layers.Input(shape=(784,)) # 입력층
dense1 = keras.layers.Dense(100, activation='sigmoid') # 은닉층 (입력차원의 1/2 ~ 1/4)
# a x 4 + 2 = b  >>>  b x 3 - 5 = c  >>> c = a x 12 + 1 (결국 선형 결합)
# 비선형성, 복잡성을 주기위해 활성화 함수 통과 ex)sigmoid

dense2 = keras.layers.Dense(10, activation='softmax') # 출력층
model = keras.Sequential([inputs, dense1, dense2])
print()
model.summary()

# ----- 다른 방법으로 층 추가 1 -----

model = keras.Sequential([
    keras.layers.Input(shape=(784,)),
    keras.layers.Dense(100, activation='sigmoid', name='은닉층'),
    keras.layers.Dense(10, activation='softmax', name='출력층')
], name='패션 MNIST 모델 1Type')
print()
model.summary()
# 784 x 100 + 100 = 78500
# 100 x 10 + 10 = 1010

# ----- 다른 방법으로 층 추가 2 -----

model = keras.Sequential(name='패션 MNIST 모델 2Type')
model.add(keras.layers.Input(shape=(784,)))
model.add(keras.layers.Dense(100, activation='sigmoid', name='은닉층'))
model.add(keras.layers.Dense(10, activation='softmax', name='출력층'))
print()
model.summary()

# 모델 컴파일
model.compile(loss='sparse_categorical_crossentropy')  
model.fit(train_scaled, train_target, epochs=5)


