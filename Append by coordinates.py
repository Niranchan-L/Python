a = [1,2,3,4,5,6,7,8,9,10,98]
b = [12,4,32,56,734,23,56,34,7,23]
c = []
# Expected Output:
#   [(1,12),(2,4),(3,32),...]

for x in range(min(len(a),len(b))):
    c.append((a[x],b[x]))
print(c)

print(list(zip(a, b)))