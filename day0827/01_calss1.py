# 클래스는 왜 필요할까?

result1 = 0

def add(num):
    global result1
    result1 += num
    return result1

print(add(3))
print(add(4))
print(add(5))

# 만약에 계산기가 2대 필요하면?

result2 = 0

def add2(num):
    global result2
    result2 += num
    return result2

print(add2(5))
print(add2(6))
print(add2(7))
