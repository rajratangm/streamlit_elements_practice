
import streamlit as st 



# st.set_page_config(page_icon='🏭', page_title='Generation')


st_example = st.container(border=False)
tabs = st_example.tabs(["Generation 1", "Generation 2"])



with tabs[0]:
    st.header('You have selected generation unit ')
    st.checkbox('show all Unit')
    # if not st.session_state.data.empty:
    st.text_input('Enter units separated by white space', help='Units enting', key='1')
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

