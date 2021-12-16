## Energy and Gas ##
from spike import PrimeHub, DistanceSensor, Motor, MotorPair

hub = PrimeHub()
hub.light_matrix.show_image("SWORD")
distance = DistanceSensor("C")
tires = MotorPair("E", "F")
gray_clawie = Motor("B")
yellow_clawie = Motor("A")

# Go to Motor and make it electric
tires.start(speed=40)
while distance.get_distance_inches() > 13:
    pass
tires.stop()

tires.move_tank(4, "in", left_speed=53, right_speed=35)
gray_clawie.run_for_rotations(-0.5, speed=20)
tires.move_tank(4, "in", left_speed=50, right_speed=20)
tires.move_tank(3.5, "in", left_speed=25, right_speed=20)
gray_clawie.run_for_rotations(0.3, speed=15)

# # Return back for Cargo Unload
tires.move_tank(-1, "in", left_speed=10, right_speed=10)
tires.move_tank(-16, "in", left_speed=50, right_speed=25)
tires.move_tank(-3, "in", left_speed=25, right_speed=50)
tires.move_tank(11, "in", left_speed=30, right_speed=26)
gray_clawie.run_for_rotations(-0.5, speed=35)

# Truck
tires.move_tank(-29, "in", left_speed=39, right_speed=31)

# # Fill Up Crate
tires.move_tank(44, "in", left_speed=50, right_speed=45)
