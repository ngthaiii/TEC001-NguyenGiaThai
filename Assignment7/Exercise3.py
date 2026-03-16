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
    merc = Car("ABC-123", 142)
    merc.travelled_distance = 2000
    merc.current_speed = 60
    merc.drive(1.5)
    print(f"The travelled distance in 1.5h is: {int(merc.travelled_distance)} km.")