from user import User, Graph
from Queue import Queue, LifoQueue
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

def infect(g, start):
    '''
    INPUTS: pre-infection Graph object, User object
    OUTPUT: list of 'infected' users (total infection, no stopping points)
    '''
    q = Queue()
    q.put(start)
    v_set = set()
    while not q.empty():
        node = q.get()
        if node not in v_set:
            print "Just infected ", node
            v_set.add(node)
            for neighbor in g.get_neighbors(node):
                q.put(neighbor)

def build_graph():
    '''
    INPUT: None
    OUTPUT: Graph object

    Constructs a graph object edge by edge
    '''
    g = Graph()
    g.add_edge('Tom', 'Mary', 1)
    g.add_edge('Tom', 'Jen', 1)
    g.add_edge('Mary', 'Jerry', 1)
    g.add_edge('Jen', 'Fido', 1)
    g.add_edge('Lassie', 'Jen', 1)
    return g

def visualize(list):
    '''
    INPUT: Homespun Graph object (defined in user.py)
    OUTPUT: image of network (PNG)
    '''
    G = nx.read_edgelist(list, delimiter=' ', create_using=nx.DiGraph())
    plt.figure(figsize(6,4))
    nx.draw(G)


if __name__ == '__main__':
    g = build_graph()
    print "Users: ", [u for u in g.users]
    print "Spreading the infection!"
    infect(g, 'Tom')