# https://velog.io/@anjaekk/Python-Pandas-Streamlit%EB%A1%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%8B%9C%EA%B0%81%ED%99%94-%ED%95%98%EA%B8%B0
import streamlit as st
import pandas as pd

st.title("2021 서울 교통공가 시자철 월별 하차 인원")        #타이틀 지정

df = pd.read_csv("서울교통공사.csv",encoding='cp949')      #파일 불러오기
df.set_index = df['연번']                                 #연번을 인덱스로 설정


# 데이터 저작권 정보 링크 삽입
if st.button('data copyright link'):                     # : 버튼의 이름을 data copyright link로 생성
    st.write("https://www.data.go.kr/data/15044247/fileData.do")


# raw data 전체
if st.checkbox('show raw data'):
    st.subheader('Raw data')
    st.write(df)

# 역별 하차인원
st.subheader('역별 하차인원')                           # 부제목을 달아줌
option = st.selectbox(
    'Select Line', 
    (df['역명']))      # 선택박스 만들고 csv 다운받은 df의 역명을넣음

station_data = df.loc[(df['역명'] == option )]          #해당하는 역의 row 데이터를 loc로 가져옴
station_data = station_data[station_data.columns.difference(['연번','호선','역번호','역명'])]
                                                        #그래프에 해당하지않는 자료는 제외함
s_index = station_data.index.tolist()
st.area_chart(station_data.loc[s_index[0]],use_container_width=True)
                                                        #.loc[s_index[0]]인덱스에 해당하는 row를 가져오도록하고
                                                        #use_contaioner_가로화면에 꽉차도록 설정


