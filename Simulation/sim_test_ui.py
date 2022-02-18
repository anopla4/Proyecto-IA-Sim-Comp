import streamlit as st
import streamlit.components.v1 as components
from Test.numerical_sim_test import numerical_sim_test
from TreatmentTree.pyvis_draw import visualize_graph_pyvis, visualize_branch_pyvis
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
    tree =  numerical_sim_test(main, 1, 240, int(n))
    end = time()
    st.info(f"Time execution: {round(end-start,4)}s")
    
    ##tree.calculate_probability()
    best_branch = tree.best_branch()
    st.write('Best branch average final state')
    st.write(best_branch[-1].get_average_final_state())
    
    st.write('best branch')
    st.write('')
    st.write('initial')
    for node in best_branch[1:]:
        st.write((f"{node.value} ------->> hora:{node.created_time} ------>>> probability:{round((node.probability_value))}%"))

    path = "Test/html_files/"
    try:
        visualize_branch_pyvis(best_branch, show=False, path=path+'branch.html')
        #drug_net.save_graph(f'{path}/branch.html')
        HtmlFileB = open(f'{path}/branch.html', 'r', encoding='utf-8')

    # Save and read graph as HTML file (locally)
    except:
        visualize_branch_pyvis(best_branch, show=False, path=path+'branch.html')
        #drug_net.save_graph(f'{path}/branch.html')
        HtmlFileB = open(f'{path}/branh.html', 'r', encoding='utf-8')

    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFileB.read(), height=435)

    # st.write("\n\n")
    # st.write("Treatment Tree")

    # try:
    #     visualize_graph_pyvis(tree.root, -1, show=False, path=path+'graph.html')
    #     #visualize_branch_pyvis(best_branch, show=False, path=path+'graph.html')
    #     #drug_net.save_graph(f'{path}/branch.html')
    #     HtmlFileG = open(f'{path}/graph.html', 'r', encoding='utf-8')

    # # Save and read graph as HTML file (locally)
    # except:
    #     visualize_graph_pyvis(tree.root, -1, show=False, path=path+'graph.html')
    #     #visualize_branch_pyvis(best_branch, show=False, path=path+'graph.html')
    #     #drug_net.save_graph(f'{path}/branch.html')
    #     HtmlFileG = open(f'{path}/graph.html', 'r', encoding='utf-8')

    # # Load HTML file in HTML component for display on Streamlit page
    # components.html(HtmlFileG.read(), height=435)