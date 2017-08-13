import sys

class Program:

    def __init__(self, filename):
        self.variable = []
        self.variable_pointer = -1

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

    # Assign an integer value to the current variable
    def x2(self):
        self.variable[self.variable_pointer] = 0

    # Assign a float value to the current variable
    def x3(self):
        self.variable[self.variable_pointer] = 0.0

    # Assigne a string value to the current variable
    def x4(self):
        self.variable[self.variable_pointer] = ""

    # + 1
    def x5(self):
        self.variable[self.variable_pointer] = self.variable[self.variable_pointer] + 1

if __name__ == "__main__":
    Program(sys.argv[1])
