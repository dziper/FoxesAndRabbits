import pygame as pg
import random
import copy
import grid as g
import rabbit

res = 20
w = 16
h = 10
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

r = rabbit.Rabbit((1,5),grid)
grid.print()
print()
r.move()
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
            if event.key == pg.K_s:
                if paused:
                    grid.step()
    screen.blit(grid.getSurf(res),(0,0))
    pg.display.update()
