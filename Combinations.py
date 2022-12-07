n = 12
r = 10
d = n-r
def fac(n):
    if n == 1:
        return n
    return (n*fac(n-1))
print(fac(n)//(fac(d)*fac(r)))