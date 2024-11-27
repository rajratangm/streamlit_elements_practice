import streamlit as st 
# st.set_page_config(page_icon="🔌", page_title='Calibration')



st.title('Weather Paths')

with st.sidebar:
    st.title('Select data')
    st.markdown('Use the widgets below to trigger a calibration run. Please ensure that you re-upload the hyperparameters file if any changes are made to the file between calibration runs.')
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
    st.number_input('Hyperparamenter ID', min_value=0)
    st.file_uploader('Hyperparameters File')

    st.button('Run Calibration')

