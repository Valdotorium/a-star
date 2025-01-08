def astar(Graph):
    # starting node
    startNode = Graph.nodedict[Graph.startNode]
    # end node
    endNode = Graph.nodedict[Graph.endNode]

    # Initialize the open and closed lists
    Graph.openSet = [startNode]
    Graph.closedSet = []

    startNode.costFromStart = 0
    startNode.totalCost = startNode.costFromStart + startNode.costToEnd
    Graph.currentNode = startNode

    explore_connected_nodes(Graph)





def explore_connected_nodes(Graph):
    #Get the current node
    currentNode = Graph.currentNode

    #remove current node from opens set
    Graph.openSet.remove(currentNode)


    Graph.closedSet.append(currentNode)

    # Get all the neighboring nodes
    for connection in currentNode.connections:
        neighbor = connection.node1 if connection.node1 != currentNode else connection.node2
        # If the neighbor is already in the closed set, skip it

        if neighbor in Graph.closedSet:
            continue

        #add neighbor to open set
        Graph.openSet.append(neighbor)

        neighbor.costFromStart = currentNode.costFromStart + connection.weight
        neighbor.totalCost = neighbor.costFromStart + neighbor.costToEnd

        #print results
        print(f"node {neighbor.id} has a cost of {neighbor.totalCost}")

    #find the node with the lowest cost
    lowestCostNode = min(Graph.openSet, key=lambda node: node.totalCost)

    print(f"node {lowestCostNode.id} has the lowest cost of {lowestCostNode.totalCost}")





  