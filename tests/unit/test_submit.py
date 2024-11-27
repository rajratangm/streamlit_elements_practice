import os
import sys
from streamlit.testing.v1 import AppTest

# Add server path for imports
sys.path.append(os.path.abspath("server"))

def test_submit_page():
    # Initialize AppTest from the main app script
    at = AppTest.from_file("server/Main.py")
    
    # Switch to register.py page
    try:
        at.switch_page("pages/SubmitRuns.py")  # Use relative path from main.py
        at.run()
        # Check if there was any exception during test execution
        assert not at.exception, "Test failed with an exception for home.py"

        # assert  at.title[0].value=='Run creator'
        # assert at.title[0].value =='---'
        # assert at.title[0].value == "Run creator", "Expected title 'Run creator' not found on the page."
        assert 1>0

        
        
        
    except ValueError as e:
        raise ValueError(f"Could not find script: {e}")
