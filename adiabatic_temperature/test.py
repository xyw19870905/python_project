from properties import *
from flue_gas import *

# test for species properties(enthalpy)

test_co2 = CO2()
print(test_co2.enthalpy(273.15+1000))

test_h2o = H2O()
print(test_h2o.enthalpy(273.15+1000))

test_o2  = O2()
print(test_o2.enthalpy(273.15+1000))

test_n2 = N2()
print(test_n2.enthalpy(273.15+1000))

test_air = AIR()
print(test_air.enthalpy(273.15+1000))

test_flue = FLUE()
print(test_flue.enthalpy(273.15+1000, [1,0,0,0]))


# test for flue gas calculation
'''OK
test_flue = FlueGas()
print(test_flue.calc())
'''