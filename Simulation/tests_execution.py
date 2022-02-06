from Test.high_probability_to_win_Test import high_probability_to_win_Test
from Test.naive_test import naive_test
from main import main
from time import time


from TreatmentTree.tree_draw import visualize_branch, visualize_graph, print_branch_data
#from TreatmentTree.pyviz_draw import visualize_graph

# ----  test naive
#
start = time()
tree = naive_test(main, 1, 240, 100)
end = time()
#
#-----


#-----test good
# start = time()
# tree =  high_probability_to_win_Test(main, 1, 240, 10)
# end = time()
#
#------

print(f'time:{round(end-start, 4)}')

best_branch = tree.best_branch()
print(best_branch[-1].get_average_final_state())
print_branch_data(best_branch)

#visualize_branch(best_branch)
#visualize_graph(tree.root)


#visualize_graph(tree.root, 10)

tree.prunning()
visualize_graph(tree.root, 120)

