a = 2520
result = []
for x in range(a+1):
    for y in range(a+1):
        if x*y == a:
            result.append(x)
print(result)
if len(result) == 2:
    print("NOTE:",a,"is a Prime number.")
