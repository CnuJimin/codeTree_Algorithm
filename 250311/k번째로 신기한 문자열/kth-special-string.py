n, k ,t = map(str, input().split())
n = int(n)
k = int(k)

arr = [input() for i in range(n)]

wordList = []

for i in arr:
    if i[:len(t)] == t:
        wordList.append(i)


wordList.sort()

print(wordList[k-1])