word_1 = input()
word_2 = input()

word_1 = "".join(sorted(word_1))
word_2 = "".join(sorted(word_2))

if word_1 == word_2:
    print("Yes")
else:
    print("No")