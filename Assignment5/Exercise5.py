import random
def value_pi():
    try:
        total_points = int(input("Enter a random number of points:"))
    except ValueError:
        print("Please enter an integer.")
        return
    points_inside = 0
    for i in range(total_points):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x**2 + y**2 < 1:
            points_inside += 1
    if total_points > 0:
        pi = 4 * points_inside / total_points
        print(f"Approximate value of pi:{pi}")
    else:
        print("Number of point can not less than 0.")
value_pi()