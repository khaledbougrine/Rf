import numpy as np
import cmath

N = 303
P = 303
PI = np.pi
DELTA_PHI = 2 * PI / P
KVar = cmath.exp(1j * 2 * cmath.pi / 3)
conjK = cmath.exp(-1j * 2 * cmath.pi / 3)
f = np.linspace(4000, 15000, 10000)
R = 2  # cm
z_0 = 50
z0=50

