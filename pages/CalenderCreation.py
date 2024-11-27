import streamlit as st 
# st.set_page_config(page_icon="📆", page_title='Calender')
st.title('Calender Creation')

with st.sidebar:
    st.title('Select data')
    st.markdown('Use the widget below to create a calender')
    st.selectbox('Area', options=['Japan',
    "Hokkaido",
    "Tohoku",
    "Tokyo",
    "Chubu",
    "Hokuriku",
    "Kansai",
    "Chugoku",
    "Shikoku",
    "Kyushu",
    "Okinawa"])
    st.file_uploader('Calender Mapping File')

    st.button('Run Calnder Creation')

