a, b = map(int, input().split())

def change(a,b):
    max_value = max(a,b)
    min_value = min(a,b)

    return 25 + max_value, 2 * min_value

a,b = change(a,b)

print(b,a)