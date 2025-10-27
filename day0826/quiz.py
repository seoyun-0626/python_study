# 더하기 빼기 곱하기 나누기 제곱 를 입력받기
# 숫자 두개 를 입력 받기
# 함수 하나에 '연산종류' '숫자두개' 넣어서
# 결과 이쁘게 출력하기
# (0으로 나눌 수 없습니다. 이경우는 따로 케어해주세요.)


def add_mul(choice,x,y):
    if choice == "더하기":
        return f'{x} + {y} = {x + y}'
    elif choice == "빼기":
        return f'{x} - {y} = {x - y}'
    elif choice == "곱하기":
        return f'{x} * {y} = {x * y}'
    elif choice == "나누기":
        if y == 0:
            return "0으로 나눌 수 없습니다."
        else:
            return f'{x} / {y} = {x / y}'
    elif choice == "제곱":
        return f'{x} ** {y} = {x ** y}'
    else:
        return "똑바로 입력하세요!"
while True:
    a = input('( 더하기 / 빼기 / 곱하기 / 나누기 / 제곱 ) 중에 선택하세요 (종료를 원하시면 e 를 치세요) : ')
    if a == 'e':
        print("ㅇㅇ ㅃㅇ")
        break
    b = int(input("1번숫자: "))
    c = int(input("2번숫자: "))


    result = add_mul(a,b,c)
    print(f'결과: {result}')