#Week4 Assignmentr Part2 Michael Connell

class Car:
    def __init__(self, year_model, make):
        # Constructor method that initializes the data attributes
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        # Method that increases the car's speed by 5
        self.__speed += 5

    def brake(self):
        # Method that decreases the car's speed by 5
        self.__speed -= 5

    def get_speed(self):
        # Accessor method for the speed attribute
        return self.__speed


# Create a Car object
my_car = Car(2021, 'Toyota')

# Call the accelerate method five times and display the current speed after each call
for i in range(5):
    my_car.accelerate()
    print('Current speed:', my_car.get_speed())

# Call the brake method five times and display the current speed after each call
for i in range(5):
    my_car.brake()
    print('Current speed:', my_car.get_speed())