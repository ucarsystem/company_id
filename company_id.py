import pandas as pd
import streamlit as st

# 파일 로드
def load_data():
    file_path = "인천ID.xlsx"
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='ID목록')
    return df

df = load_data()

# '퇴사여부' 컬럼의 NaN 값을 빈 문자열로 변경
df['퇴사여부'] = df['퇴사여부'].fillna('')

# Streamlit UI 설정
st.title("운수사별 운전자 명단 조회")

# 운수사 선택
driver_companies = df['운수사'].unique()
selected_company = st.selectbox("운수사를 선택하세요", driver_companies)

# 선택된 운수사의 운전자 필터링
df_filtered = df[df['운수사'] == selected_company]

# 검색창을 추가하여 운전자 검색
search_name = st.text_input("운전자 이름을 입력하세요")

if search_name:
    df_filtered = df_filtered[df_filtered['운전자이름'].str.contains(search_name, na=False, case=False)]

# 결과 출력
st.dataframe(df_filtered)
