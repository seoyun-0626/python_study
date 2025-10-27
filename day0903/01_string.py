import pandas as pd
import numpy as np
pd.set_option('display.unicode.east_asian_width',True)

# 텍스트로 이루어진 시리즈 배열 만들기 (자료형 미지정)
fruit_names = pd.Series(["apple", "Banana", "Cherry"])

# 시리즈 출력
print(fruit_names)
print()

# string 명시하기
fruit_name2 = pd.Series(["apple", "Banana", "Cherry"], dtype="string")
print(fruit_name2)
print()

# 자료형 지정: pd.StringDtype() 사용
fruit_name3 = pd.Series(["apple", "Banana", "Cherry"], dtype="string")
print(fruit_name3)
print()

# 자료형 반환
fruit_name4 = fruit_names.astype('string')
print(fruit_name4)
print()

### ---- 문자열 메서드 ---- ###

ser = pd.Series(["Apple_사과", "Banana_바나나", "Cherry_체리",np.nan],
                index=["First "," Second", " Third", "Fourth"])

print(ser)
print()

ser2 = ser.astype('string')
print(ser2)
print()

print(ser.str.lower())
print()
print(ser.str.upper())
print()
print(ser.str.len())
print()
print(ser.str.split("_"))
print()
print(ser.str.split("_", expand=True))
print()
print(type(ser.str.split("_", expand=True)))
print()
print(ser.str.split("_").str.get(0))
print()
print(ser.str.split("_").str.get(1))
print()

idx = ser.index
print(idx)
print(idx.str.strip())
print(idx.str.lstrip())
print(idx.str.rstrip())
print()

print('---원본 인덱스 스트립 정리하기---')
ser.index = ser.index.str.strip()
print(ser)

print("-----replace 에서 정규식 사용/미사용 ------")
print()

print(ser.str.replace("_",":", regex=False))
print()

print(ser.str.replace("[^a-zA-Z\s]", "",regex=True))
print()

print('------문자열 인덱싱 -------')
print()

print(ser.str[0]) # A B C
print()

print(ser.str[0:4])
print()

print('-------- contains 와 fullmatch -------')
print()

contains_A = ser.str.contains("A", na=False)
print(contains_A)

contains_pattern = ser.str.contains(r"[AB][a-z]+")  # (A|B) 도가능 # [A|B] -- A와 B와 | 를 각각 그대로 인식
print(contains_pattern)
print()

fullmatch_pattern = ser.str.fullmatch(r"[AB][a-z가-힣_]+")
print(fullmatch_pattern)
print()




