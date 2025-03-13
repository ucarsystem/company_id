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
st.title("👥운전자 명단 조회")

# 운수사 선택 (맨 앞에 '운수사를 선택해주세요' 추가)
driver_companies = ["운수사를 선택해주세요"] + list(df['운수사'].unique())
selected_company = st.selectbox("운수사를 선택하세요", driver_companies, index=0)

# 선택된 운수사가 '운수사를 선택해주세요'가 아닐 때만 필터링 실행
if selected_company != "운수사를 선택해주세요":
    df_filtered = df[df['운수사'] == selected_company]

    # 검색창 추가 (이름 & ID 검색 가능)
    search_query = st.text_input("운전자 이름 또는 ID를 입력하세요")

    if search_query:
        df_filtered = df_filtered[
            df_filtered['운전자이름'].str.contains(search_query, na=False, case=False) |
            df_filtered['운전자ID'].astype(str).str.contains(search_query, na=False, case=False)
        ]

    # 결과 출력
    st.dataframe(df_filtered)
else:
    st.write("운수사를 선택하면 운전자 명단이 표시됩니다.")
