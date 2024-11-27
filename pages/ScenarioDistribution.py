# import streamlit as st 
# from datetime import datetime
# import pandas as pd 
# import matplotlib.pyplot as plt

# st.set_page_config(page_icon=":chart:", page_title="scenarios")
# st.header('Scenarios Distributions')

# st_example = st.container(border=False)
# tabs = st_example.tabs(["Price and Fundamental data", "Generation","Fuels"])

# with tabs[0]:
#     st.header('price and Fundamental data Distribution')
#     st.checkbox('show distribution')
# with tabs[1]:

#     st.checkbox('show distribution')
# with tabs[2]:
#     st.header('fuels distribution')
#     st.selectbox('select fuel indexes from the list', options=['1','2','3'])
#     st.checkbox('show distribution', key='tab1')

# with st.sidebar:
#     st.header('Select data')
#     st.write('Use the widget belo to explore the generation model')

#     st.subheader('Select job')

#     st.checkbox('Show inputs only', help="Check to show only the imputs for the run. This is useful if the ruin hasn't been solved and inserted yet. If results are not needed, this can be checked to avoid loading the results")
    
#     selected_job = st.selectbox('Select a job', ['BC_Jan22_Aug24_G6WithRe...','BC_Jan22_Aug24_G6WithRe','BC_Jan22_Aug24_G6WithRe','BC_Jan22_Aug24_G6WithRe'])
#     selected_scenario= st.selectbox('Select Scenarios',['Scenario_A','Scenario_B'])

#     st.checkbox('Compare two jobs', help='compare jobs here')
#     st.checkbox('Select all areas',help='select all areas here')

#     selected_areas= st.multiselect('Select areas',['TKO','SYS','HKD','CHB','HKR','KNS','CGK'], default='TKO')

#     st.selectbox('Select granual', ['Hourly','Daily','Weekly','Monthly','Quarterly','Yearly'])

#     st.button('Load Data')

#     selected_date_range=st.slider('Select date range',min_value=datetime(2024, 1, 1), max_value=datetime(2024, 8, 31),value=(datetime(2024, 1, 1), datetime(2024, 8, 31)), format="YYYY-MM-DD")

#     st.button('Refresh job list')


# data = st.session_state.data
# st.subheader('Original Data')
# st.dataframe(data)
# data['Date'] = pd.to_datetime(data['Date'])

# filtered_data = data[
#     (data['Job'] == selected_job) &
#     (data['Scenario'] == selected_scenario) &
#     (data['Area'].isin(selected_areas)) &
#     (data['Date'] >= selected_date_range[0]) &
#     (data['Date'] <= selected_date_range[1])
# ]

# # Display the filtered DataFrame
# st.subheader('Filtered Data')
# st.dataframe(filtered_data)


# def plot_graphs(filtered_data):
#     # Check if there is any data to plot
#     if filtered_data.empty:
#         st.warning("No data available for the selected filters.")
#         return
    
#     # Set the figure size
#     plt.figure(figsize=(12, 6))
    
#     # Plotting each variable over time
#     for column in filtered_data.columns:
#         if column not in ['Date', 'Job', 'Scenario', 'Area']:  # Skip non-numeric columns
#             plt.plot(filtered_data['Date'], filtered_data[column], label=column)
    
#     plt.title('Graphs of Different Variables Over Time')
#     plt.xlabel('Date')
#     plt.ylabel('Values')
#     plt.legend()
#     plt.xticks(rotation=45)
#     plt.tight_layout()  # Adjust layout to make room for the rotated labels
#     st.pyplot(plt)  # Display the plot in the Streamlit app

# # Call the function to plot the graphs
# plot_graphs(filtered_data)


import streamlit as st 
from datetime import datetime
import pandas as pd 
import matplotlib.pyplot as plt

# st.set_page_config(page_icon=":chart:", page_title="scenarios")
st.header('Scenarios Distributions')

st_example = st.container()
tabs = st_example.tabs(["Price and Fundamental data", "Generation","Fuels"])

with tabs[0]:
    st.header('Price and Fundamental Data Distribution')
    st.checkbox('Show Distribution', key='dist_checkbox_tab0')

with tabs[1]:
    st.header('Generation Data Distribution')
    st.checkbox('Show Distribution', key='dist_checkbox_tab1')

with tabs[2]:
    st.header('Fuels Distribution')
    st.selectbox('Select Fuel Indexes from the List', options=['1', '2', '3'], key='fuel_selectbox')
    st.checkbox('Show Distribution', key='dist_checkbox_tab2')

with st.sidebar:
    st.header('Select Data')
    st.write('Use the widget below to explore the generation model')

    st.subheader('Select Job')
    st.checkbox('Show Inputs Only', help="Check to show only the inputs for the run. This is useful if the run hasn't been solved and inserted yet. If results are not needed, this can be checked to avoid loading the results", key='inputs_only_checkbox')

    selected_job = st.selectbox('Select a Job', ['BC_Jan22_Aug24_G6WithRe...', 'BC_Jan22_Aug24_G6WithRe', 'BC_Jan22_Aug24_G6WithRe', 'BC_Jan22_Aug24_G6WithRe'], key='job_selectbox')
    selected_scenario = st.selectbox('Select Scenario', ['Scenario_A', 'Scenario_B'], key='scenario_selectbox')

    st.checkbox('Compare Two Jobs', help='Compare jobs here', key='compare_jobs_checkbox')
    st.checkbox('Select All Areas', help='Select all areas here', key='select_all_areas_checkbox')

    selected_areas = st.multiselect('Select Areas', ['TKO', 'SYS', 'HKD', 'CHB', 'HKR', 'KNS', 'CGK'], default='TKO', key='areas_multiselect')
    st.selectbox('Select Granularity', ['Hourly', 'Daily', 'Weekly', 'Monthly', 'Quarterly', 'Yearly'], key='granularity_selectbox')

    st.button('Load Data', key='load_data_button')

    selected_date_range = st.slider('Select Date Range', min_value=datetime(2024, 1, 1), max_value=datetime(2024, 8, 31), value=(datetime(2024, 1, 1), datetime(2024, 8, 31)), format="YYYY-MM-DD", key='date_range_slider')
    st.button('Refresh Job List', key='refresh_job_list_button')

data = st.session_state.data
# st.subheader('Original Data')
# st.dataframe(data, key='original_data_df')
data['Date'] = pd.to_datetime(data['Date'])

filtered_data = data[
    (data['Job'] == selected_job) &
    (data['Scenario'] == selected_scenario) &
    (data['Area'].isin(selected_areas)) &
    (data['Date'] >= selected_date_range[0]) &
    (data['Date'] <= selected_date_range[1])
]

# Display the filtered DataFrame
# st.subheader('Filtered Data')
# st.dataframe(filtered_data, key='filtered_data_df')

def plot_graphs(filtered_data):
    # Check if there is any data to plot
    if filtered_data.empty:
        st.warning("No data available for the selected filters.")
        return
    
    # Set the figure size
    plt.figure(figsize=(12, 6))
    
    # Plotting each variable over time
    for column in filtered_data.columns:
        if column not in ['Date', 'Job', 'Scenario', 'Area']:  # Skip non-numeric columns
            plt.plot(filtered_data['Date'], filtered_data[column], label=column)
    
    plt.title('Graphs of Different Variables Over Time')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout to make room for the rotated labels
    st.pyplot(plt)  # Display the plot in the Streamlit app

# Call the function to plot the graphs
# plot_graphs(filtered_data)
