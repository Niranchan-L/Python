is_zero_to_infinity = input("is the limit zero to infinity? Type 'Y' or 'N' :")
n = int(input("What is the value of n?"))
a = int(input("What is the value of a?"))
# 0/* x^n e^-ax dx
print()
if is_zero_to_infinity.upper() == "Y":
    # Getting n factorial
    result = 1
    d = pow(a, n+1)
    while n > 1:
        result *= n
        n -= 1
    # Find HCF
    z = []
    for x in range(2,min(d,result)):
        if result%d == 0:
            print(int(result/d))
            break
        else:
            if [result%x,d%x] == [0,0]:
                z.append(result//x)
                z.append(d//x)
    print(z[-2],"/",z[-1])
else:
    print("The limit does not exist!")

