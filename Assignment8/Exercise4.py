import random
class Car:
    def __init__(self, registration_num, max_speed):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_dis = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_dis += self.current_speed * hours

class Race:
    def __init__(self, name, dis_km, car_list):
        self.name = name
        self.dis_km = dis_km
        self.car_list = car_list
        self.hour = 0

    def hours_passes(self):
        for car in self.car_list:
            change = random.randint(-10,15)
            car.accelerate(change)
            car.drive(1)
            self.hour += 1

    def print_status(self):
        header = f"{"Registration Number":<20} {"Max Speed":<12} {"Current Speed":<15} {"Distance":<10}"
        print(header)
        for car in self.car_list:
            reg = car.registration_num
            max_s = f"{car.max_speed}km/h"
            cur_speed = f"{car.current_speed}km/h"
            dist = f"{car.travelled_dis:.1f}"
            print(f"{reg:<21} {max_s:<14} {cur_speed:<13} {dist:<10}")

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_dis > self.dis_km:
                return True
        return False

if __name__ == "__main__":
    cars = []
    for i in range(1,11):
        register = f"ABC-{i}"
        maxi_speed = random.randint(150,200)
        cars.append(Car(register, maxi_speed))

    derby = Race("Grand Demolition Derby", 8000, cars)
    while not derby.race_finished():
        derby.hours_passes()
        if derby.hour % 10 == 0:
            print()
            derby.print_status()

    final = "RACE FINISHED"
    print(f"\n" + final.center(70))
    derby.print_status()