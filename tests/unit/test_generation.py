# import os
import sys
from streamlit.testing.v1 import AppTest
import os
# Add server path for imports
sys.path.append(os.path.abspath("server"))

def test_generation_page():
    # Initialize AppTest from the main app script
    at = AppTest.from_file("server\pages\Generation.py")
    at.run()

    checkbox= at.tabs[0].checkbox[0]
    assert checkbox.label =='show all Unit'
    assert checkbox.check().run()

    assert at.tabs[0].get('text_input')[0]

    

    