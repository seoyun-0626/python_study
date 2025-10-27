import pandas as pd
import glob

# 1. 모든 연도 파일 읽기 (경로 맞춰야 함)
files = glob.glob("./data/아파트(매매)_실거래가_*.xlsx")

dfs = []
for file in files:
    df = pd.read_excel(file, skiprows=12, usecols=['시군구', '계약년월', '거래금액(만원)'])
    
    # 거래금액 숫자로 변환
    df['거래금액(만원)'] = df['거래금액(만원)'].astype(str).str.replace(",", "").astype(int)
    
    dfs.append(df)

# 2. 합치기
df_all = pd.concat(dfs, ignore_index=True)

# 3. 저장
df_all.to_csv("apartment_2015_2025_clean.csv", index=False, encoding="utf-8-sig")

print(df_all.head())
print("전체 데이터 크기:", df_all.shape)


print(df_all.head())        # 앞부분 5행
print(df_all.tail())        # 뒷부분 5행
print("전체 데이터 크기:", df_all.shape)  # 합쳐진 행/열 개수
print(df_all.columns)       # 컬럼 확인


# 2015~ 2025 년도까지 시군구, 계약년월, 거래금액 만 뽑아서 csv로 저장 

