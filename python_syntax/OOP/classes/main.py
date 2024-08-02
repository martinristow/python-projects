# The creation method of our empty class
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1 # na userot sto go zasleduvame mu go zgolemuvame brojot na sledbenici
        self.following += 1 # so ova si ja zgolemuvame listata na korisnici koj sto nie gi sledime

# One object of our class :)
user1 = User(1, "martin")

user2 = User(2, "ristov")

user1.follow(user2)
print(user2.followers)

