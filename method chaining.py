# method chaining = calling multiple methods  sequentially
#                   each call performs an action  on the same object and return self

class Car:
    def turn_on(self):
        print("You can start the engine")
        return self

    def drive(self):
        print("You can drive the car")
        return self

    def brake(self):
        print("You can step on the brake")
        return self

    def tun_off(self):
        print("You can stop the car")
        return self

car = Car()

#car.turn_on().drive()
#car.brake().tun_off()

car.turn_on().drive().car.brake().tun_off()

car.turn_on()\
    .drive()\
    .car.brake()\
    .tun_off()
