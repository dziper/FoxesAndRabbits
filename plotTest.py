import numpy as np
import matplotlib.pyplot as plt

ls = [0,1,2,3,5,6,7,2,3,4,5]

for i in range(10):
    plt.plot(ls[:i])
    plt.pause(0.01)
