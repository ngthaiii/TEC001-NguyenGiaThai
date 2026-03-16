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

if __name__ == "__main__":
    merc = Car("ABC-123", 142)
    merc.accelerate(30)
    merc.accelerate(70)
    merc.accelerate(50)
    print(f"The speed after acceleration is: {merc.current_speed} km/h.")
    merc.accelerate(-200)
    print(f"The final speed is: {merc.current_speed} km/h.")