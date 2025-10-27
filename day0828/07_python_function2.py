print()
print("------hex------")
print() # 정수를 입력받아 16진수 문자열로 반환

print(hex(234))
print(hex(3))

print()
print("------oct------")
print() # 정수를 8진수 문자열로 반환

print(oct(3))
print(oct(8))
print(oct(9))
print(oct(16))

print()
print("------id------")
print() # 객체의 고유 주솟값 반환

a = 3
print(id(3))
print(id(a))

b = a
print(id(b))

print()
print("------int------")
print() # 정수로 반환

print(int('3'))
print(int(3.4))
print(int(3.9))

print(int('11' , 2)) # 2진수 11을 10진수로 반환 #3
print(int('1A' , 16)) # 16진수 1A를 10진수로 반환 #26

print()
print("------isintance------")
print()  # 그 클래스의 인스턴스인가?

class Person : pass

a = Person()
b = 3

print(isinstance(a,Person))
print(isinstance(b,Person))


print()
print("------len------")
print() # 길이 반환

print(len('python'))
print(len([1, 2, 3]))
print(len([1, a]))

print()
print("-------list-------")
print()

print(list("python"))
print(list((1,2,3)))

a = [1, 2, 3]
b = a # 참조
c = list(a) # 복사

print()
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))


print()
print("-------max-------")
print()

print(max([1, 2, 3]))  # 3
print(max("python"))  # y

print(min([1, 2, 3]))  # 1
print(min("python"))  # h