import matplotlib.pyplot as plt
ipt=[1, 2, 3, 4, 9, 13]
inp=[]
inpt=[]
for x in range(0,len(ipt)):
    print(x)
    inp.append(ipt[x]*2)

for x in range(0,len(ipt)):
    inpt.append(ipt[x]*3)
plt.ylabel('some numbers')
plt.plot(ipt, inp,'gs', ipt, inpt, 'bp')
plt.show()
ipt=[1, 2, 3, 4, 9, 13, 16, 17]
inp=[]
inpt=[]
for x in range(0,len(ipt)):
    print(x)
    inp.append(ipt[x]*2)

for x in range(0,len(ipt)):
    inpt.append(ipt[x]*3)
plt.ylabel('some numbers')
plt.plot(ipt, inp,'gs', ipt, inpt, 'bp')
plt.show()
