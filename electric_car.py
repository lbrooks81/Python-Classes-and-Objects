from car import Car

class Battery:
    """Models a battery for an electric car."""
    battery_size : int
    
    def __init__(self, battery_size=40) -> None:
        self.battery_size = battery_size
    
    def describe_battery(self) -> None:
        print(f"This car has a {self.battery_size}=kWh battery.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    battery : Battery

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self) -> None:
        print("This car doesn't need a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.fill_gas_tank()