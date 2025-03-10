n = int(input())

def helloWorld(n):
    if n == 0 :
        return 

    helloWorld(n - 1)
    print("HelloWorld")

helloWorld(n)