class Car:
    def __init__(self, registration_num, max_speed):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

if __name__ == "__main__":
    merc = Car("ABC-123", 142)
    print(f"The registration number is: {merc.registration_num}."
          f"\nThe max speed is: {merc.max_speed} km/h."
          f"\nThe current speed is: {merc.current_speed} km/h."
          f"\nThe travelled distance is: {merc.travelled_distance} km.")