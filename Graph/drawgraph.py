import pygame as pg

def drawgraph(screen, font, Graph):
    screen.fill((20,20,20))

    connections = Graph.connections
    nodes = Graph.nodedict

    #drawing the connections between the positions of the nodes they connect
    for connection in connections:
        #warning: potentially dangerous
        if round(connection.weight) * 2.75 < 255:
            pg.draw.line(screen, (round(connection.weight) * 2.75, 100, 60), connection.node1.position, connection.node2.position, 2)
        else:
            pg.draw.line(screen, (255, 90, 60), connection.node1.position, connection.node2.position, 2)
        #write weight of connection
        text = font.render(str(connection.weight), True, (255, 255, 255))

        screen.blit(text, ((connection.node1.position[0] + connection.node2.position[0]) / 2 - text.get_width() / 2, (connection.node1.position[1] + connection.node2.position[1]) / 2 - text.get_height() / 2))

    #drawing the nodes as circles at their positions
    for node in nodes.values():
        print(Graph.selectedNode)
        if node.id == Graph.selectedNode:
            pg.draw.circle(screen, (200, 120, 120), node.position, 12)
        else:
            pg.draw.circle(screen, (120, 120, 120), node.position, 12)
        text = font.render(str(node.id), True, (255, 255, 255))

        screen.blit(text, (node.position[0] - text.get_width() / 2, node.position[1] - text.get_height() / 2))

    #if a node is selected, write all of its attributes in the top left corner
    if Graph.selectedNode is not None:
        selectedNode = nodes[Graph.selectedNode]
        text = font.render(f"ID: {selectedNode.id}, Position: {selectedNode.position}", True, (255, 255, 255))
        screen.blit(text, (70, 0))

    pg.display.flip()