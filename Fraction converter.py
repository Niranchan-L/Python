n = int(input("Numerator: "))
d = int(input("Denominator: "))
soln = [n,d]
printed = False
for x in range(2,max(n,d)):
    if n%d == 0:
        print()
        print((int(n/d)))
        printed = True
        break
    else:
        if [n%x,d%x] == [0,0]:
            soln.append(n//x)
            soln.append(d//x)
if not printed: 
    print()
    print(soln[-2], "/", soln[-1])

