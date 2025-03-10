word = input()
part = input()

def contains(word, part):
    if part in word:
        return word.index(part)
    return -1 

print(contains(word, part))