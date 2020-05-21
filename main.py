import pygame as pg
import random
import copy
import grid as g

res = 20
w = 16
h = 16
size = (w,h)

pxw = w * res
pxh = h * res

pxsize = pxw, pxh
fps = 10

pg.init()
screen = pg.display.set_mode(pxsize)
pg.display.set_caption('Foxes and Rabbits')
clock = pg.time.Clock()

grid = g.Grid(size)
grid.print()

paused = False
running = True
while running:
    screen.fill((0,0,0))
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_SPACE:
                paused = not paused
