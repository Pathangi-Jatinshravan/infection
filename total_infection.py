from user import User, Graph
from Queue import Queue
import networkx as nx
import matplotlib.pyplot as plt

def infect(g, start):
    '''
    INPUTS: pre-infection Graph object, User object
    OUTPUT: set of 'infected' users
    
    Infects connected portion of user graph with new site.
    '''
    q = Queue()
    q.put(start)
    infected = set()
    while not q.empty():
        node = q.get()
        if node not in infected:
            print "Just infected", node
            g.users[node].site_version = 'new' # Expose infected user to new site
            infected.add(node)
            for neighbor in g.get_neighbors(node):
                q.put(neighbor)
    return infected

def build_graph(edge_file):
    '''
    INPUT: None
    OUTPUT: Graph object

    Reads in edgelist and constructs Graph object edge by edge (edge weights equal for total infection)
    '''
    g = Graph()
    with open(edge_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(',')
            g.add_edge(str(line[0]), str(line[1]),1)
    return g

def visualize(list, infected):
    '''
    INPUT: Homespun Graph object (defined in user.py), list of infected users
    OUTPUT: image of network (PNG)
    '''
    G = nx.read_edgelist(list, delimiter=',')
    plt.figure(figsize=(6,6))
    values = [1.0 if str(node) in infected else 0.0 for node in G.nodes()]
    nx.draw(G, node_size=500, cmap=plt.get_cmap('rainbow'), node_color=values, font_size=6, font_family='sans-serif')
    plt.savefig('network_infection.png',format='PNG')



if __name__ == '__main__':
    g = build_graph('data/edges.csv')
    users = g.users.keys()
    print "Total infection:"
    print "Users: ", users
    first_user = raw_input("Please enter the name of the user to infect first: ")
    while first_user not in users:
        print "Oops, that's not a valid user. \nPlease choose from the following: ", users
        print "\n"    
        first_user = raw_input("Please enter the name of the user to infect first: ")
    print "\nSpreading the infection! \n"
    infected = infect(g, first_user)
    visualize('data/edges.csv', infected)