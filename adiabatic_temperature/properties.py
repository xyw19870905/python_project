# using Cantera for enthalpy calculation
# only consider major specise: CO2/H2O/O2/N2

import cantera as ct

class CO2:
    ''' Properties of CO2 '''
    def enthalpy(self, T):
        gas = ct.Solution('gri30.xml')
        gas.TPX = 273.15, ct.one_atm, 'CO2:1'
        h0 = gas.enthalpy_mass
        rho0 = gas.density
        gas.TPX = T, ct.one_atm, 'CO2:1'
        h1 = gas.enthalpy_mass

        return (h1-h0)*rho0/1000         # kJ/Nm3


class H2O:
    ''' Properties of H2O '''
    def enthalpy(self, T):
        gas = ct.Solution('gri30.xml')
        gas.TPX = 273.15, ct.one_atm, 'H2O:1'
        h0 = gas.enthalpy_mass
        rho0 = gas.density
        gas.TPX = T, ct.one_atm, 'H2O:1'
        h1 = gas.enthalpy_mass

        return (h1-h0)*rho0/1000         # kJ/Nm3


class O2:
    ''' Properties of O2 '''
    def enthalpy(self, T):
        gas = ct.Solution('gri30.xml')
        gas.TPX = 273.15, ct.one_atm, 'O2:1'
        h0 = gas.enthalpy_mass
        rho0 = gas.density
        gas.TPX = T, ct.one_atm, 'O2:1'
        h1 = gas.enthalpy_mass

        return (h1-h0)*rho0/1000         # kJ/Nm3



class N2:
    ''' Properties of N2 '''
    def enthalpy(self, T):
        gas = ct.Solution('gri30.xml')
        gas.TPX = 273.15, ct.one_atm, 'N2:1'
        h0 = gas.enthalpy_mass
        rho0 = gas.density
        gas.TPX = T, ct.one_atm, 'N2:1'
        h1 = gas.enthalpy_mass

        return (h1-h0)*rho0/1000         # kJ/Nm3


class AIR:
    ''' Properties of Air '''
    def enthalpy(self, T):
        gas = ct.Solution('gri30.xml')
        gas.TPX = 273.15, ct.one_atm, 'O2:0.21, N2:0.79'
        h0 = gas.enthalpy_mass
        rho0 = gas.density
        gas.TPX = T, ct.one_atm, 'O2:0.21, N2:0.79'
        h1 = gas.enthalpy_mass

        return (h1-h0)*rho0/1000         # kJ/Nm3


class ASH:
    ''' Properties of Ash '''
    def enthalpy(self, T):
        ''' using constant Cp 1230 J/kg/K '''
        return 1.23*(T-273.15)     # kJ/kg

class FLUE:
    ''' Properties of flue '''
    def enthalpy(self, T, sp):
        gas = ct.Solution('gri30.xml')
        gas.TPX = 273.15, ct.one_atm, 'CO2:%f, H2O:%f, O2:%f, N2:%f' % (sp[0], sp[1], sp[2], sp[3])
        h0 = gas.enthalpy_mass
        rho0 = gas.density
        gas.TPX = T, ct.one_atm, 'CO2:%f, H2O:%f, O2:%f, N2:%f' % (sp[0], sp[1], sp[2], sp[3])
        h1 = gas.enthalpy_mass

        return (h1-h0)*rho0/1000        # kJ/Nm3