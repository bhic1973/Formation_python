import os
import sys
from math import pi

import numpy as np

print(sys.version)
print(sys.executable)

print(os.listdir())

print(np.sin(2 * pi * np.array([0.25, 0.35, 0.76, 1.23])))

name = input("Enter your name: ")

print(f"Hello {name} ")
