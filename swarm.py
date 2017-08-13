import sys

class Program:

    def __init__(self, filename):
        self.variable = []
        self.pointer1 = -1
        self.pointer2 = -2
        self.power_of_ten = 0

        with open(filename) as f:
            program = ''.join(line.strip() for line in f)
            #print program
            for func in program:
                try:
                    eval('self.x' + func + '()')
                except:
                    pass

    # Create a new variable
    def x0(self):
        self.variable.append(None)

    # Print all variables
    def x1(self):
        print self.variable

    # Assign an integer value
    def x2(self):
        self.variable[self.pointer1] = 0

    # Assign a float value
    def x3(self):
        self.variable[self.pointer1] = 0.0

    # Assigne a string value
    def x4(self):
        self.variable[self.pointer1] = ""

    # + 1
    def x5(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] + 1 * (10 ** self.power_of_ten)

    # - 1
    def x6(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] - 1 * (10 ** self.power_of_ten)

    # power of ten + 1
    def x7(self):
        self.power_of_ten = self.power_of_ten + 1

    # power of ten - 1
    def x8(self):
        self.power_of_ten = self.power_of_ten - 1

    # addition
    def x9(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] + self.variable[self.pointer2]

    # subtraction
    def xA(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] - self.variable[self.pointer2]

    # multiplication
    def xB(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] * self.variable[self.pointer2]

    # division
    def xC(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] / self.variable[self.pointer2]

    # modulus
    def xD(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] % self.variable[self.pointer2]

    # exponent
    def xE(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] ** self.variable[self.pointer2]

    # floor division
    def x9(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] // self.variable[self.pointer2]

if __name__ == "__main__":
    Program(sys.argv[1])
