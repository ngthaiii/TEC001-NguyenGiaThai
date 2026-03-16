import random
class Car:
    def __init__(self, registration_num, max_speed):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

if __name__ == "__main__":
    cars = []
    for i in range(1,11):
        register = f"ABC-{i}"
        maxi_speed = random.randint(150, 200)
        cars.append(Car(register, maxi_speed))

    hour = 0
    while True:
        hour += 1
        for car in cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

        if any(car.travelled_distance >= 10000 for car in cars):
            break
    print("{:<21} {:<15} {:<15} {:<20}".format(
        "Registration Number", "Max Speed", "Current Speed", "Travelled Distance"))
    for car in cars:
        print("{:^20} {:^12} {:^23} {:^10.1f}".format(
        car.registration_num,
        f"{car.max_speed} km/h",
        f"{car.current_speed} km/h",
        car.travelled_distance))