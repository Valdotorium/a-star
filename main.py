from Graph import app
from Graph import generategraph
import pygame as pg
import asyncio
import os
import random
import string
import json
import math
#CONTROLS
# click on node: select node
#click anywhere else: nothing or deselect node
#space: create node at mouse position
#node is selected + x: delete node and its connections
#node is selected + c while hovering over other node: create connection with manhattean dist. as weight between nodes
#node is selected + s: make selected node start node
#node is selected + e: make selected node end node, calculates costs

#CONFIGS
START_MODE = "load"  #fromScratch, generateRandomGraph, load
AWAIT_STEPS = False #make the user press c before continuing the algorithm

async def main():
    Graph = app.Graph()
    #basic scripts for the pygame window
    pg.init()
    pg.font.init()

    #initializing font
    font = "./PixelOperator.ttf"
    font = pg.font.Font(None, 20)

    #generate a random graph if wanted
    if START_MODE == "randomGraph":
        Graph = generategraph.generateRandomGraph()

    #load a graph if wanted
    elif START_MODE == "load":
        Data = json.load(open("./autobahn-stau.json"))
        Graph = app.Graph()
        #data has nodes with their ids and positions and connections with their nodes and weight
        for node in Data["nodes"]:
            Graph.add_node(node["id"], node["position"])
        for connection in Data["connections"]:
            try:
                Graph.add_connection(connection["node1"], connection["node2"], connection["weight"])
            except:
                node1pos = Graph.nodedict[connection["node1"]].position
                node2pos = Graph.nodedict[connection["node2"]].position
                Graph.add_connection(connection["node1"], connection["node2"], round(math.sqrt(abs(node1pos[0] / 4 - node2pos[0] / 4) ** 2 + abs(node1pos[1]/ 4 - node2pos[1] / 4) ** 2 )))


    screen = pg.display.set_mode((1200, 800))
    
    pg.display.set_caption("Pathfinding Visualization")
    # mainloop
    while True:
        Graph.update(screen, font, AWAIT_STEPS)
        await asyncio.sleep(0.1)

asyncio.run(main())