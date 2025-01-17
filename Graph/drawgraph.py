import pygame as pg

def drawgraph(screen, font, Graph):
    screen.fill((20,20,20))

    connections = Graph.connections
    nodes = Graph.nodedict

    #drawing the connections between the positions of the nodes they connect
    for connection in connections:
        #warning: potentially dangerous
        if round(connection.weight) * 2.75 < 255:
            #if connection connects nodes in the path, make them orange
            if connection.node1.id in Graph.path and connection.node2.id in Graph.path:
                pg.draw.line(screen, (255, 150, 120), connection.node1.position, connection.node2.position, 4)

            #if connection connects nodes in the visited list, make them blue
            elif connection.node1.id in Graph.visited and connection.node2.id in Graph.visited:

                if connection in connection.node1.connections and connection in connection.node2.connections:
                    pg.draw.line(screen, (100, 220, 0), connection.node1.position, connection.node2.position, 3)
            else:
                pg.draw.line(screen, (round(connection.weight) * 2.75, 100, 60), connection.node1.position, connection.node2.position, 2)
        else:
            pg.draw.line(screen, (255, 90, 60), connection.node1.position, connection.node2.position, 2)
        #write weight of connection
        text = font.render(str(connection.weight), True, (255, 255, 255))

        screen.blit(text, ((connection.node1.position[0] + connection.node2.position[0]) / 2 - text.get_width() / 2, (connection.node1.position[1] + connection.node2.position[1]) / 2 - text.get_height() / 2))
    
    #drawing the nodes as circles at their positions
    for node in nodes.values():

        #if the nod.ides id ist in Graph.path
        if node.id == Graph.selectedNode:
            #selectednode is red
            pg.draw.circle(screen, (200, 100, 100), node.position, 12)
        elif node in Graph.path:
            #path node is red
            pg.draw.circle(screen, (190,100,100), node.position, 15)
        elif node == Graph.currentNode:
            #current node is red
            pg.draw.circle(screen, (190, 100, 100), node.position, 15)

        elif node.id in Graph.visited:
            #currentnode is light green
            pg.draw.circle(screen, (100, 220, 100), node.position, 12)

        elif node in Graph.openSet:
            #visited node is dark green
            pg.draw.circle(screen, (100, 150, 100), node.position, 12)


        elif node.id == Graph.startNode and Graph.startNode != None:
            #startnode is yellow
            pg.draw.circle(screen, (160, 160, 100), node.position, 12)
        elif node.id == Graph.endNode and Graph.endNode != None:
            #endnode is blue
            pg.draw.circle(screen, (100, 160, 160), node.position, 12)
        else:
            pg.draw.circle(screen, (100, 100, 100), node.position, 12)
        text = font.render(str(node.id), True, (255, 255, 255))

        screen.blit(text, (node.position[0] - text.get_width() / 2, node.position[1] - text.get_height() / 2))

    #if a node is selected, write all of its attributes in the top left corner
    if Graph.selectedNode is not None:
        selectedNode = nodes[Graph.selectedNode]
        text = font.render(f"""ID: {selectedNode.id}, Position: {selectedNode.position}, Estimated cost to End: {selectedNode.costToEnd} """, True, (255, 255, 255))
        screen.blit(text, (70, 740))
        text = font.render(f""" has been explored from: {selectedNode.exploredFrom}, has been visited from: {selectedNode.cameFrom}""", True, (255, 255, 255))
        screen.blit(text, (70, 760))

    if Graph.startNode == Graph.selectedNode and Graph.startNode != None:
        text = font.render("This is the start Node", True, (255, 255, 255))
        screen.blit(text, (70, 780))
    if Graph.endNode == Graph.selectedNode and Graph.endNode != None: 
        text = font.render("This is the end Node", True, (255, 255, 255))
        screen.blit(text, (70, 780))

    pg.display.flip()