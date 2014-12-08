from user import User, Graph
from Queue import Queue, LifoQueue


def infect(g, start):
    '''
    INPUTS: pre-infection Graph object, User object
    OUTPUT: list of 'infected' users, limited by edge weighting (see README)
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

def build_graph(edge_file):
    '''
    INPUT: None
    OUTPUT: Graph object

    Constructs a graph object edge by edge
    '''
    g = Graph()
    with open(edge_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(',')
            g.add_edge(str(line[0]), str(line[1]),1)
    return g


if __name__ == '__main__':
    g = build_graph('edges.csv')
    print "Users: ", [u for u in g.users]
    first_user = raw_input("Enter the name of the user to infect first ")
    print "Spreading the infection!"
    infect(g, first_user)