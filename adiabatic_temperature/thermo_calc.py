import properties as prop
import input_data as i_d

class Thermo():
    heat_in  = 0        # kJ/s
    heat_out = 0        # kJ/s

    # skip sensible heat of waste
    def energy_in(self, V, species):
        # primary air sensible heat
        gas = prop.AIR()
        self.heat_in += gas.enthalpy(i_d.pa_temperature)*V*i_d.pa_alpha*i_d.B/3600.0

        # secondary air sensible heat
        self.heat_in += gas.enthalpy(i_d.sa_temperature)*V*i_d.sa_alpha*i_d.B/3600.0
        
        # waste
        self.heat_in += i_d.LHV*i_d.B*(1.0-(i_d.q3+i_d.q4)/100.0)/3600.0
        
    def energy_out(self):
        # heat carried out by ash (100% of Ash)
        ash = prop.ASH()
        heat_out = i_d.B*i_d.Ash/100.0*ash.enthalpy(i_d.ash_temperature)/3600.0


    def temp_calc(self, V, Vy, species):
        self.energy_in(V, species)
        self.energy_out()

        net = self.heat_in - self.heat_out
        flue_gas_energy = 0
        T = 273.15+1000
        state = 0
        
        gas = prop.FLUE()
        flue_gas_energy = gas.enthalpy(T, species)*Vy*i_d.B/3600.0
        
        while True:
            gas = prop.FLUE()
            flue_gas_energy = gas.enthalpy(T, species)*Vy*i_d.B/3600.0
            if (flue_gas_energy > net and state != 1):
                T -= 1
                state = 2
            elif (flue_gas_energy < net and state != 2):
                T += 1
                state = 1
            else:
                break

            if(T > 1500 or T < 500):
                print('Error: Temperature > 1500K or Temperature < 500K!')
                break

        return T