a = []
if len(a) == 0:
    print("Empty list! Please try again.")
else:
    result = 1
    for x in a:
        result*=x
    print(str(result)[-1])
