from pyvis.network import Network
import networkx as nx
from .node import Node

def create_graph(G:Network,nodes:list[Node], n):
    if len(nodes) == 0 or n == 0:
        return
    for node in nodes:
        if node is not None:
            label = f"{node.value}"
            id = node._id
            title = f"Time:{node.created_time}\n\n{node.get_average_arrival_state()}"
            G.add_node(n_id=id, label=label,shape='circle', title=title, level=n)
            if node.parent != None:
                G.add_edge(node._id, node.parent._id)
    childrens = []
    for node in nodes:
        if node is not None:
            childrens.extend(node._children)
    create_graph(G, childrens, n-1)

def visualize_graph(root:Node, n):
    net = Network('1000px', '1000px')
    create_graph(net, [root], n)
    ##pos = hierarchy_pos(G,f"-1 :0")    
    #nx.draw(G, pos=pos, with_labels=True, font_weight='bold')
    #plt.figure(figsize=(16,16))
    print('here')
    net.show('mygraph.html')
    #plt.show()