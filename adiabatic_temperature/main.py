# main file
import input_check as i_c
import flue_gas as f_g
import thermo_calc as t_c

def main():
    # check input data
    chk = i_c.Check()
    if(chk.check_input() == False):
        exit()

    # calculate flue gas
    flue = f_g.FlueGas()
    V, Vy, species = flue.calc()

    # calculate enthalpy and furnance outlet temperature
    fnc = t_c.Thermo()
    T = fnc.temp_calc(V, Vy, species)

    print(T-273.15)


if __name__ == "__main__":
    main()
