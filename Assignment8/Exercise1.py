class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"The elevator is going up, current floor is: {self.current_floor}.")
        else:
            print("You are on the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"The elevator is going down, current floor is: {self.current_floor}.")
        else:
            print("You are on the bottom floor.")

    def go_to_floor(self, destination):
        if destination < self.bottom_floor or destination > self.top_floor:
            print("The number of floors is outside the range.")
            return
        if destination > self.current_floor:
            while self.current_floor < destination:
                self.floor_up()
        elif destination < self.current_floor:
            while self.current_floor > destination:
                self.floor_down()
        else:
            print("You are on the right floor.")
        print(f"Arrived at floor: {self.current_floor}.")

if __name__ == "__main__":
    h = Elevator(0,10)
    print(f"\nGoing to floor 5")
    h.go_to_floor(5)
    print(f"\nGoing back the bottom floor")
    h.go_to_floor(0)
    print(f"\nGoing to a random floor")
    h.go_to_floor(7)
    h.go_to_floor(11)
    h.go_to_floor(-3)
    h.go_to_floor(0)
