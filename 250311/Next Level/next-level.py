name, level = map(str, input().split())

class User:
    def __init__(self, ID = "codetree", lv = 10):
        self.ID = ID
        self.lv = lv

user1 = User()
user2 = User(name, level)

print(f"user {user1.ID} lv {user1.lv}")
print(f"user {user2.ID} lv {user2.lv}")