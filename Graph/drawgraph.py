
import pygame as pg

def drawgraph(screen, nodes, connections):
    screen.fill((255, 255, 255))

    for connection in connections:
        pg.draw.line(screen, (0, 0, 0), connection.node1.position, connection.node2.position, 1)

    for node in nodes:
        print(node.position)
        pg.draw.circle(screen, (0, 0, 0), node.position, 5)
        pg.draw.text(screen, str(node.id), node.position, font=pg.font.Font(None, 12))

    pg.display.flip()