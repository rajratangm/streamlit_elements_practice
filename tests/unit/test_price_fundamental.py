# import os
# import sys
# import pytest
# from streamlit.testing.v1 import AppTest

# # Add server path for imports
# sys.path.append(os.path.abspath("server"))

# def test_homepage():
#     at = AppTest.from_file('server\Main.py')
#     assert at.run()

# def test_checkboxs():
    
#     at = AppTest.from_file('server/pages/PriceFundamental.py')
#     at.run()
#     checkbox = at.sidebar.checkbox[0]
#     assert checkbox.label =='Show inputs only'










# # def test_home_page():
# #     """Verify the Price and Fundamentals page loads without errors."""
# #     at = AppTest.from_file("server/Main.py").run()
    
# #     # Switch to PriceFundamental page
# #     at.switch_page("pages/PriceFundamental.py")
# #     # at.run(timeout=10)

# #     # Ensure no exceptions occurred during execution
# #     assert not at.exception, "The Price and Fundamentals page failed to load."

# # def test_sidebar_widgets():
# #     """Check if all sidebar widgets render and are functional."""
# #     at = AppTest.from_file("server/Main.py").run(timeout=10)
# #     at =at.switch_page("pages/PriceFundamental.py")

# #     # Interact with 'Show inputs only' checkbox
# #     checkbox = at.checkbox[0] #(key="Show_inputs_only")
# #     assert checkbox, "Checkbox 'Show inputs only' not found."
# #     checkbox.check().run()

# #     # Interact with select boxes
# #     # job_selectbox = at.sidebar.selectbox("Select a job")
# #     # assert job_selectbox, "Select box 'Select a job' not found."
# #     # job_selectbox.select("BC_Jan22_Aug24_G6WithRe...").run()

# #     # scenario_selectbox = at.sidebar.selectbox("Select Scenarios")
# #     # assert scenario_selectbox, "Select box 'Select Scenarios' not found."
# #     # scenario_selectbox.select("Scenario_A").run()

# #     # # Interact with multiselect
# #     # multiselect = at.sidebar.multiselect("Select areas")
# #     # assert multiselect, "Multiselect 'Select areas' not found."
# #     # multiselect.select("SYS").run()

# #     # # Interact with slider
# #     # slider = at.sidebar.slider("Select date range")
# #     # assert slider, "Date range slider not found."
# #     # slider.set_value(("2024-01-01", "2024-08-31")).run()

# #     # Ensure no exceptions occurred
#     # assert not at.exception, "Error during sidebar interactions."
