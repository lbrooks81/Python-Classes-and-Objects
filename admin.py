from user import User

class Privileges:
    """Class names should be singular"""
    privileges : list

    def __init__(self, privileges) -> None:
        self.privileges = privileges

    def show_privileges(self) -> None:
        for privilege in self.privileges:
            print(privilege, end=', ')

class Admin(User):
    privileges : Privileges
    
    def __init__(self, first_name, last_name, followers, age, privileges) -> None:
        super().__init__(first_name, last_name, followers, age)
        self.privileges = privileges
    
    

privileges = Privileges(['Can add post', 'Can delete post', 'Can delete user'])
admin = Admin('Pete', 'Gabe', 1000000, 74, privileges)
admin.privileges.show_privileges()