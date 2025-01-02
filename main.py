from Graph import app
import pygame as pg
import asyncio
import os
import random
import string


Graph = app.Graph()

async def main():
    #basic scripts for the pygame window
    pg.init()
    pg.font.init()

    #initializing font
    font = "./PixelOperator.ttf"
    font = pg.font.Font(None, 14)
    font.render("www", 1, (20,20,20))

    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Pathfinding Visualization")

    # generating a random graph
    node_count = 9
    connections_multiplier = 1.45
    N = 3
    for i in range(node_count):
        #TODO: make sure nodes are spaced 
        nodePosition = (random.randint(20,780), random.randint(20,580))
        Graph.add_node(''.join(random.choices(string.ascii_uppercase + string.digits, k=N)), nodePosition)

    #some random connections
    for i in range(round(node_count * connections_multiplier)):
        firstNodeId = random.choice(list(Graph.nodedict.keys()))
        secondNodeId = random.choice(list(Graph.nodedict.keys()))
        firstNode = Graph.nodedict[str(firstNodeId)]
        secondNode = Graph.nodedict[str(secondNodeId)]
        #TODO: check if the two nodes are already connected
        if firstNode!=secondNode:
            Graph.add_connection(firstNodeId, secondNodeId, abs(round((firstNode.position[0] / 20 - secondNode.position[0] / 20) * random.uniform(0.5,2))) + abs(round((firstNode.position[1] / 10 - secondNode.position[1] / 10) * random.uniform(0.5,2))))
    # draw the graph
    while True:
        Graph.draw(screen, font)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        await asyncio.sleep(0.1)


asyncio.run(main())