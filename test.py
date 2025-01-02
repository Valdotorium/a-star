from Graph import app
import pygame as pg


App = app.GraphInterface()
while True:
    App.update()
    pg.display.flip()