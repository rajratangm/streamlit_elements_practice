# import os
# import sys
# from streamlit.testing.v1 import AppTest

# # Add server path for imports
# sys.path.append(os.path.abspath("server"))

# def test_load_page():
#     # Initialize AppTest from the main app script
#     at = AppTest.from_file("server/Main.py")
    
#     # Switch to register.py page
#     try:
#         at.switch_page("pages/LoadFactor.py")  # Use relative path from main.py
#         at.run()
        
#         # Check if there was any exception during test execution
#         assert not at.exception, "Test failed with an exception for LoadFactor.py"

#         # assert at.title[0].value=='PROECJT'
#         # assert at.checkbox[0].check().run()

#         # assert at.sidebar.header[4].value=='thisone'
#         # assert at.sidebar.header[0].value=='thisone'
        
        
        
#     except ValueError as e:
#         raise ValueError(f"Could not find script: {e}")
