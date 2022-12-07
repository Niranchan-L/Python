x = 8
y = 72
for n in range(max(x,y)):
    if float(y*n) == float(x):
        print(n)
        break
    elif float(x*n) == float(y):
        print(1,"/",n)
        break