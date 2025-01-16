
from . import classes
from . import drawgraph
from . import interactions
class Graph():
    def __init__(self):
        self.nodedict = {}
        self.connections = []

        #for interactions
        self.selectedNode = None
        self.startNode = None
        self.endNode = None
        self.currentNode = None

        #for astar
        self.path = []
        self.visited = []
        self.openSet = []
        self.closedSet = []
        
    def add_node(self, id, position):
        node = classes.Node(id, position)
        self.nodedict[id] = node

    def add_connection(self, node1_id, node2_id, weight):
        connection = classes.Connection(self.nodedict[node1_id], self.nodedict[node2_id], weight)
        self.connections.append(connection)

        self.nodedict[node1_id].connections.append(connection)
        self.nodedict[node2_id].connections.append(connection)

    def update(self, screen, font, AWAIT_STEPS):
        interactions.interactions(self, screen, font, AWAIT_STEPS)
        drawgraph.drawgraph(screen, font, self)
        