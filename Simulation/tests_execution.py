from Test.high_probability_to_win_Test import high_probability_to_win_Test
from TreatmentTree.node import Node
from main import main
from time import time


#from TreatmentTree.networkx_draw import visualize_branch_nx, visualize_graph_nx
from TreatmentTree.pyvis_draw import visualize_graph_pyvis, visualize_branch_pyvis

def print_branch_data(nodes:list[Node]):
    print('root')
    for node in nodes[1:]:
        print(f"{node.value}  aplication time:{node.created_time}   p:{round((node.probability_value))}%")

# ----  test naive
##tree = naive_test(main)
#-----


#-----test good
st = time()
tree =  high_probability_to_win_Test(main, 1, 240, 1000)
end = time()
print(f"Time execution: {round(end-st,4)}")

tree.calculate_probability()
best_branch = tree.best_branch()
print(best_branch[-1].get_average_final_state())
print_branch_data(best_branch)

visualize_branch_pyvis(best_branch)
#visualize_graph(tree.root)


#visualize_graph_nx(tree.root, 140)

tree.prunning(max_childs=2)
visualize_graph_pyvis(tree.root, 140)