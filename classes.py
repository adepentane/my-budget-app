class Car:
    def __init__(self, car_name, car_color, car_model):
        self.car_name = car_name
        self.car_color = car_color
        self.car_model = car_model

    def accel(self):
        print(f'{self.car_name} accelerate at 180 mph')

car_1 = Car('Mercedese', 'Silver', '2006')
car_2 = Car('Audi', 'Black', '2021')

car_1.accel()

print(car_1.car_name, car_1.car_color)
