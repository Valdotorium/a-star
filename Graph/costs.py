
def calculateCostsToEnd(Graph):
    endNode = Graph.nodedict[Graph.endNode]  # get the end node from the graph
    EndPosition = (endNode.position[0] / 20, endNode.position[1] /20)
    for node in Graph.nodedict.values():#
        nodePosition = (node.position[0] / 20, node.position[1] / 20)
        node.costToEnd = round(abs(EndPosition[0] - nodePosition[0]) + abs(EndPosition[1] - nodePosition[1]))

def calculateCostToEnd(Node, endNode):
    EndPosition = (endNode.position[0] / 20, endNode.position[1] / 20)
    Node.costToEnd = round(abs(EndPosition[0] - Node.position[0] / 20) + abs(EndPosition[1] - Node.position[1] / 20))

def resetAllCosts(Graph):
    for node in Graph.nodedict.values():
        node.costToEnd = "not defined yet"
        node.totalCost = None
        node.costFromStart = None
