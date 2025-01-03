from Graph import app
from Graph import generategraph
import pygame as pg
import asyncio
import os
import random
import string


#CONFIGS
START_MODE = "randomGraph"  #fromScratch, generateRandomGraph, load



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