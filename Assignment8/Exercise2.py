class Elevator:
    def __init__(self, bottom_floor, top_floor, elevator_id):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        self.elevator_id = elevator_id

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"The elevator {self.elevator_id} is going up, current floor is: {self.current_floor}.")
        else:
            print("You are on the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"The elevator {self.elevator_id} is going down, current floor is: {self.current_floor}.")
        else:
            print("You are on the bottom floor.")

    def go_to_floor(self, destination):
        if destination < self.bottom_floor or destination > self.top_floor:
            print(f"The elevator {self.elevator_id} is not moving. The number of floors is outside the range.")
            return
        if destination > self.current_floor:
            while self.current_floor < destination:
                self.floor_up()
        elif destination < self.current_floor:
            while self.current_floor > destination:
                self.floor_down()
        else:
            print("You are on the right floor.")
        print(f"The elevator {self.elevator_id} arrived at floor: {self.current_floor}.")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.num_elevators = num_elevators

        self.elevators = []
        for i in range(num_elevators):
            new_ele = Elevator(bottom_floor, top_floor, elevator_id=i+1)
            self.elevators.append(new_ele)

    def run_elevator(self, elevator_num, destination_floor):
        if 1 <= elevator_num <= self.num_elevators:
            print()
            ele = self.elevators[elevator_num -1]
            ele.go_to_floor(destination_floor)
        else:
            print(f"\nThe elevator must be between 1 and {self.num_elevators}.")
if __name__ =="__main__":
    building = Building(0,10,3)

    building.run_elevator(1,7)
    building.run_elevator(2,2)
    building.run_elevator(3,8)
    building.run_elevator(4,10)
    building.run_elevator(1,11)