import numpy as np
import matplotlib.pyplot as plt
from sympy import diff,sin,cos,tan,atan,symbols
n1=np.array([3,-6,-2])
n2=np.array([2,1,-2])
direction_vector=np.cross(n1,n2)
print("intersection line:",direction_vector)
