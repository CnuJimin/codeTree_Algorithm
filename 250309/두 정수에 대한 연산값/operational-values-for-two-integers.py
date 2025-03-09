a, b = map(int, input().split())

def change(a,b):

    if a > b:
        a = a + 25
        b *= 2
    else:
        a *= 2
        b += 25

    return a,b

a,b = change(a,b)

print(a,b)