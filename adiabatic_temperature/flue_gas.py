# skip N/S/Cl

import input_data as i_d

class FlueGas():
    V0  = 0                 # Nm^3/kg
    V   = 0                 # Nm^3/kg
    Vy0 = 0                 # Nm^3/kg
    Vy  = 0                 # Nm^3/kg
    species = [0,0,0,0]     # for CO2/H2O/O2/N2 mole fraction

    def air(self):
        self.V0 = 0.0889*i_d.C + 0.265*i_d.H - 0.0333*i_d.O
        self.V  = i_d.alpha*self.V0

    def flue(self):
        self.air()
        V_CO2    = 0.01867*i_d.C
        V_N2_0   = 0.008*i_d.N + 0.79*self.V0
        V_H2O_0  = 0.111*i_d.H + 0.0124*i_d.M
        self.Vy0 = V_CO2 + V_N2_0 + V_H2O_0
        self.Vy  = self.Vy0 + (i_d.alpha-1)*self.V0

        self.species[0] = V_CO2/self.Vy
        self.species[1] = V_H2O_0/self.Vy
        self.species[3] = (V_N2_0+(i_d.alpha-1)*self.V0*0.79)/self.Vy
        self.species[2] = 1.0 - (self.species[0]+self.species[1]+self.species[3])

    def calc(self):
        self.flue()
        return self.V, self.Vy, self.species
