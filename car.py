class Car:
    """A simple attempt to represent a car."""

    make : str
    model : str
    year : int
    odometer_reading : int

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self) -> str:
        """Returns a neatly formatted descriptive name."""
        return f"{self.year} {self.make} {self.model}".title()
    
    def read_odometer(self) -> None:
        """Prints a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage : int) -> None:
        """
        Sets the odometer reading to the given value.
        Rejects the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

        