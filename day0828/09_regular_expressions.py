# 정규 표현식 (regular expressions)
# 암호 해독학 (by 제이엠)

data = """
park 800905-1049118
kim  700905-1059119
"""

for line in data.split("\n"):
    print(line)

print('123'.isdigit()) #True
print('a123'.isdigit()) #False

words = ['apple', 'banana', 'mango']

print(" ".join(words)) #apple banana mango

for line in data.split("\n"):
    if "-" in line:
        name, jumin = line.split()
        front, back = jumin.split("-")
        print(name, front +"-********")

print("============== re ===============")

import re

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6}-\d{7})")
print(pat.sub("\g<1>-********",data))



    

        

 