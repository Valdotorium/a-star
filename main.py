from Graph import app
from Graph import generategraph
import pygame as pg
import asyncio
import os
import random
import string

#CONTROLS
# click on node: select node
#click anywhere else: nothing or deselect node
#space: create node at mouse position
#node is selected + x: delete node and its connections
#node is selected + c while hovering over other node: create connection with manhattean dist. as weight between nodes

#CONFIGS
START_MODE = "fromScratch"  #fromScratch, generateRandomGraph, load

async def main():
    Graph = app.Graph()
    #basic scripts for the pygame window
    pg.init()
    pg.font.init()

    #initializing font
    font = "./PixelOperator.ttf"
    font = pg.font.Font(None, 14)
    font.render("www", 1, (20,20,20))

    #generate a random graph if wanted
    if START_MODE == "randomGraph":
        Graph = generategraph.generateRandomGraph()

    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Pathfinding Visualization")
    # mainloop
    while True:
        Graph.update(screen, font)
        await asyncio.sleep(0.1)


asyncio.run(main())