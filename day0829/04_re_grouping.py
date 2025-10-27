# ------- !!!! 그루핑 !!!! --------- 

# 1.여러문자를 하나로 묶어서 반복처리
# 2.매치된 문자에서 원하는 부분만 추출

from ast import pattern
import re



p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?') # <re.Match object; span=(0, 9), match='ABCABCABC'>  객체를 볼 수 있음
print(m)
print(m.group())  # ABCABCABC  원하는 내용을 반환함 

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-5678")

# 이름 부분만 추출하고 싶다면?
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-5678")
print(m)
print(m.group(1))
print(m.group(2))
print(m.group(3))

# 문자열 재참조
print("-----문자열재참조")
p = re.compile(r'(\b\w+)\s+\1')
m = p.search('Paris in in the \n the spring').group()
s = p.findall('Paris in in the \n the spring')
print(m)
print(s)
print()

print("-----이메일 사용자명과 도메인 분리-------")
print()

text = '문의: hello.world@python.org'

pattern = r"([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Za-z]{2,})"

match = re.search(pattern, text)
print("전체: ",match.group(0))
print("사용자명: ",match.group(1))
print("도메인: ",match.group(2))

print("-------문장의 첫 단어 추출 (멀티라인)-------")
print()

text = """Hello world
안녕하세요 파이썬
 공백 시작
_언더 시작
Regex is powerful"""

pattern = "^\w+"

p = re.compile(pattern,re.M)
m = p.findall(text)
print(m)

print("-------중복된 글자 줄이기-------")
print()

text = "와아아 대박!!! 굿굿굿"
pattern = r"(.)\1{2,}"   # 같은 문자 3번 이상 반복된 부분 찾기

result = re.sub(pattern, r"\1\1", text)
print("중복 줄이기: ", result)


print("-------기초연습-------")
print()

text = "와아아 대박!!! 굿굿굿"
p = re.compile(r"(.)\1")

m = p.findall(text)
print(m) 

print("------전화번호 정규화(하이픈 통합)------")
# 0으로시작
# 맨 앞이 0포함 2~3자리
# 가운데가 3~4 자리
# 끝이 4 자리
text = " 고객센터 02-123-1234, 010-1234-1234, 031.123.1234, 010 1234 1234(대표)"

rx = re.compile(r"(\b0\d{1,2})[.\s-]?(\d{3,4})[-.\s]?(\d{4})")

normalized = rx.sub(r"\1-\2-\3", text)
print("정규화: ",normalized)

print()
m = rx.finditer(text)
print(m)

for i in m:
    print(i.group())

# finditer 로 각 그룹 확인 

print()

m = rx.finditer(text)
for i in m:
    print("원본: ",i.group(0),"| 지역: ",i.group(1), "| 국번호: ",i.group(2), "| 가입자: ", i.group(3))







