import input_data as i_d

class Check:
    state = 0
    eps = 1.0e-6

    def proximate(self):
        if i_d.others < 0:
            print('Warning: proximate analysis not balance!')
            self.state = 1

    def ultimate(self):
        if abs((i_d.M+i_d.V+i_d.FC+i_d.Ash)-100) > self.eps:
            print('Warning: ultimate analysis not balance!')
            self.state = 1

    def check_input(self):
        self.proximate()
        self.ultimate()
        if self.state == 1:
            print('Warning in the input data, exit!')
            return False
        else:
            print('No Warning in the input data, continue!')
            return True
