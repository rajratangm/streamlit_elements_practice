
import json
import streamlit as st



# -------- App --------
st_example = st.container(border=False)
st_example.markdown("### st-link-analysis: Extended Example")
tabs = st_example.tabs(["Fuel option 1", "Fuel Option 2"])

with tabs[0]:
    st.markdown("This is Fuel Option 1 ")
    st.header('Fuel Option 1')

with tabs[1]:
    st.markdown("this i Fuel option two")


# with tabs[2]:
#     st.markdown("##### Modifying layout")
#     st.caption(
#         "No available JSON editor, so please ensure entered text is a valid JSON"
#     )
#     layout = display_layout_editor(layout)
#     height = st.slider("Height", 250, 750, 400)




