from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
tire = MotorPair('E', 'F')

# Home Delivery Code

tire = MotorPair('E', 'F')

tire.move_tank(-10, 'in', left_speed=42, right_speed=40)
tire.move_tank(-30, 'in', left_speed=40, right_speed=41)
tire.move_tank(-16, 'in', left_speed=40, right_speed=46)
tire.move_tank(-4, 'in', left_speed=70, right_speed=38)
