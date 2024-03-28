from restaurant import Restaurant

class IceCreamStand(Restaurant):
    flavors : list
    
    def __init__(self, restaurant_name, cuisine_type, flavors) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.customers_served = 0
        
    def display_flavors(self) -> None:
        for flavor in self.flavors:
            print(flavor, end=', ')

my_flavors : list = ['Vanilla', 'Chocolate', 'Strawberry', 'Cookies & Creme']
my_stand = IceCreamStand('Ice Cream Stand', 'Ice Cream', my_flavors)
my_stand.display_flavors()