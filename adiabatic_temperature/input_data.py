# should be specified first

# waste feed
B = 750*1000/24         # kg/h

# waste properties
# ultimate analysis (ar)
M = 43
V = 32
FC = 4
Ash = 21

# proximate analysis (ar)
C = 19.23
H = 2.66
O = 13.21
N = 0.46
S = 0.09
Cl = 0.32
others = 100 - (C+H+O+N+S+Cl+M+Ash)       # must be positive or zero

# low heat value (ar)
LHV = 1600*4.1868       # kJ/kg

# excess air ratio
alpha = 1.8             # must be large than 1


# primary air
pa_alpha = 1.3
pa_temperature = 273.15+220

# secondary air
sa_alpha = alpha - pa_alpha
sa_temperature = 273.15+40

# Ash temperature
ash_temperature = 273.15+220+200

# Furnance efficiency
q3 = 0.5
q4 = 2.5