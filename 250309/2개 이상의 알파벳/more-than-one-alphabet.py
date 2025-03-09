word = input()

# def up(word):
#     arr = list(word)

#     if len(set(arr)) >= 2:
#         return "Yes"
#     else:
#         return "No"

# print(up(word))


def up(word):
    cnt = 0
    for i in range(len(word) -1 ):
        if word[i] != word[i+1]:
            cnt += 1
    
    if cnt >= 2:
        return "Yes"
    else:
        return "No"

print(up(word))
      

