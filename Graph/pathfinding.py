import time
from . import drawgraph

def astar(Graph, screen, font):
    time.sleep(1)
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
    #add start node to path
    Graph.visited.append(startNode.id)

    i = 0
    # perform astar search until the open set is empty or the end node is reached
    while Graph.currentNode.id != Graph.endNode:
        explore_connected_nodes(Graph)
        go_to_cheapest_node(Graph, screen, font)
        time.sleep(.15)
        i += 1
        #if curent node is end node, quit
        if Graph.currentNode.id == Graph.endNode or i > 100:
            #add endnode to path
            print("Path found:", Graph.visited)
            backtrack_path(Graph, screen, font)
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




def go_to_cheapest_node(Graph, screen, font):
    try:
        print("nodes in open set: ", [node.id for node in Graph.openSet])

        #Get the current node
        currentNode = Graph.currentNode

        #remove current node from opens set
        Graph.openSet.remove(currentNode)


        Graph.closedSet.append(currentNode)
  
        #find the node with the lowest cost
        
        lowestCostNode = min(Graph.openSet, key=lambda x: x.totalCost)
        #if end node is in open set, make it end node
        if Graph.nodedict[Graph.endNode] in Graph.openSet:
            lowestCostNode = Graph.nodedict[Graph.endNode]
        print(f"node {lowestCostNode.id} has the lowest cost of {lowestCostNode.totalCost}")
        #mark the connection travelled to the node as visited
        for connection in lowestCostNode.connections:
            if connection.node1 == lowestCostNode and connection.node2 == Graph.currentNode or connection.node1 == Graph.currentNode and connection.node2 == lowestCostNode:
                connection.visited = True
                break

        #move to lowestcostnode
        Graph.currentNode = lowestCostNode
                
        #add current node to visited,  contains all visited nodes
        Graph.visited.append(Graph.currentNode.id)

        drawgraph.drawgraph(screen,font,Graph)
        
        #print the previous and current node
        print(f"moved to node: ", Graph.currentNode.id, "the path is: ", Graph.visited)
    except:
        #if the open set is empty, there is no path to the end node
        print("nodes in open set: ", [node.id for node in Graph.openSet])

        #make a list containing all ids of the nodes in openset
        print("could not find node in openset")

def backtrack_path(Graph, screen, font):
    current = Graph.nodedict[Graph.endNode]
    Graph.path.append(current.id)
    visitedIndex = -2

    while current.id != Graph.startNode:
        #add current node to path
        
        #find the previous node
        previous = None
        foundPreviousNode = False

        while not foundPreviousNode:

            for connection in current.connections:
                if connection.node1.id == Graph.visited[visitedIndex] or connection.node2.id == Graph.visited[visitedIndex] and connection.visited:
                    previous = connection.node1 if connection.node1!= current else connection.node2
                    foundPreviousNode = True
                    break
            visitedIndex -= 1
        #TODO: #2 sometimes getting wrong node, need to log more nodes in visited?
        #error occurs for example on stuttgart - landberg in rods.json
        #mark node with a camefrom variable
        #if previous node is None, it means we couldn't find the previous node in the graph, so there's no path from start to end
        #break the loop and return the path
        if previous is None:
            print("could not find previous node")
            break
        current = previous
        Graph.path.append(current.id)
        #draw the graph
        drawgraph.drawgraph(screen, font, Graph)
        time.sleep(.15)
    #reverse the path to get the correct order
    Graph.path.reverse()
    print("Path from start to end: ", Graph.path)
