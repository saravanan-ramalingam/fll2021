from spike import PrimeHub, Motor, MotorPair

hub = PrimeHub()
tire = MotorPair('E', 'F')
claw = Motor('B')

tire.move_tank(20, unit='in', left_speed=62, right_speed=50)
tire.move_tank(26, unit='in', left_speed=50, right_speed=50)
tire.move_tank(2, unit='in', left_speed=12, right_speed=2)
claw.run_for_rotations(-0.6, speed=20)
tire.move_tank(12, unit='in', left_speed=20, right_speed=20)

# Start to reach the Helicopter
tire.move_tank(-8, unit='in', left_speed=30, right_speed=40)
tire.move_tank(9, unit='in', left_speed=40, right_speed=40)
tire.move_tank(4, unit='in', left_speed=30, right_speed=65)
tire.move_tank(12, unit='in', left_speed=30, right_speed=35)
tire.move_tank(5, unit='in', left_speed=35, right_speed=30)

# Start to Move the train
tire.move_tank(-5, 'in', left_speed=10, right_speed=50)
claw.run_for_rotations(-0.4, speed=20)
tire.move_tank(8, 'in', left_speed=25, right_speed=20)
tire.move_tank(9, 'in', left_speed=22, right_speed=20)

# Turn around and come back to base
tire.move_tank(-1, 'in', left_speed=20, right_speed=20)
tire.move_tank(-7, 'in', left_speed=20, right_speed=50)
tire.move_tank(-2, 'in', left_speed=5, right_speed=10)
tire.move_tank(-2, 'in', left_speed=10, right_speed=5)
tire.move_tank(20, 'in', left_speed=30, right_speed=30)

# Hit the Bridge
claw.run_for_rotations(0.4, speed=20)
tire.move_tank(8, 'in', left_speed=30, right_speed=30)
claw.run_for_rotations(-0.4, speed=20)
tire.move_tank(-3, 'in', left_speed=30, right_speed=30)

# Return to Base
claw.run_for_rotations(0.4, speed=20)
tire.move_tank(13, 'in', left_speed=30, right_speed=30)
tire.move_tank(40, 'in', left_speed=30, right_speed=35)
