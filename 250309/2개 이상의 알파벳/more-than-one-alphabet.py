word = input()

def up(word):
    arr = list(word)

    if len(set(arr)) >= 2:
        return "Yes"
    else:
        return "No"

print(up(word))