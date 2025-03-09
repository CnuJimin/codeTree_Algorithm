n,m = map(int, input().split())

def swap(a,b):
    a,b = b,a

    return a,b

a, b = swap(n,m)
print(a,b)