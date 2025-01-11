
from . import app
import random, string

def generateRandomGraph():    # generating a random graph
    Graph = app.Graph()
    node_count = 16
    connections_multiplier = 1
    N = 3
    for i in range(node_count):
        #TODO: make sure nodes are spaced 
        nodePosition = (random.randint(20,780), random.randint(20,580))
        Graph.add_node(''.join(random.choices(string.ascii_uppercase + string.digits, k=N)), nodePosition)

    #some random connections
    for i in range(round(node_count * connections_multiplier)):
        firstNodeId = random.choice(list(Graph.nodedict.keys()))
        secondNodeId = random.choice(list(Graph.nodedict.keys()))
        firstNode = Graph.nodedict[str(firstNodeId)]
        secondNode = Graph.nodedict[str(secondNodeId)]
        #TODO: check if the two nodes are already connected
        if firstNode!=secondNode:
            Graph.add_connection(firstNodeId, secondNodeId, abs(round((firstNode.position[0] / 20 - secondNode.position[0] / 20) * random.uniform(0.5,2))) + abs(round((firstNode.position[1] / 10 - secondNode.position[1] / 10) * random.uniform(0.5,2))))

    return Graph
