import streamlit as st
from streamlit_card import card
from streamlit_elements import elements, mui
import streamlit as st 
from datetime import datetime
import pandas as pd 
# import matplotlib.pyplot as plt

# Function to render cards using `streamlit-card`
st.session_state.data = pd.read_csv('practice_data.csv')
def render_cards(options, callback_key):
    """Display cards based on a list of options and set the selected card."""
    for option in options:
        if card(title=option, text=f"Details about {option}", key=f"card-{option}"):
            st.session_state[callback_key] = option

# Page functions
def home_page():
    st.title(f"Home Page{st.session_state.page}lllllllllllllllllllllll")
    st.write("Welcome to the Home Page!")
    

    st.markdown("""
    Generation Model UI ⚡
    Welcome to the Generation Model UI! 👋 This app enables the user to analyse results generated with the Generation Model, as well as to launch runs.
    The app is divided into several sections, each of which focuses on a different aspect of the model:

    Generation Model: This section allows the user to analyse results generated with the Generation Model and to launch runs.

    Price and Fundamental Data: This page allows the user to analyse price and fundamental data.
    Generation: This page allows the user to analyse generation data.
    Load Factors: This page allows the user to analyse load factors.
    Flows: This page allows the user to analyse flows.
    Fuel Prices: This page allows the user to analyse fuel prices.
    Submit runs: This page allows the user to submit runs to be solved by the Generation Model and using custom parameters. It also allows the user to control the progress of existing runs.
    Weather Scenarios: This page allows the user to analyse and launch weather scenarios generation (Load, Solar, Wind,..).

    Load Forecast - Calendar Creation: This page allows the user to create a calendar for a load forecast.
    Load Forecast - Calibration: This page allows the user to change parameters and calibrate the load forecast model.
    Load Forecast - Weather Paths: This page allows the user to execute a forecast for specified area. (Pages to be added: Solar and Wind scenarios)
    Commodities scenarios: This page allows the user to analyse and launch commodities scenarios generation. This includes the fuel indexes prices to be used in the Generation Model. (Section to be impemented)

    ⏲️
    Click here to add/modified scheduled jobs using Azure Logic Apps.

    👾
    Useful links for developers:

    Generation model UI - repository (JapanGenerationModelUI) and app
    Backend web app - repository (generation-model-backend-app) and app
    Input generation app - repository (generation-model-inputs-app) and app (generation-model-inputs-app)
    Generation model batch service - repository (JapanGenerationModelDocker) and app - generationmodelbatch
    Input generation package - repository (GenerationModelInputs)
    Supply and demand model package - repository (Japan_GenerationModel)
    Generation Model - System Overview

    """ )



def about_page():
    st.title("About Page")
    st.write("This is the About Page.")


    

    st.header('Price and Fundamentals')


    data = st.session_state.data

    st.subheader('Original Data')

    val= data.iloc[:, :-1]
    st.dataframe(val,use_container_width=True)

    data['Date'] = pd.to_datetime(data['Date'])

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
    fVal = filtered_data.iloc[:, :-1]
    st.dataframe(fVal, use_container_width=True)

def contact_page():
    st.title("Contact Page")
    st.write("This is the Contact Page.")


    st_example = st.container(border=False)
    st_example.markdown("### st-link-analysis: Extended Example")
    tabs = st_example.tabs(["Generation 1", "Generation 2"])



    with tabs[0]:
        st.header('You have selected generation unit ')
        st.checkbox('show all Unit')
        if not st.session_state.data.empty:
            st.text_input('Enter units separated by white space', help='Units enting')
            st.text_input('Or select units from the list', help='Select units from list')
            st.checkbox('Load actual generation data', help='load actualt data')
            st.checkbox('load unit costs', help='load unit costs')
            st.selectbox('Select plants', options=[
                        "TokaiDaini",
                        "Kashiwazaki",
                        "NakosoIGCC",
                        "Hitachinaka",
                        "Hirono",
                        "ShinHitachinaka",
                        "ShinYokosuka",
                        "Isogo",
                        "Nakoso"
                    ])
            st.checkbox('Show distribution', help='show distribution')

    with tabs[1]:
        st.header('Generation by Fuel')
        st.selectbox('Select fuel types from the list', options=[
                    "LNG",
                    "COAL",
                    "OIL",
                    "FOREX",
                    "NUCLEAR",
                    "JWLNG",
                    "OTHER"
                ], help='Select guel types')
        st.checkbox('show distribution', help='Show distribution')



# Multi-page functions
def page_1():
    st.title("Page 1")
    st.write("This is the first option's detailed page.")
    st.checkbox("Sample Checkbox")

def page_2():
    st.title("Page 2")
    st.write("This is the second option's detailed page.")
    st.checkbox("Another Checkbox")

def page_3():
    st.title("Page 3")
    st.write("This is the third option's detailed page.")

# Navbar using `streamlit-elements`
def render_navbar():
    # Create Navbar with buttons
    with elements("navbar"):
        with mui.AppBar(position="sticky", sx={"backgroundColor": "#6200ea"}):
            with mui.Toolbar:
                mui.Typography("Dynamic Navbar", variant="h6", sx={"flexGrow": 1})
                with st.sidebar:
                    val = st.checkbox('this is it')
                # Streamlit Button for 'Home'
                if st.button("Home", key="home_button"):
                    st.session_state.page = "home"
                    if val:
                        st.markdown('HOME and MARKED')
                
                # Streamlit Button for 'About'
                if st.button("About", key="about_button"):
                    st.session_state.page = "about"
                    if val:
                        st.markdown('HOME and MARKED')
                
                # Streamlit Button for 'Contact'
                if st.button("Contact", key="contact_button"):
                    st.session_state.page = "contact"
                    if val:
                        st.markdown('HOME and MARKED')
    # Determine and render the appropriate page
    page = st.session_state.get("page", "home")
    if page == "home":
        home_page()
    elif page == "about":
        about_page()
    elif page == "contact":
        contact_page()
    else:
        st.error("Page not found!")

# Main Streamlit App
def main():
    st.set_page_config(page_title="Dynamic Navigation", layout="wide")

    # Initialize session state
    if "main_card" not in st.session_state:
        st.session_state.main_card = None
    if "sub_card" not in st.session_state:
        st.session_state.sub_card = None
    if "page" not in st.session_state:
        st.session_state.page = "home"

    # Define main cards and sub-options
    main_cards = ["Card 1", "Card 2", "Card 3", "Card 4"]
    sub_card_options = {
        "Card 1": ["Option 1A", "Option 1B", "Option 1C"],
        "Card 2": ["Option 2A", "Option 2B", "Option 2C"],
        "Card 3": ["Option 3A", "Option 3B", "Option 3C"],
        "Card 4": ["Option 4A", "Option 4B", "Option 4C"],
    }

    # Map sub-options to pages
    page_map = {
        "Option 1A": render_navbar,  # Integrates navbar with Option 1A
        "Option 2A": page_2,
        "Option 3A": page_3,
    }

    # Main logic
    if st.session_state.main_card is None:
        render_cards(main_cards, "main_card")
    elif st.session_state.sub_card is None:
        selected_main_card = st.session_state.main_card
        st.header(f"Options for {selected_main_card}")
        render_cards(sub_card_options[selected_main_card], "sub_card")
    else:
        selected_sub_card = st.session_state.sub_card
        if selected_sub_card in page_map:
            page_map[selected_sub_card]()
        else:
            st.error("Invalid selection!")

    # Navigation buttons to reset state
    if st.button("Go Back"):
        if st.session_state.sub_card is not None:
            st.session_state.sub_card = None
        else:
            st.session_state.main_card = None


if __name__ == "__main__":
    main()

# import streamlit as st
# from streamlit_card import card
# from streamlit_elements import elements, mui
# from streamlit_option_menu import option_menu  # Import option_menu from streamlit-option-menu

# # Function to render cards using `streamlit-card`
# def render_cards(options, callback_key):
#     """Display cards based on a list of options and set the selected card."""
#     # Create a two-column layout to fit cards in a grid
#     columns = st.columns(len(options))  # Number of columns is equal to the number of options
    
#     for i, option in enumerate(options):
#         with columns[i]:  # Assign each card to a column
#             # Render the card using streamlit-card
#             if card(title=option, text=f"Details about {option}", key=f"card-{option}", image="https://via.placeholder.com/150"):
#                 # Set the selected option in session state when the card is clicked
#                 st.session_state[callback_key] = option

# # Page functions
# def home_page():
#     st.title("Home Page")
#     st.write("Welcome to the Home Page!")
#     st.image("https://via.placeholder.com/800x300.png?text=Home+Page")

# def about_page():
#     st.title("About Page")
#     st.write("This is the About Page.")
#     st.image("https://via.placeholder.com/800x300.png?text=About+Page")

# def contact_page():
#     st.title("Contact Page")
#     st.write("This is the Contact Page.")
#     st.image("https://via.placeholder.com/800x300.png?text=Contact+Page")

# # Navbar using `streamlit-option-menu`
# def render_navbar():
#     # Use `option_menu` to create the navbar
#     selected = option_menu(
#         menu_title="Main Menu",  # Title of the menu
#         options=["Home", "Documentation", "Examples", "Community", "About"],  # Options in the menu
#         icons=["house", "book", "star", "people", "info-circle"],  # Optional icons for each option
#         menu_icon="cast",  # Icon for the menu
#         default_index=0,  # Default selected menu option
#         orientation="vertical",  # Menu layout
#         styles={
#             "container": {"padding": "5px", "background-color": "#f1f1f1"},
#             "icon": {"color": "blue", "font-size": "20px"},
#             "nav-link": {"font-size": "18px", "text-align": "center"},
#         },
#     )

#     # Store selected page in session state
#     st.session_state.page = selected

#     # Render the page content based on the selected navbar item
#     if selected == "Home":
#         home_page()
#     elif selected == "About":
#         about_page()
#     elif selected == "Contact":
#         contact_page()
#     else:
#         st.write("Page not found!")

# # Main Streamlit App
# def main():
#     st.set_page_config(page_title="Dynamic Navigation", layout="wide")

#     # Initialize session state if not already set
#     if "page" not in st.session_state:
#         st.session_state.page = "Home"  # Default page is Home

#     # Create a card selection menu using `render_cards`
#     options = ["Home", "About", "Contact"]
#     render_cards(options, "selected_page")

#     # Render the navbar
#     render_navbar()

# if __name__ == "__main__":
#     main()
