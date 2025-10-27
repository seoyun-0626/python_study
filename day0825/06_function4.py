# 람다식
# 함수를 간단하게 만들기

def add(a,b):
    return a+b

add2 = lambda a, b: a+b

result = add2(3, 4)
print(result)  #7
print()

distance = lambda x1, y1, x2, y2: ((x2-x1)**2 + (y2-y1)**2)**0.5

result = distance(1, 2, 4, 6) # 루트{(4-1)제곱 + (6-2)제곱}
print(result)  #5.0
print()  

print("------리스트 + 맵---------")
print()


print("==============================")

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  #[1, 4, 9, 16, 25]
print()

#리스트 컴프리핸션 방식으로 ! 똑같은 결과 구현하기
# [결과 for x in 어디]

squares = [x**2 for x in numbers]
print(squares)



print("==============================")


numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(lambda x: x % 2 == 0,numbers2))
print(evens)  #[2, 4, 6, 8]
print()

#리스트 컴프리핸션 방식으로 ! 똑같은 결과 구현하기
# [결과 for x in 어디]

evens = [x for x in numbers2 if x % 2 == 0]
print(evens)

print("==============================")


numbers3 = [5, -2, 0, 8, -7]

result = list(map(lambda x : "양수" if x > 0 else("음수" if x < 0 else "0"),numbers3))
print(result) #['양수', '음수', '0', '양수', '음수']
print()

#리스트 컴프리핸션 방식으로 ! 똑같은 결과 구현하기
# [결과 for x in 어디]

result = ["양수" if x > 0 else("음수" if x < 0 else "0") for x in numbers3]
print(result)

print("==============================")
# 람다 + 맵 + 필터 방식으로 똑같이 구현하기 

result3 = list(map(lambda num : num *3, filter(lambda x: x % 2 == 0, numbers3)))
print(result3)
print()

print("============나혼자 연습하기==================")

## 람다식 하나 만들기 map 혹은 filter 넣어서 (리스트)
## 리스트 컴프리헨션으로 바꾸기
## 혹은 반대로!!

numbers4 = [12, 7, 9, 14, 21, 28, 33, 40]

print("--3의 배수이면서 짝수인 숫자만 골라서 새로운 리스트--")

result4 = list(
    filter(lambda x: x % 2 == 0, filter(lambda x: x % 3 == 0, numbers4))
)
print(result4)

result4 = [x for x in numbers4 if x % 3 == 0 and x % 2 ==0]
print(result4)

print("--홀수만 고른후 나온숫자 제곱해서 새로운 리스트--")

result5 = list(
    map(lambda num : num**2, filter(lambda x: x % 2 == 1, numbers4))
)
print(result5)

result4 = [x**2 for x in numbers4 if x % 2 == 1]
print(result5) 

