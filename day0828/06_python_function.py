print()
print("------abs------")
print()  # 절대값

print(abs(3))
print(abs(-3))
print(abs(-0.2))

print()
print("------all------")
print()  # 반복 가능한 객체 안의 값이 전부 참인지 검사

print(all([1, 2, 3]))  # True
print(all([1, 2, 3, 0])) # False
print(all((1, 2, 3)))
print(all('파이썬 좋아요'))
print(all(''))

print()
print("------any------")
print() # 요소들 중에 하나라도 참이면 참 

print(any([1, 2, 0])) 
print(any([0, ""]))

print()
print("------chr /ord ------")
print() # 유니코드 숫자를 입력받아 해당하는 문자 반환 

print(chr(97))  # a 
print(chr(44032)) # 가

print(ord('a'))  # 97
print(ord('가'))  # 44032



print()
print("------dir------")
print() # 객체가 지닌 변수나 함수를 반환 

print(dir([1, 2, 3]))
print(dir({'a':1}))

print()
print("------divmod------")
print() # 몫과 나머지를 튜플로 반환

print(divmod(7, 3))

print()
print("------enumerate------")
print() # (리스트, 튜플 등)입력 받아서 인덱스 포함하여 반환 

for idx , name in enumerate(['body','foo', 'bar']):
    print(idx,name)

print()
print("------eval-----")
print()  # 문자열로 된 표현식을 실제 코드처럼 실행해서 결과를 돌려주는 함수

print(eval('1+2'))
print(eval("'hi' + 'hello'"))
print(eval('divmod(4, 3)'))

print()
print("------filter------")
print() 
# 리스트 같은 반복 가능한 객체에서 조건에 맞는 값만 걸러내는 함수
# 반환값이 참인 것만 묶어서 반환 

numbers = [1, -3, 2, 0, -5, 6]

# def positive(numbers):
#     result = []
#     for i in numbers:
#         if i > 0:
#             result.append(i)
#     return result
# # print(positive(numbers))

# def positive(x):
#     return x > 0
# print(list(filter(positive, numbers)))    

print(list(filter(lambda x : x > 0, numbers)))


print()
print("------map------")
print()

# def two_times(numbers):
#     result = []
#     for i in numbers:
#         result.append(i * 2)
#     return result

# a = two_times(numbers)
# print(a)  # 2, -6, 4, 0, -10, -12)    

# def two_times(x):
#     return x * 2

# print(list(map(two_times,numbers)))    
# map(함수, 반복 가능 데이터)
# 요소별 결과 값 반환


print(list(map(lambda x : x * 2, numbers)))