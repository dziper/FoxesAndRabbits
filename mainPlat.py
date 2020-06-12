import pygame as pg
import random
import copy
import platform as pl

res = 5
w = 200
h = 200
size = (w,h)

pxw = w * res
pxh = h * res
fps = 10

pxsize = pxw, pxh

pg.init()
screen = pg.display.set_mode(pxsize)
pg.display.set_caption('DropGame')
clock = pg.time.Clock()

myPlat = pl.Platform()

paused=True
running=True

while running:
    screen.fill((0,0,0))
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_RIGHT:
                pl.Platform.Right(self)
            if event.key == pg.K_LEFT:
                pl.Platform.Left(self)
            if event.key == pg.K_SPACE:
                paused= not paused
