import streamlit as st
from Test.high_probability_to_win_Test import high_probability_to_win_Test
#from TreatmentTree.node import Node
from main import main
from time import time

st.set_page_config(
        page_title="T-Tree Test Ui")

st.markdown("<h1 style='text-align: center; '>Treatment Tree Test UI</h1>",unsafe_allow_html=True,)

st.write("")
st.write("")

n = st.text_input(label="number of simulations", value=1000)

if st.button('Run the default test'):
    start = time()
    tree =  high_probability_to_win_Test(main, 1, 240, int(n))
    end = time()
    st.info(f"Time execution: {round(end-start,4)}s")
    
    tree.calculate_probability()
    best_branch = tree.best_branch()
    st.write('Best branch average final state')
    st.write(best_branch[-1].get_average_final_state())
    

    st.write('best branch')
    st.write('')
    st.write('initial')
    for node in best_branch[1:]:
        st.write((f"{node.value} ------->> hora:{node.created_time} ------>>> probability:{round((node.probability_value))}%"))
