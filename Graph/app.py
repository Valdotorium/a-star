from . import configs
from . import classes

import pygame as pg

class GraphInterface():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((configs.WINDOW_WIDTH, configs.WINDOW_HEIGHT))
        pg.display.set_caption("Graph Interface")
    
    def update(self):
        self.screen.fill((0, 0, 0))
        pg.display.flip()
        if pg.key.get_pressed()[pg.K_0]:
            pg.quit()
        