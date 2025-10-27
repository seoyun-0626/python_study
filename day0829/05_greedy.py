import re

s = '<html><head><title>Title</title>'

print(len(s))

print(re.match('<.*>',s).span())

print(re.match('<.*>',s).group())

print(re.match('<.*?>',s).group())   # 저 모양의 최소단위를 뽑아옴

# *? +? {m,n}? < m번으로 해라 

text = '123456'
pattern = r'\d{2,4}?'

matches = re.findall(pattern, text)
print(matches)

print("--------괄호 안의 내용 뽑기--------")
print()

text = '오늘 메뉴는 (자장면) 과 (오징어덮밥) 입니다.'

# ['(자장면)','(오징어덮밥)']

pattern = r'\((.*?)\)'    # 이건 괄호안의 내용만 뽑기 
pattern2 = r'\(.*?\)'
pattern3 = r'\(\w{3,5}\)'
menu = re.findall(pattern, text)
menu2 = re.findall(pattern2, text)
menu3 = re.findall(pattern3, text)
print(menu)
print(menu2)
print(menu3)
