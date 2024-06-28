#!/usr/bin/python3
from decimal import Decimal
import math
INPUT_MSG = 'm:'
speed_light_squared = Decimal(math.pow(300000000, 2))
mass = int(input(INPUT_MSG))
print(format(mass * speed_light_squared, 'f'))
