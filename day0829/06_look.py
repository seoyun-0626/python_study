import re

#(?=...) / (?!...) / (?<=...) / (?<!...)

# 긍정형 전방탐색 (Positive Lookahead)
# 특정 문자가 "뒤에" 나오는지 확인만 하고 미포함
# 뽑고싶은게 앞에있는거지 

text = "apple1 pie and apple2 tart"

pattern = r"apple\d(?= pie)"

matches = re.findall(pattern, text)
print(matches)
print()

# 부정형 전방탐색 (Negative Lookahead)
# 특정 문자가 "뒤에" 안나오는지 확인만 하고 미포함
# 뽑고싶은게 앞에있는거지 

text = "apple1 pie and apple2 tart"

pattern = r"apple\d(?! pie)"

matches = re.findall(pattern, text)
print(matches)
print()

# 긍정형 후방탐색 (Positive Lookbehind)
# 특정 패턴이 바로 "앞에" 있는지 확인 
# 뽑고싶은게 뒤에있는거지

text = "apple pie1 and banana pie2 tart"

pattern = r"(?<=apple )pie\d"

matches = re.findall(pattern, text)
print(matches)
print()

# 부정형 후방탐색 (Positive Lookbehind)
# 특정 패턴이 바로 "앞에" 없는지 확인 
# 뽑고싶은게 뒤에있는거지


text = "apple pie1 and banana pie2 tart"

pattern = r"(?<!apple )pie\d"

matches = re.findall(pattern, text)
print(matches)
print()

text = "foo.bar auto.bat .bar send.cf"
# .bat 파일은 빼고싶다.
pattern = r'\w*[.](?!bat\b)\w*\b'    #\w앞에 \b 넣고 안넣고 차이를 기억해랏!
matches = re.findall(pattern, text)
print(matches)
