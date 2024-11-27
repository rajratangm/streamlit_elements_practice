import streamlit as st 
# st.set_page_config(page_icon="💡")


st.title('Weather Paths')

with st.sidebar:
    st.title('Select data')
    st.header('Launch Weather Paths')
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
    st.number_input('Version', min_value=1)
    st.date_input('As of')

    st.button('Run Weather Paths')

