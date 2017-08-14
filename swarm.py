import sys

class Program:

    def __init__(self, filename):
        self.variable = []
        self.pointer1 = -1
        self.pointer2 = -2
        self.power_of_ten = 0
        self.control_lock = False

        with open(filename) as f:
            program = ''.join(line.strip() for line in f)
            #print program
            program = [program[i:i + 2] for i in range(0, len(program), 2)]
            for func in program:
                if func == '1E':
                    self.control_lock = False
                if not self.control_lock:
                    try:
                        eval('self.x' + func + '()')
                    except:
                        pass

    # create a new variable
    def x00(self):
        self.variable.append(None)

    # print all variables
    def x01(self):
        print self.variable

    # assign an integer value
    def x02(self):
        self.variable[self.pointer1] = 0

    # assign a float value
    def x03(self):
        self.variable[self.pointer1] = 0.0

    # assign a string value
    def x04(self):
        self.variable[self.pointer1] = ""

    # + 1
    def x05(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] + 1 * (10 ** self.power_of_ten)

    # - 1
    def x06(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] - 1 * (10 ** self.power_of_ten)

    # power of ten + 1
    def x07(self):
        self.power_of_ten = self.power_of_ten + 1

    # power of ten - 1
    def x08(self):
        self.power_of_ten = self.power_of_ten - 1

    # addition
    def x09(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] + self.variable[self.pointer2]

    # subtraction
    def x0A(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] - self.variable[self.pointer2]

    # multiplication
    def x0B(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] * self.variable[self.pointer2]

    # division
    def x0C(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] / self.variable[self.pointer2]

    # modulus
    def x0D(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] % self.variable[self.pointer2]

    # exponent
    def x0E(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] ** self.variable[self.pointer2]

    # floor division
    def x0F(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] // self.variable[self.pointer2]

    # assign False
    def x10(self):
        self.variable[self.pointer1] = False

    # assign True
    def x11(self):
        self.variable[self.pointer1] = True

    # == (equal)
    def x12(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] == self.variable[self.pointer2]

    # != (not equal)
    def x13(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] != self.variable[self.pointer2]

    # > (greater than)
    def x14(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] > self.variable[self.pointer2]

    # < (less than)
    def x15(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] < self.variable[self.pointer2]

    # >= (greater than or equal)
    def x16(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] >= self.variable[self.pointer2]

    # <= (less than or equal)
    def x17(self):
        self.variable[self.pointer1] = self.variable[self.pointer1] <= self.variable[self.pointer2]

    # increase pointer1
    def x18(self):
        self.pointer1 += 1

    # decrease pointer1
    def x19(self):
        self.pointer1 -= 1

    # increase pointer2
    def x1A(self):
        self.pointer2 += 1

    # decrease pointer2
    def x1B(self):
        self.pointer2 -= 1

    # if
    def x1C(self):
        if self.variable[self.pointer1]:
            self.control_lock = False
        else:
            self.control_lock = True

    # if not
    def x1D(self):
        if not self.variable[self.pointer1]:
            self.control_lock = False
        else:
            self.control_lock = True

    # end control
    def x1E(self):
        self.control_lock = False

if __name__ == "__main__":
    Program(sys.argv[1])
