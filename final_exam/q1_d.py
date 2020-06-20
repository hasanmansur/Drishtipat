# S M HASAN MANSUR
# G01143027

# Z_S calculation for question 1(d)

import math
H = 2.1336 * 1000 * 87.2
R_D = math.sqrt((1174 - 1180)**2 +(745-1028)**2)
V3_C = math.sqrt((786-1168)**2 + (-17572 - 462)**2)
C_D = math.sqrt((1168-1180)**2 + (462-1028)**2)
V3_R = math.sqrt((786-1174)**2 + (-17572 -745)**2)

Z_S = (H * R_D * V3_C) / (C_D * V3_R)
print("Z_S", Z_S)

X_S = (212 * 91587.711) / 1569
print("X_S", X_S)

Y_S =  (384 * 91587.711) / 1569
print("Y_S", Y_S)

D = -0.0034 * 12375.14 + .99 * 22415.34 - 0.084 * 91587.711
print("D", D)
