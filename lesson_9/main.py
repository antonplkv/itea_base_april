class Car:

    def __init__(self, model, engine_type, max_speed):
        self.model = model
        self.engine_type = engine_type
        self.max_speed = max_speed

    def move(self):
        print(f'The car {self.model} is moving')

    def stop_engine(self):
        print(f'The car {self.model} has been stopped')

    def get_max_speed(self):
        print(f'Max speed is {self.max_speed}')




car = Car('audi', 'v-6', 240)

car.move()
car.stop_engine()

car.model = 'mercedes'

car.get_max_speed()



print('*' * 10)
car2 = Car('bmw', 'v-8', 260)

car2.move()
car2.stop_engine()
car2.get_max_speed()
print(car2.model, car2.engine_type, car2.max_speed)




