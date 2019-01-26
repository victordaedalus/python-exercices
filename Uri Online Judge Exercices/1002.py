"""
area = π . raio2
"""
# Import
import math

# Variables
area = None
raio = None
pi = None

# Execution

pi = 3.14159
raio = float(input())
area = pi * (math.pow(raio, 2))
print('A={:0.4f}'.format(area))
