class User:
    first_name : str
    last_name : str
    followers : int
    age : int
    login_attempts : int

    def __init__(self, first_name, last_name, followers, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.followers = followers
        self.age = age
        self.login_attempts = 0

    def describe_user(self) -> None:
        print(f"{self.first_name} {self.last_name} is {self.age} years old and has {self.followers} followers.")
    
    def greet_user(self) -> None:
        print(f"Hello, {self.first_name}, glad to see you back again.")

    def increment_login_attempts(self) -> None:
        self.login_attempts += 1
    
    def reset_login_attempts(self) -> None:
        self.login_attempts = 0

user1 = User('Logan', 'Brooks', 400, 20)
user2 = User('Robert', 'Fripp', 400000, 77)
user3 = User('Johnny', 'Five', 5, 55)

users : list = [user1, user2, user3]

for user in users:
    user.describe_user()
    user.greet_user()

while user1.login_attempts < 3:
    user1.increment_login_attempts()
    print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)