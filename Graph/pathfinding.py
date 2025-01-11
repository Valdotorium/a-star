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
    Graph.path.append(startNode.id)

    i = 0
    # perform astar search until the open set is empty or the end node is reached
    while True:
        explore_connected_nodes(Graph)
        go_to_cheapest_node(Graph, screen, font)
        time.sleep(.3)

        i += 1
        #if curent node is end node, quit
        if Graph.currentNode.id == Graph.endNode or i > 20:
            #add endnode to path
            Graph.path.append(Graph.currentNode.id)

            
            print("Path found:", Graph.path)

            
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

        #check what node from start lowestCostNode is the neighbor of
        foundLowestCost = False
        for connection in currentNode.connections:
            neighbor = connection.node1 if connection.node1!= currentNode else connection.node2
            if neighbor == lowestCostNode:
                #make the node with lowest cost current node
                print(f"node {lowestCostNode.id} has the lowest cost of {lowestCostNode.totalCost}, it was neighbor of current node")
                Graph.currentNode = lowestCostNode
                foundLowestCost = True
                pass
            
               
        x = 1
        if not foundLowestCost:
            print("lowestCostNode is not neighbor of current node")
            while len(Graph.path) > 0:
                if not foundLowestCost:
                    #going back until we find the lowest cost node 
                    Node = Graph.nodedict[Graph.path[-1]]
                    for connection in Node.connections:
                        neighbor = connection.node1 if connection.node1!= Node else connection.node2
                        if neighbor == lowestCostNode:
                            foundLowestCost = True
                            #make the node with lowest cost current node
                            print(f"node {lowestCostNode.id} has the lowest cost of {lowestCostNode.totalCost}, it was neighbor of: ", Node.id)
                            Graph.currentNode = lowestCostNode
                            break
                    if foundLowestCost:
                        break
                    x += 1
                    print(f"node {lowestCostNode.id} is not neighbor of node {Graph.path[-1]}")
                    Graph.path.pop(-1)
                    print(f"the path is now {Graph.path}")
                    drawgraph.drawgraph(screen,font,Graph)
                    time.sleep(.3)

                else:
                    break
                    
                
        #add current node to path
        Graph.path.append(Graph.currentNode.id)


        drawgraph.drawgraph(screen,font,Graph)
        
        #print the previous and current node
        print(f"moved to node: ", Graph.currentNode.id, "the path is: ", Graph.path)
    except:
        #if the open set is empty, there is no path to the end node
        print("nodes in open set: ", [node.id for node in Graph.openSet])

        #make a list containing all ids of the nodes in openset
        print("could not find node in openset")


  