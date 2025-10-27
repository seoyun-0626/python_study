print('-- 클래스로 만들기 --')
print()

class Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

cal3 = Calculator()
cal4 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print()
print(cal2.add(4))
print(cal2.add(5))

print(cal3.sub(3))
print(cal4.sub(4))
print()
print(cal3.sub(4))
print(cal4.sub(5))
