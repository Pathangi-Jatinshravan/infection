class User:
    '''
    User class, representing a node in the coaching graph. Users are connected to graph neighbors via
    coaching relationships, and have the attribute "site_version" 
    '''
    def __init__(self, name):
        self.name = name
        self.site_version = None
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

    def get_weight(neighbor):
        return self.neighbors.get(neighbor, None)

class Graph:
    def __init__(self):
        self.users = {}

    def add_node(self, name):
        self.users[name] = User(name)

    def add_edge(self, a, b, weight):
        if a not in self.users:
            self.add_node(a)
        if b not in self.users:
            self.add_node(b)
        self.users[a].add_neighbor(b, weight)
        self.users[b].add_neighbor(a, weight)

    def get_neighbors(self, node):
        if node in self.users:
            return self.users[node].neighbors
        else:
            return []

    def get_weight(self, a, b):
        if a in self.users:
            return self.users[a].get_weight(b)
        else:
            return None