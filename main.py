from Graph import app
import pygame as pg
import asyncio


Graph = app.Graph()

async def main():
    #basic scripts for the pygame window
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Pathfinding Visualization")

    # Add nodes to the graph
    for i in range(10):
        node = app.Graph.add_node(Graph, i, (i * 100, 100))


    # draw the graph
    while True:
        Graph.draw(screen)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        await asyncio.sleep(0.1)


asyncio.run(main())