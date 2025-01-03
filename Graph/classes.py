class Node:
    def __init__(self, id, position):
        self.id = id
        self.position = position
        self.connections = []


        #need to be defined later
        self.costFromStart = None
        self.costToEnd = "not defined yet"
        self.totalCost = None



class Connection:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight



