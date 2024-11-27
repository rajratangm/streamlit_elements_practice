import streamlit as st
from datetime import datetime
import pandas as pd
from streamlit_modal import Modal
import plotly.express as px


st.header('Price and Fundamentals')
# st.session_state.data
data = st.session_state.data

st.subheader('Original Data')

val= data.iloc[:, :-1]
# st.dataframe(val,use_container_width=True)

data['Date'] = pd.to_datetime(data['Date'])

col1, col2 = st.columns(2)

st.header('Select data')
st.write('Use the widget belo to explore the generation model')
with col1:
    selected_job = st.selectbox('Select a job', ['BC_Jan22_Aug24_G6WithRe...','BC_Jan22_Aug24_G6WithRe','BC_Jan22_Aug24_G6WithRe','BC_Jan22_Aug24_G6WithRe'])
    selected_scenario= st.selectbox('Select Scenarios',['Scenario_A','Scenario_B'])

    col1_col1, col1_col2, col1_col3 = st.columns(3)

    with col1_col1:
        st.checkbox('Compare two jobs', help='compare jobs here')
    with col1_col2:
        st.checkbox('Select all areas',help='select all areas here')
    with col1_col3:
        st.checkbox('Show inputs only', help="Check to show only the imputs for the run. This is useful if the ruin hasn't been solved and inserted yet. If results are not needed, this can be checked to avoid loading the results", key="Show_inputs_only")


with col2:
    selected_areas= st.multiselect('Select areas',['TKO','SYS','HKD','CHB','HKR','KNS','CGK'], default='TKO')

    st.selectbox('Select granual', ['Hourly','Daily','Weekly','Monthly','Quarterly','Yearly'])

    if st.button('Load Data'):
        checked =st.checkbox('error')
        try:
            
            pd.read_csv('this.csv')
                # Simulating a failure
                # raise FileNotFoundError("File not found: 'this.csv'")
        except Exception as e:
            # st.session_state["show_modal"] = True
            # st.toast('this is error')
            modal = Modal(key='modal', title='FileNotFound')
            with modal.container():
                st.subheader('please check the file location file is not found')
                st.markdown('<p>this is it</p> ')


    selected_date_range=st.slider('Select date range',min_value=datetime(2024, 1, 1), max_value=datetime(2024, 8, 31),value=(datetime(2024, 1, 1), datetime(2024, 8, 31)), format="YYYY-MM-DD")

    st.button('Refresh job list')


data = st.session_state.data
st.subheader('Original Data')
st.dataframe(data)
data['Date'] = pd.to_datetime(data['Date'])

filtered_data = data[
    (data['Job'] == selected_job) &
    (data['Scenario'] == selected_scenario) &
    (data['Area'].isin(selected_areas)) &
    (data['Date'] >= selected_date_range[0]) &
    (data['Date'] <= selected_date_range[1])
]

# Display the filtered DataFrame
st.subheader('Filtered Data')
fVal = filtered_data.iloc[:, :-1]
st.dataframe(fVal, use_container_width=True)

