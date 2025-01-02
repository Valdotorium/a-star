
from . import classes
from . import drawgraph

class Graph():
    def __init__(self):
        self.nodedict = {}
        self.connections = []

    def add_node(self, id, position):
        node = classes.Node(id, position)
        self.nodedict[id] = node

    def add_connection(self, node1_id, node2_id, weight):
        connection = classes.Connection(self.nodedict[node1_id], self.nodedict[node2_id], weight)
        self.connections.append(connection)

        self.nodedict[node1_id].connections.append(connection)
        self.nodedict[node2_id].connections.append(connection)

    def draw(self, screen, font):
        drawgraph.drawgraph(screen, self.nodedict, self.connections, font)

    
    


        