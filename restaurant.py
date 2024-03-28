class Restaurant:
    restaurant_name : str
    cuisine_type : str
    customers_served : int

    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.customers_served = 0
        
    def describe_restaurant(self) -> None:
        print(f"Our restaurant, {self.restaurant_name}, serves {self.cuisine_type}")
    
    def open_restaurant(self) -> None:
        print(f"Welcome to {self.restaurant_name}! We are now open!")
    
    def set_customers_served(self, number_served) -> None:
        self.customers_served = number_served

    def increment_customers_served(self, number_served) -> None:
        self.customers_served += number_served
    
my_restaurant = Restaurant("Pizza Planet", "Pizza")

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()

print(f'Customers served: {my_restaurant.customers_served}')

my_restaurant.set_customers_served(20)
print(f'Customers served: {my_restaurant.customers_served}')

my_restaurant.increment_customers_served(20)
print(f'Customers served: {my_restaurant.customers_served}')

