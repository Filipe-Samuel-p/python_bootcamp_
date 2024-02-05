class User:
   def __init__(self,username) -> None:
      self.id = username

user_1 = User("Filipe")

print(user_1.id)