import streamlit as st 
from datetime import datetime
import pandas as pd 
import matplotlib.pyplot as plt

# st.set_page_config(page_icon="↔️", page_title="Flows")
st.header('flows')

with st.sidebar:
    st.header('Select data')
    st.write('Use the widget belo to explore the generation model')

    st.subheader('Select job')

    st.checkbox('Show inputs only', help="Check to show only the imputs for the run. This is useful if the ruin hasn't been solved and inserted yet. If results are not needed, this can be checked to avoid loading the results")
    
    selected_job = st.selectbox('Select a job', ['BC_Jan22_Aug24_G6WithRe...','BC_Jan22_Aug24_G6WithRe','BC_Jan22_Aug24_G6WithRe','BC_Jan22_Aug24_G6WithRe'])
    selected_scenario= st.selectbox('Select Scenarios',['Scenario_A','Scenario_B'])

    st.checkbox('Compare two jobs', help='compare jobs here')
    st.checkbox('Select all areas',help='select all areas here')

    selected_areas= st.multiselect('Select areas',['TKO','SYS','HKD','CHB','HKR','KNS','CGK'], default='TKO')

    st.selectbox('Select granual', ['Hourly','Daily','Weekly','Monthly','Quarterly','Yearly'])

    st.button('Load Data')

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
st.dataframe(filtered_data)


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
plot_graphs(filtered_data)
