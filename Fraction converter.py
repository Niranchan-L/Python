n = int(input("Numerator: "))
d = int(input("Denominator: "))
soln = [n,d]
printed = False # Added
for x in range(2,max(n,d)):
    if n%d == 0:
        print()
        print((int(n/d)))
        printed = True # Added
        break
    else:
        if [n%x,d%x] == [0,0]:
            soln.append(n//x)
            soln.append(d//x)
if not printed: # Added
    print()
    print(soln[-2], "/", soln[-1])

