import pygame as pg

def drawgraph(screen, nodes, connections, font):
    screen.fill((20,20,20))

    #drawing the connections between the positions of the nodes they connect
    for connection in connections:
        #warning: potentially dangerous
        pg.draw.line(screen, (round(connection.weight) * 2, 90, 70), connection.node1.position, connection.node2.position, 2)
        #write weight of connection
        text = font.render(str(connection.weight), True, (255, 255, 255))

        screen.blit(text, ((connection.node1.position[0] + connection.node2.position[0]) / 2 - text.get_width() / 2, (connection.node1.position[1] + connection.node2.position[1]) / 2 - text.get_height() / 2))

    #drawing the nodes as circles at their positions
    for node in nodes.values():
        print(node.position)
        pg.draw.circle(screen, (120, 120, 120), node.position, 12)
        text = font.render(str(node.id), True, (255, 255, 255))
        screen.blit(text, (node.position[0] - text.get_width() / 2, node.position[1] - text.get_height() / 2))


    pg.display.flip()