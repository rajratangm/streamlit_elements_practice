import os
import sys
from streamlit.testing.v1 import AppTest

# Add server path for imports
sys.path.append(os.path.abspath("server"))

def test_main_page():
    at = AppTest.from_file("server/Main.py")
    at.run()
    assert not at.exception, "Test failed with an exception for main.py"
