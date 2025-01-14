
import random
from . import pathfinding
import pygame as pg
from . import costs

def interactions(Graph, screen, font):
    nodeClicked = False
    #detect if a node is being clicked
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            for node in Graph.nodedict.values():

                if pg.Rect(node.position[0] - 12, node.position[1] - 12, 24, 24).collidepoint(mouse_pos):
                    Graph.selectedNode = node.id
                    nodeClicked = True
            #if no node is clicked, deselect the current node
            if not nodeClicked:
                Graph.selectedNode = None

        #quit program
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    #pressing space creates a node at the mouse position
    if pg.key.get_just_pressed()[pg.K_SPACE]:
        #TODO: #1 fix bug where node placement is not possible, probably because of the use of ids that have already been used previously
        mouse_pos = pg.mouse.get_pos()
        Graph.add_node(len(Graph.nodedict), mouse_pos)
        #refreshing the costs
        if Graph.endNode != None:
            costs.calculateCostToEnd(Graph.nodedict[len(Graph.nodedict)-1], Graph.nodedict[Graph.endNode])

    #if x is clicked the current selected node and all of its connections get deleted
    if pg.key.get_just_pressed()[pg.K_x]:
        if Graph.selectedNode is not None:
            i = 0
            while i < len(Graph.connections):
                connection = Graph.connections[i]
                #delete all connections
                print("Connection data ", "node 1: ", connection.node1, "node 2: ", connection.node2, "selectednode: ", Graph.selectedNode)
                if connection.node1 == Graph.nodedict[Graph.selectedNode] or connection.node2 == Graph.nodedict[Graph.selectedNode]:
                    connection.node1.connections.remove(connection)
                    connection.node2.connections.remove(connection)
                    Graph.connections.remove(connection)
                    i -= 1
                i += 1
            #delete the node from the graph
            del Graph.nodedict[Graph.selectedNode]
            print("deleted node")
            #reset all costs if endnode does not exist
            try:
                x = Graph.nodedict[Graph.endNode].position[0]
                print("found endNode at position: ", x)
            except:
                print("no endNode found")
                Graph.endNode = None
                costs.resetAllCosts(Graph)
            Graph.selectedNode = None
        

    #pressing c key creates a connection between the current node and the clicked node
    if pg.key.get_just_pressed()[pg.K_c]:
        mouse_pos = pg.mouse.get_pos()
        for node in Graph.nodedict.values():
            if pg.Rect(node.position[0] - 12, node.position[1] - 12, 24, 24).collidepoint(mouse_pos):
                #the connection can only be created when the two nodes are not already connected with a connection
                if any(connection.node1.id == Graph.selectedNode and connection.node2.id == node.id for connection in Graph.connections) and any(connection.node2.id == Graph.selectedNode and connection.node1.id == node.id for connection in Graph.connections):
                    break
                #there cannot be a connection between the same node
                if Graph.selectedNode == node.id:
                    break
                #create a connection between the two nodes and tak the manhattan distance between both nodes as cost
                Graph.add_connection(Graph.selectedNode, node.id, abs(round((Graph.nodedict[Graph.selectedNode].position[0] / 20 - node.position[0] / 20))) + abs(round((Graph.nodedict[Graph.selectedNode].position[1] / 10 - node.position[1] / 10))))


    #pressing s key makes the selected node the start node
    if pg.key.get_just_pressed()[pg.K_s]:
        if Graph.selectedNode is not None:
            Graph.startNode = Graph.selectedNode
        if Graph.startNode == Graph.endNode:
            Graph.startNode = None

    #pressing e key makes the selected node the end node
    if pg.key.get_just_pressed()[pg.K_e]:
        if Graph.selectedNode is not None:
            Graph.endNode = Graph.selectedNode

        if Graph.startNode == Graph.endNode:
            Graph.endNode = None

        #if graph start and end node are not none then perform a star
        if Graph.startNode is not None and Graph.endNode is not None and Graph.startNode != Graph.endNode:
            #reset everything
            Graph.visited = []
            costs.resetAllCosts(Graph)
            Graph.path = []

            for node in Graph.nodedict.values():
                node.cameFrom = None
                node.exploredFrom = None

            costs.calculateCostsToEnd(Graph)
            #pathfinding
            pathfinding.astar(Graph, screen, font)
