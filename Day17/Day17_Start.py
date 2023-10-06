class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user1 = User("001", "moon")

print(user1.id)

