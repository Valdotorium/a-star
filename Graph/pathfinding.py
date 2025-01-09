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
    i = 0
    # perform astar search until the open set is empty or the end node is reached
    while True:
        explore_connected_nodes(Graph)
        go_to_cheapest_node(Graph)
        i += 1
        #if curent node is end node, quit
        if Graph.currentNode.id == Graph.endNode or i > 20:
            print("Path found")
            break






def explore_connected_nodes(Graph):
    #Get the current node
    currentNode = Graph.currentNode


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




def go_to_cheapest_node(Graph):
    try:
        #Get the current node
        currentNode = Graph.currentNode

        #remove current node from opens set
        Graph.openSet.remove(currentNode)


        Graph.closedSet.append(currentNode)
  
        #find the node with the lowest cost
        lowestCostNode = min(Graph.openSet, key=lambda node: node.totalCost)
        #make the node with lowest cost current node
        Graph.currentNode = lowestCostNode


        print(f"node {lowestCostNode.id} has the lowest cost of {lowestCostNode.totalCost}")
        #print the previous and current node
        print(f"moved to node: ", Graph.currentNode.id)
    except:
        #if the open set is empty, there is no path to the end node
        print("could not find node in openset")


  