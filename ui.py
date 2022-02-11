import streamlit as st
from streamlit_ace import st_ace

def title():
    st.markdown(
    "<h1 style='text-align: center; '>Treatment Tree</h1>",
    unsafe_allow_html=True,)

def code_editor():
    first, second = st.columns([11,1])
    with first:
        code = st_ace(wrap=True)
    with second:
        st.write(code)

def guide():
    st.info("This page sould be a language syntax guide")

st.set_page_config(
        page_title="T-Tree")

st.sidebar.header('Treatment Tree, a medical treatment simulator')
nav = st.sidebar.radio('',['Code Editor', 'Language Guide'])
st.sidebar.markdown(""" \n \n""")
st.sidebar.markdown(" ## [Source Code](https://github.com/anoppa/Proyecto-IA-Sim-Comp)", unsafe_allow_html=True,)
st.sidebar.markdown(""" \n""")
expander = st.sidebar.expander('Team')
expander.markdown("### We are students of CS at the MATCOM faculty of Havana University.\n #### Alejandro Beltrán Varela [alejbv] (https://github.com/alejbv)\n #### Ana P. Argüelles Terrón [anoppa] (https://github.com/anoppa) \n #### Javier A. Lopetegui González [jlopetegui98] (https://github.com/jlopetegui98)  \n #### Abel Molina Sánchez [abel1927] (https://github.com/abel1927)", unsafe_allow_html=True,)

title()
if nav == 'Code Editor':
    code_editor()
else:  
    guide()



