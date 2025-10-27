print()
print("------pow------")
print() # 거듭제곱(제곱, n제곱)을 계산하는 함수

print(pow(2, 4)) #2의 4승 16
print(pow(2,100)) #2의 100승 

print()
print("------range------")
print()

print(list(range(5)))  # [0, 1, 2, 3, 4]   # 0부터 끝값-1 까지
print(list(range(5,10)))  # [5, 6, 7, 8, 9]  # 시작부터 끝값-1 까지
print(list(range(1,10,2))) # [1, 3, 5, 7, 9]  # 간격만큼 증가
print(list(range(0,-11,-2))) # [0, -2, -4, -6, -8, -10] 
print(list(range(0,-11,-1))) # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

print()
print("------round------")
print() # 반올림

print(round(4.6)) # 5
print(round(4.2)) # 4
print(round(4.5)) # 가까운 짝수쪽으로 붙음 4
print(round(5.5)) # 6

print(round(5.678, 2)) # 5.68

print()
print("------sorted------")
print() # 정렬해서 리스트로 반환

print(sorted([3, 1, 2]))  # [1, 2, 3]
print(sorted(['a', 'b', 'c'])) # ['a', 'b', 'c']
print(sorted('zero')) # ['e', 'o', 'r', 'z']
print(sorted([3, 2, 1])) # [1, 2, 3]

print()
print("------str------")
print()  # 문자열로반환

print(str(3))
print(str('hi'))

print()
print("------sum------")
print() # 합

print(sum([1, 2, 3]))
print(sum([4, 5, 6]))

print()
print("------tuple------")
print() # 반복 가능한 데이터를 튜플로 반환

print(tuple('abc'))
print(tuple([1, 2, 3]))
print(tuple((1,2,3)))

print()
print("------type------")
print()

print(type('abc'))
print(type([]))
print(type(open('test', 'w')))

print()
print("------zip------")
print()

print(list(zip([1, 2, 3],[4, 5, 6])))
print(list(zip([1, 2, 3],[4, 5, 6],[7, 8, 9])))
print(list(zip('abc','def')))














