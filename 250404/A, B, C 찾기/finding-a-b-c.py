arr = list(map(int, input().split()))

arr.sort()

val = max(arr)

for a in range(1, val):
    for b in range(a, val):
        for c in range(b,val):
            result = []
            result.append(a)
            result.append(b)
            result.append(c)
            result.append(a+b)
            result.append(a+c)
            result.append(b+c)
            result.append(a+b+c)
            result.sort()
            if result == arr:
                print(a,b,c)