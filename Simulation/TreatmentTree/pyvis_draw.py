from typing import Dict
from pyvis.network import Network
#import networkx as nx
from .node import Node

def __format_info(state:Dict[str,float])->str:
    s = ""
    for p, v in state.items():
        s += f"{p}:{round(v,3)}\n"
    return s

def __create_branch(G:Network, nodes:list[Node]):
    for i in range(len(nodes)):
        label = f"{nodes[i].value}"
        id = nodes[i]._id
        info = None 
        if i == len(nodes)-1:
            info = __format_info(nodes[i].get_average_final_state())
        else:
            info = __format_info(nodes[i].get_average_arrival_state())
        title = f"Time:{nodes[i].created_time} \n\n {info}"
        G.add_node(n_id=id, label=label,shape='circle', title=title, level=i)
        if i > 0:
            G.add_edge(nodes[i]._id, nodes[i-1]._id)

def __create_graph(G:Network,nodes:list[Node], n):
    if len(nodes) == 0 or n == 0:
        return
    for node in nodes:
        if node is not None:
            label = f"{node.value}"
            id = node._id
            title = f"Time:{node.created_time}\n\n{__format_info(node.get_average_arrival_state())}"
            color='cyan'
            if id==-1:
                color='red'
            G.add_node(n_id=id, label=label,shape='circle', color=color, title=title) #level=n)
            if node.parent != None:
                prob = node.probability_value
                color='cyan'
                if prob>0.5:
                    color='black'
                G.add_edge(node._id, node.parent._id,width=prob/10,color=color,title=str(prob))
    childrens = []
    for node in nodes:
        if node is not None:
            childrens.extend(node._children)
    __create_graph(G, childrens, n-1)

def visualize_branch_pyvis(branch_nodes:list[Node]):
    net = Network('1000px', '1000px')
    __create_branch(net, branch_nodes)
    net.show('branch.html')

def visualize_graph_pyvis(root:Node, n):
    net = Network('1000px', '1000px')
    __create_graph(net, [root], n)
    net.repulsion(node_distance=100, spring_length=100)
    net.show('graph.html')
    #plt.show()