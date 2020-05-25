class Car:

    def __init__(self, model, engine_type, max_speed):
        self.model = model
        self.engine_type = engine_type
        self.max_speed = max_speed

    def move(self):
        print(f'The car {self.model} with speed {self.max_speed} is moving')

    def stop_engine(self):
        print(f'The car {self.model} has been stopped')

    def get_max_speed(self):
        print(f'Max speed is {self.max_speed}')


class Truck(Car):

    def move(self):
        print('Truck is moving')

    def offload(self):
        print('The items are being offloaded')

    def increment_speed(self, value):
        self.max_speed += value



car = Truck('MAN', 'V-12', 140)

car.move()
# car.offload()
# car.increment_speed(1)
# car.get_max_speed()

car2 = Car('audi', 'v-6', 240)
car2.move()