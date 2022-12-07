x = [0]*100
for p in range(1, 101):
    for z in range(p-1, 100, p):
        if x[z] == 0:
            x[z] = 1
        else:
            x[z] = 0





# Printing process
for e in range(10):
    print(x[e*10:(e*10) + 10])

for r in range(len(x)):
    if x[r] == 1:
        print(r+1)
