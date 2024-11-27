import streamlit as st 


# st.set_page_config(page_icon="📥", layout='wide')
st.title('Run creator', key='title')

col1, col2 = st.columns(2)

with col1:
    st.session_state.backtest= st.checkbox('Backtest run', help='To check back test')
    st.date_input('Start date', help='Start date')
    st.date_input('End date', help='End date')

with col2:
    
    st.checkbox('Fix flows', disabled= False if st.session_state.backtest else True)
    st.number_input('Number of scenarios', value=1 if st.session_state.backtest else 200, help='Number of scenarios', min_value=0)
    st.number_input('Number of hours to aggragate', min_value=0, help='Number of hours', value=6)



st.markdown('---')
if st.checkbox('Custom as of dates for weaher scenarios', help='Custom as of dates for weather'):
    col1, col2,col3,col4 = st.columns(4)
    with col1: 
        st.selectbox('Select as of date for Load', options= [
                "2024-10-15 00:00:00",
                "2024-10-16 00:00:00",
                "2024-01-01 00:00:00",
                "2024-10-17 00:00:00",
                "2023-01-01 00:00:00",
                "2023-10-04 00:00:00",
                "2024-10-24 00:00:00",
                "2024-10-28 00:00:00",
                "2024-10-01 00:00:00",
                "2024-10-30 00:00:00"
            ])
        
        st.selectbox('Select version for Load', options = [
                "1 - First Upload with Eventail for Jera",
                "1 - First Upload with Eventail for Jera",
                "1 - First Upload with Eventail for Jera",
                "1 - First Upload with Eventail for Jera",
                "1 - First Upload with Eventail for Jera",
                "1 - First Upload with Eventail for Jera",
                "1 - First Upload with Eventail for Jera",
                "1 - First Upload with Eventail for Jera",
                "1 - First Upload with Eventail for Jera",
                "2 - This is the new Tokyo calibration with Relative Humidity dependencies - Exogenous = HeatIndex with Transformations. Note this was calibrated on EDFT data not JERA data."
            ])
    with col2:
        st.selectbox('Select as of date for Solar', options=["2024-01-01 00:00:00"])

        st.selectbox('Select version for Solar', options=[
                "1 - First Upload using EDFTs data",
                "1 - First Upload using EDFTs data",
                "1 - First Upload using EDFTs data",
                "1 - First Upload using EDFTs data",
                "1 - First Upload using EDFTs data",
                "1 - First Upload using EDFTs data",
                "1 - First Upload using EDFTs data",
                "1 - First Upload using EDFTs data",
                "1 - First Uploa"
            ])
    with col3: 
        st.selectbox('Select as of date for Wind', options=['2024-01-01 00:00:00'] )
        st.selectbox('Select version for Wind', options=[
                "1 - First Upload using EDFTs data",
                "1 - First Upload using EDFTs data",
                "1 - First Upload using EDFTs data",
                "1 - First Upload using EDFTs data",
                "1 - First Upload using EDFTs data",
                "1 - First Upload using EDFTs data",
                "1 - First Upload using EDFTs data",
                "1 - First Upload using EDFTs data",
                "1 - First Uploa      " 
            ])
    with col4:
        st.selectbox('Select as of date for Commodities', options=['2023-10-04 00:00:00'])
        st.selectbox('Select version for Commodities', options=['1 - First Upload with Commodity Scenario Generator',
                                '2 - Test'])

st.markdown('---')

if st.checkbox('Use a custom MasterGen file', help='use a custom MasterGen'):
    st.header('Custom MasterGen data')
    st.file_uploader(label='Upload a custom MasterGen file')
    # st.toast("This is a short notification!", icon="ℹ️")
    st.info("Please upload a custom MasterGen file.")  # icon can be an emoji or symbol
    uploaded_file = st.file_uploader("Upload a single file")

st.button('Reset Job ID')


col1, col2,col3 = st.columns(3)
with col1:
    st.text_input('Job ID', key="wide_input", label_visibility="collapsed", value='BC_2024-11-05_2024-11-05_G0_20241105054433')

    if st.checkbox('Insert data in the DB', help='Insert data in the DB'):
        st.selectbox('Select granularity', options=('Weekly','Hourly','Daily'), help='Select granularity', )

st.button('Create inputs only')
st.button('Run model optimisation')


st.dataframe(st.session_state.data, use_container_width=True)
st.button('Refresh jobs')
st.checkbox('Display tasks', help='Display tasks')

st.header('Check the status of the tasks for runs')
st.markdown('---')
st.text_input('Job ID')
st.selectbox('Status', options=['Created', 'Available'])
st.button('Refresh tasks')

st.header('Enable/disable a run')
st.markdown('---')
st.selectbox('Select a job ID to enable/diable', options= [
                "RUNNING",
                "Enable/disable a run",
                "Select a job ID to enable/disable",
                "BC_Jan24_Aug24_G6Param9NewGpCte",
                "BC_Jan24_Aug24_G6Param9NewGpCte",
                "BC_2024-01-01_2024-08-31_G6_20241105180501",
                "BC_Jan24_Aug24_G6Param9FuelTypes",
                "BC_Jan24_Jan24_G6TestFuelTypes",
                "BC_Jan24_Aug24_G6Params9Reserve4pRatio10p",
                "BC_Jan24_Aug24_G6Params9",
                "BC_Jan24_Aug24_G6Params8",
                "BC_Jan24_Aug24_G6Params7",
                "BC_Jan24_Aug24_G6Params6Bis"
            ])
st.button('Enable/Diable run for UI')
