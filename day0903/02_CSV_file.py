import pandas as pd
import os

# data 폴더 만들어서 read_csv_sample.csv 넣기

# 디렉토리 아래에 있는 폴더/파일 목록
print(os.listdir("./data"))

file_path = "./data/read_csv_sample.csv"  #"data" 폴더 안에 뭐 있는지 보여줘.
print(file_path)

'''
os.path.join("폴더", "파일명")
'''

file_path2 = os.path.join('data', 'read_csv_sample.csv')
print(file_path2)

# 절대 경로 반환
cur_dir = os.getcwd()
print(cur_dir)

# 절대경로 지정
file_path3 = os.path.join(cur_dir, "data", "read_csv_sample.csv")
print(file_path3)

# 마우스 우클릭으로 절대경로 복사
file_path4 = r"C:\Users\admin\OneDrive\바탕 화면\python1\data\read_csv_sample.csv"
print(file_path4)

# 마우스 우클릭으로 상대경로 복사 
file_path5 = "data\read_csv_sample.csv"
print(file_path5)
print()

# 첫 행의 데이터가 열 이름이 된다
# 자동 정수 인덱스
df1 = pd.read_csv(file_path)
print(df1)
print()

# 첫 행부터 데이터인 경우는 None 을 주자.
df2 = pd.read_csv(file_path, header = None)
print(df2)
print()

# 1번과 동일 
def3 = pd.read_csv(file_path, index_col=None)
print(def3)
print()

def4 = pd.read_csv(file_path, index_col='c0')
print(def4)
print()
print(type(def4))
print()
def4.info()



