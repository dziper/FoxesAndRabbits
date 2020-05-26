import pygame as pg
import random
import copy
import grid as g

res = 5
w = 100
h = 100
size = (w,h)

pxw = w * res
pxh = h * res

pxsize = pxw, pxh
fps = 10

pg.init()
screen = pg.display.set_mode(pxsize)
pg.display.set_caption('Foxes and Rabbits')
clock = pg.time.Clock()

myGrid = g.Grid(size)

myGrid.initializeAnimals(fx = 200, rb = 200)

paused = True
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
            if event.key == pg.K_s:
                if paused:
                    myGrid.step()
    if not paused:
        myGrid.step()
    screen.blit(myGrid.getSurf(res),(0,0))
    pg.display.update()
