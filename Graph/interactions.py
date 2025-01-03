

import pygame as pg

def interactions(Graph):
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