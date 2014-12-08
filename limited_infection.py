from user import User, Graph
from Queue import Queue


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
            print "Just infected", node
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
    users = g.users.keys()
    print "Users: ", users
    first_user = raw_input("Please enter the name of the user to infect first: ")
    while len(first_user)==0 or first_user not in users:
        print "Oops, that's not a valid user \n. Please choose from the following users: ", users
        print "\n"    
        first_user = raw_input("Please enter the name of the user to infect first: ")
    print "\n"
    print "Spreading the infection!"
    print "\n"
    infect(g, first_user)