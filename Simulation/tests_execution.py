from Test.high_probability_to_win_Test import high_probability_to_win_Test
from Test.naive_test import naive_test
from main import main


from TreatmentTree.tree_draw import visualize_branch, print_branch_data

# ----  test naive
##tree = naive_test(main)
#-----


#-----test good
tree =  high_probability_to_win_Test(main, 1, 240, 10000)


best_branch = tree.best_branch()
print(best_branch[-1].get_average_final_state())
print_branch_data(best_branch)
#visualize_branch(best_branch)
#visualize_graph(tree.root)