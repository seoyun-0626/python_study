# 리스트를 제이슨으로 저장/로드 하기

import json
import os

filename = "people2.json"

if not os.path.exists(filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([], f)

# 제이슨 파일 불러오기
with open(filename,"r",encoding='utf-8') as f:
    loaded_people = json.load(f)

# people = [
#     {"name":"Tom","age" :25},
#     {"name":"Jane","age" :28},
#     {"name":"Bob","age" :22}
# ]

# 사람 이름이랑 나이 입력받아서
# loaded_people 여기에 추가하기 

name = input("name : ")
age = input("age: ")

loaded_people.append({"name": name, "age":age})

# 제이슨으로 덤프하기
with open(filename, "w", encoding="utf-8") as f:
    json.dump(loaded_people, f, ensure_ascii=False, indent=4)
  

    

# Tom is 25 years old
# Jane is 28 years old
# Bob is 22 years old

print()
print(loaded_people)
print()

for person in loaded_people:
    print(f"{person['name']} is {person['age']} years old")