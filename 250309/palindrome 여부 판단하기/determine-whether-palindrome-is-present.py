word = input()

def palindrome(word):
    out = ""

    for i in range(len(word) -1 , -1, -1):
        out += word[i]
    
    return out

if word == palindrome(word):
    print("Yes")
else:
    print("No")