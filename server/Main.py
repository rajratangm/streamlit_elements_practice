import streamlit as st
from datetime import datetime
import pandas as pd

import plotly.express as px
import numpy as np


st.set_page_config(     page_title="Ex-stream-ly Cool App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     })

st.markdown("""
<style>

header.stAppHeader.st-emotion-cache-12fmjuu.ezrtsby2 {
    background-color: #1a1c1f;
}
svg.eyeqlp53.st-emotion-cache-qsoh6x.ex0cdmw0 {
    background-color: white;
}
            .st-emotion-cache-6qob1r.eczjsme11 {
    background-color: #1a1c1f;
            color:white;
  transition: transform 0.3s ease-in-out;
            
}
          button.st-emotion-cache-n5r31u.ef3psqc19:hover {
    
    color: white; /* Change text color */
    cursor: pointer; /* Show pointer on hover */
}
                     
            button.st-emotion-cache-n5r31u.ef3psqc19(:after) {
  
    background: transparent;
            border:none;
}
            
            button.st-emotion-cache-n5r31u.ef3psqc19 {
    background-color: #1a1c1f !important;
    border: none;
}
button.st-emotion-cache-n5r31u.ef3psqc19:hover {
    background-color: #1a1c1f !important;
    
    cursor: pointer;
}
            
            section.stMain.st-emotion-cache-bm2z3a.ea3mdgi8 {
            background-color: #353a40 !important;
            color:white;
            position: relative;
}
            details.st-emotion-cache-1h9usn1.eqpbllx3 {
    border: none;
}
    
            
 svg.eyeqlp53.st-emotion-cache-qsoh6x.ex0cdmw0 {
    background-color: #1a1c1f !important;
            bordern:none !important;
}
      
            


button.st-emotion-cache-1igbibe.ef3psqc19 {
    color: black;
}

   

            .st-emotion-cache-1dtefog {
            font-size:50px;
    display: flex;
    gap: 0.5rem;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-flex: 1;
    flex-grow: 1;
}

/* Add hover effect */
.st-emotion-cache-1dtefog:hover {
    background-color: rgba(255, 255, 255, 0.1) !important; /* Change background color on hover */
    cursor: pointer; /* Change cursor to pointer to indicate interactivity */
    transform: scale(1.02); /* Slightly enlarge the element */
    transition: all 0.01s ease; /* Smooth transition for hover effects */
            color:#33a0d7;
            border-radius:5px;
        font-size:50rem;
            
}
.svg.eyeqlp53.st-emotion-cache-1b2ybts.ex0cdmw0 {
    display: inline-grid
;
    visibility: hidden;
}
            

            .st-emotion-cache-p5msec {
    position: relative;
    display: flex
;
    width: 100%;
    font-size: 50px;
   padding:0;
    list-style-type: none;
}
            

            .st-emotion-cache-1puwf6r p {
    word-break: break-word;
    margin-bottom: 0px;
    font-size: 20px;
}
            
            .st-emotion-cache-1puwf6r p {
    word-break: break-word;
    margin-bottom: 0px;
    font-size: 20px;
    padding-left: 1rem;
}
            
            .st-emotion-cache-6qob1r.eczjsme11 {
    background-color: #1a1c1f;
    color: white;
    box-shadow: 0px 4px 10px rgba(31, 20, 40, 0.7);
    transition: transform 0.3s ease-in-out;
}

            
            .st-emotion-cache-s16by7 {
    display: flex
;
    -webkit-box-align: center;
    align-items: center;
    padding-top: 0px;
    padding-bottom: 0px;
    background: rgb(0,0,0);
}
            
            .st-f7 {
    display: block;
    background-color: #1a1c1f !important;
            color:white;
            
}
                  .st-f7:hover {
    display: block;
    background-color: gray !important;
            
}
            
            .st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl {
    background-color: #1a1c1f !important;
            color:white;
}
            .st-ak.st-al.st-as.st-cl.st-bg.st-cm.st-bl {
    background-color: #1a1c1f !important;
}
            .st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-dr.st-ar.st-c4.st-c5.st-bk.st-c7 {
    background-color: #1a1c1f !important;
}

            
 .st-dc {
    background: transparent;
            
}
            .st-dt {
     background-color: #1a1c1f !important;
}
.st-es {
    border-left-color: skyblue;
}
            .st-ev {
    border-bottom-color: skyblue;
}
            .st-eu {
    border-top-color: skyblue;
}
            .st-et {
    border-right-color: skyblue;
}
            
            .st-di {
    border-color: skyblue;
}
            
            .st-dh:hover {
    margin-right: 2px;
            background-color:#1a1c1f !important;
}
            
            p{
            
            color:white;}

            button.st-emotion-cache-1igbibe.ef3psqc19 {
                border-radius: 50px;
    background: green;
    border: 50px;
    border: 2px solid pink;
}
            button.st-emotion-cache-1igbibe.ef3psqc19:hover{
            border: 2px solid brown;
            }

            .st-emotion-cache-n5r31u:focus::after {
   
    color: rgb(255, 75, 75);
}
""", unsafe_allow_html=True)





st.logo(r'assets/logo.svg', icon_image=r'assets/logo-sm.svg',size='large')


if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Define page content functions
def home():

    st.header('this is header')
def price_and_fundamental():
    st.header('Price and Fundamentals')

    # Generate data dynamically for filters
    if "data" not in st.session_state:
        np.random.seed(42)  # For reproducible random data
        dates = pd.date_range(start='2024-01-01', end='2024-08-31', freq='D')
        jobs = ['Job_A', 'Job_B', 'Job_C', 'Job_D']
        scenarios = ['Scenario_A', 'Scenario_B', 'Scenario_C']
        areas = ['TKO', 'SYS', 'HKD', 'CHB', 'HKR', 'KNS', 'CGK']

        # Create a DataFrame with all combinations of Jobs, Scenarios, and Areas
        data = pd.DataFrame({
            'Date': np.random.choice(dates, 1000),
            'Job': np.random.choice(jobs, 1000),
            'Scenario': np.random.choice(scenarios, 1000),
            'Area': np.random.choice(areas, 1000),
            'Value': np.random.randint(100, 1000, 1000)  # Random values
        })
        st.session_state.data = data

    data = st.session_state.data



    # Ensure Date column is in datetime.date format for compatibility
    data['Date'] = pd.to_datetime(data['Date']).dt.date

    col1, col2 = st.columns(2)

    st.header('Select Data')
    st.write('Use the widget below to explore the generation model')

    # Left Column Filters
    with col1:
        selected_job = st.selectbox(
            'Select a job',
            sorted(data['Job'].unique())  # Populate based on available data
        )
        selected_scenario = st.selectbox(
            'Select Scenario',
            sorted(data['Scenario'].unique())  # Populate based on available data
        )

        col1_col1, col1_col2, col1_col3 = st.columns(3)

        with col1_col1:
            compare_jobs = st.checkbox('Compare two jobs', help='Compare jobs here')
        with col1_col2:
            select_all_areas = st.checkbox('Select all areas', help='Select all areas here')
        with col1_col3:
              show_inputs_only = st.checkbox(
                  'Show inputs only',
                  help="Check to show only the inputs for the run. Useful if the run hasn't been solved and inserted yet.",
                  key="Show_inputs_only"
              )
              col3_1, col3_2 = st.columns(2)
              with col3_1:
                  if st.button('Refresh job list'):
                      st.experimental_rerun()
              with col3_2:
                  st.button('Load Data')

    # Right Column Filters
    with col2:
        if select_all_areas:
            selected_areas = data['Area'].unique().tolist()
        else:
            selected_areas = st.multiselect(
                'Select areas',
                sorted(data['Area'].unique()),  # Populate based on available data
                default=['TKO']
            )

        selected_granularity = st.selectbox(
            'Select granularity',
            ['Daily', 'Weekly', 'Monthly', 'Quarterly', 'Yearly']
        )

        selected_date_range = st.slider(
            'Select date range',
            min_value=data['Date'].min(),
            max_value=data['Date'].max(),
            value=(data['Date'].min(), data['Date'].max()),
            format="YYYY-MM-DD"
        )



    # Filter data
    filtered_data = data[
        (data['Job'] == selected_job) &
        (data['Scenario'] == selected_scenario) &
        (data['Area'].isin(selected_areas)) &
        (data['Date'] >= selected_date_range[0]) &
        (data['Date'] <= selected_date_range[1])
    ]

    # Aggregate data based on selected granularity
    if not filtered_data.empty:
        if selected_granularity != 'Daily':
            filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])

            if selected_granularity == 'Weekly':
                filtered_data['Date'] = filtered_data['Date'].dt.to_period('W').apply(lambda r: r.start_time)
            elif selected_granularity == 'Monthly':
                filtered_data['Date'] = filtered_data['Date'].dt.to_period('M').apply(lambda r: r.start_time)
            elif selected_granularity == 'Quarterly':
                filtered_data['Date'] = filtered_data['Date'].dt.to_period('Q').apply(lambda r: r.start_time)
            elif selected_granularity == 'Yearly':
                filtered_data['Date'] = filtered_data['Date'].dt.to_period('Y').apply(lambda r: r.start_time)

            # Aggregate by mean Value for the granularity
            filtered_data = filtered_data.groupby(['Date', 'Area'], as_index=False)['Value'].mean()



        # Plot with Plotly
    st.subheader('Interactive Plot')
    if not filtered_data.empty:
        fig = px.line(
            filtered_data,
            x='Date',
            y='Value',
            color='Area',
            title=f'Filtered Data Over Time ({selected_granularity})'
        )

        # Update layout to make the background darker
        fig.update_layout(
            plot_bgcolor='rgb(30,30,30)',  # Dark gray for the plot area
            paper_bgcolor='rgb(20,20,20)',  # Darker gray for the outer area
            font=dict(color='white'),  # White font color for text
            title_font=dict(size=20, color='white'),  # Title font color and size
            xaxis=dict(showgrid=False, color='white'),  # White x-axis labels
            yaxis=dict(showgrid=True, gridcolor='gray', color='white')  # White y-axis labels and gray gridlines
        )

        st.plotly_chart(fig, use_container_width=True)

        st.subheader('Original Data')
        st.dataframe(data, use_container_width=True)
        st.header('Filtered dataframe')
        if not filtered_data.empty:
            st.dataframe(filtered_data, use_container_width=True)
        
    else:
        st.write("No data available for the selected filters.")
    
def generation():
    st.title("🏭 Generation")
    st.write("Details about generation.")

def load_factors():
    st.title("🌩️ Load Factors")
    st.write("Details about load factors.")

def calendar_creation():
    st.title("📆 Calendar Creation")
    st.write("Create and manage calendars.")

def calibration():
    st.title("🔌 Calibration")
    st.write("Calibrate your models.")

def weather_paths():
    st.title("🌦️ Weather Paths")
    st.write("Weather-related data.")

def app_page():
    st.title("📊 PyGWalker Integration")
    st.write("Interactive visualizations with PyGWalker.")

# Sidebar menu with expanders
with st.sidebar:
    
    with st.expander("Home", expanded=True):
        if st.button("🏚️ Home"):
            st.session_state.current_page = "home"

    with st.expander(" Generation Model"):
        if st.button("🗾Price & Fun"):
            st.session_state.current_page = "price_and_fundamental"


        if st.button("🏭 Generation"):
            st.session_state.current_page = "generation"
        if st.button("🌩️ Load Factors"):
            st.session_state.current_page = "load_factors"

    with st.expander("Load Scenarios"):
        if st.button("📆 Calendar Creation"):
            st.session_state.current_page = "calendar_creation"
        if st.button("🔌 Calibration"):
            st.session_state.current_page = "calibration"
        if st.button("🌦️ Weather Paths"):
            st.session_state.current_page = "weather_paths"

    with st.expander("Commodities Scenarios"):
        if st.button("📊 PyGWalker"):
            st.session_state.current_page = "app_page"

# Render the selected page
if st.session_state.current_page == "home":
    home()
elif st.session_state.current_page == "price_and_fundamental":
    price_and_fundamental()
elif st.session_state.current_page == "generation":
    generation()
elif st.session_state.current_page == "load_factors":
    load_factors()
elif st.session_state.current_page == "calendar_creation":
    calendar_creation()
elif st.session_state.current_page == "calibration":
    calibration()
elif st.session_state.current_page == "weather_paths":
    weather_paths()
elif st.session_state.current_page == "app_page":
    app_page()

