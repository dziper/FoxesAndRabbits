import pygame as pg
import random
import copy
import grid as g
import rabbit, fox, wolf, bear, eagle
import matplotlib.pyplot as plt


res = 5
w = 200
h = 200
size = (w,h)
rls=[]
fls=[]
wls=[]
bls=[]
els=[]
n=100
gen=0

pxw = w * res
pxh = h * res

pxsize = pxw, pxh
fps = 10
steps = 0

pg.init()
screen = pg.display.set_mode(pxsize)
pg.display.set_caption('Foxes and Rabbits')
clock = pg.time.Clock()

myGrid = g.Grid(size)

myGrid.initializeAnimals(fx = 200, rb = 400, wl=200, br=200, ea=200)

paused = True
running = True
while running:
    screen.fill((0,0,0))
    clock.tick(fps)
    pg.display.set_caption('Foxes and Rabbits   Steps: ' + str(steps))


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
                    steps+=1
    if not paused:
        myGrid.step()
        steps+= 1
        gen+= 1/n
        plt.clf()

        if steps>=n:

            rls.append(rabbit.Rcount)
            plt.plot(rls[int((gen)*n-n): int((gen)*n)], 'y')

            fls.append(fox.Fcount)
            plt.plot(fls[int((gen)*n-n): int((gen)*n)], 'r')

            wls.append(wolf.Wcount)
            plt.plot(wls[int((gen)*n-n): int((gen)*n)], 'b')

            bls.append(bear.Bcount)
            plt.plot(bls[int((gen)*n-n): int((gen)*n)], 'm')

            els.append(eagle.Ecount)
            plt.plot(els[int((gen)*n-n): int((gen)*n)], 'g')
        else:

            rls.append(rabbit.Rcount)
            plt.plot(rls, 'y')

            fls.append(fox.Fcount)
            plt.plot(fls, 'r')

            wls.append(wolf.Wcount)
            plt.plot(wls, 'b')

            bls.append(bear.Bcount)
            plt.plot(bls, 'm')

            els.append(eagle.Ecount)
            plt.plot(els, 'g')

        plt.pause(0.01)


    screen.blit(myGrid.getSurf(res),(0,0))
    pg.display.update()
