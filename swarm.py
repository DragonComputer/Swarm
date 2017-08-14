import sys
import math
import random

class Program:

    def __init__(self, filename):
        self.variable = []
        self.pointer1 = -1
        self.pointer2 = -2
        self.pointer3 = -3
        self.power_of_ten = 0

        with open(filename) as f:
            program = ''.join(line.strip() for line in f)
            #print program
            program = [program[i:i + 2] for i in range(0, len(program), 2)]
            program = self.parse(program)
            #print program
            self.x00()
            self.x00()
            self.x00()
            self.execute(program)

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
        sign = self.pointer1 / self.pointer1
        self.pointer1 = sign * (self.pointer1 % len(self.variable))

    # decrease pointer1
    def x19(self):
        self.pointer1 -= 1
        sign = self.pointer1 / self.pointer1
        self.pointer1 = sign * (self.pointer1 % len(self.variable))

    # increase pointer2
    def x1A(self):
        self.pointer2 += 1

    # decrease pointer2
    def x1B(self):
        self.pointer2 -= 1

    # if
    def x1C(self):
        if self.variable[self.pointer1]:
            return True
        else:
            return False

    # if not
    def x1D(self):
        if not self.variable[self.pointer1]:
            return True
        else:
            return False

    # end
    def x1E(self):
        pass

    # while
    def x1F(self):
        if self.variable[self.pointer1]:
            return True
        else:
            return False

    # unless
    def x20(self):
        if not self.variable[self.pointer1]:
            return True
        else:
            return False

    # break
    def x21(self):
        pass

    # abs
    def x22(self):
        self.variable[self.pointer1] = abs(self.variable[self.pointer1])

    # ceil
    def x23(self):
        self.variable[self.pointer1] = math.ceil(self.variable[self.pointer1])

    # cmp
    def x24(self):
        self.variable[self.pointer1] = cmp(self.variable[self.pointer1], self.variable[self.pointer2])

    # exp
    def x25(self):
        self.variable[self.pointer1] = math.exp(self.variable[self.pointer1])

    # fabs
    def x26(self):
        self.variable[self.pointer1] = math.fabs(self.variable[self.pointer1])

    # floor
    def x27(self):
        self.variable[self.pointer1] = math.floor(self.variable[self.pointer1])

    # log
    def x28(self):
        self.variable[self.pointer1] = math.log(self.variable[self.pointer1])

    # log10
    def x29(self):
        self.variable[self.pointer1] = math.log10(self.variable[self.pointer1])

    # max
    def x2A(self):
        self.variable[self.pointer1] = max(self.variable[self.pointer1])

    # min
    def x2B(self):
        self.variable[self.pointer1] = min(self.variable[self.pointer1])

    # modf
    def x2C(self):
        self.variable[self.pointer1] = math.modf(self.variable[self.pointer1])

    # pow
    def x2D(self):
        self.variable[self.pointer1] = math.pow(self.variable[self.pointer1], self.variable[self.pointer2])

    # round
    def x2E(self):
        self.variable[self.pointer1] = round(self.variable[self.pointer1], self.variable[self.pointer2])

    # sqrt
    def x2F(self):
        self.variable[self.pointer1] = math.sqrt(self.variable[self.pointer1])

    # choice
    def x30(self):
        self.variable[self.pointer1] = random.choice(self.variable[self.pointer1])

    # randrange
    def x31(self):
        self.variable[self.pointer1] = random.randrange(self.variable[self.pointer1], self.variable[self.pointer2], self.variable[self.pointer3])

    # random
    def x32(self):
        self.variable[self.pointer1] = random.random()

    # seed
    def x33(self):
        random.seed(self.variable[self.pointer1])

    # shuffle
    def x34(self):
        random.shuffle(self.variable[self.pointer1])

    # uniform
    def x35(self):
        self.variable[self.pointer1] = random.uniform(self.variable[self.pointer1], self.variable[self.pointer2])

    # acos
    def x36(self):
        self.variable[self.pointer1] = math.acos(self.variable[self.pointer1])

    # asin
    def x37(self):
        self.variable[self.pointer1] = math.asin(self.variable[self.pointer1])

    # atan
    def x38(self):
        self.variable[self.pointer1] = math.atan(self.variable[self.pointer1])

    # atan2
    def x39(self):
        self.variable[self.pointer1] = math.atan2(self.variable[self.pointer1], self.variable[self.pointer2])

    # cos
    def x3A(self):
        self.variable[self.pointer1] = math.cos(self.variable[self.pointer1])

    # hypot
    def x3B(self):
        self.variable[self.pointer1] = math.hypot(self.variable[self.pointer1], self.variable[self.pointer2])

    # sin
    def x3C(self):
        self.variable[self.pointer1] = math.sin(self.variable[self.pointer1])

    # tan
    def x3D(self):
        self.variable[self.pointer1] = math.tan(self.variable[self.pointer1])

    # degrees
    def x3E(self):
        self.variable[self.pointer1] = math.degrees(self.variable[self.pointer1])

    # radians
    def x3F(self):
        self.variable[self.pointer1] = math.radians(self.variable[self.pointer1])

    # assign pi
    def x40(self):
        self.variable[self.pointer1] = math.pi

    # assign e
    def x41(self):
        self.variable[self.pointer1] = math.e


    # parse the nested statements
    def parse(self,program):
        result = []
        list_ref = result
        list_refs_stack = []
        while len(program) > 0:
            inst = program.pop(0)
            if inst == '1C' or inst == '1D' or inst == '1F' or inst == '20':
                list_ref.append(inst)
                list_ref.append([])
                list_refs_stack.append(list_ref)
                list_ref = list_ref[-1]
            elif inst == '1E':
                if list_refs_stack:
                    list_ref = list_refs_stack.pop()
                list_ref.append(inst)
            else:
                list_ref.append(inst)
        return result

    # execute the given program
    def execute(self,program):
        #print program
        i = 0
        while i < len(program):
            if program[i] == '1C' or program[i] == '1D':
                if eval('self.x' + program[i] + '()'):
                    self.execute(program[i+1])
            elif program[i] == '1F' or program[i] == '20':
                while eval('self.x' + program[i] + '()'):
                    if self.execute(program[i+1]) == "break":
                        break
            else:
                if program[i] == '21':
                    return "break"
                try:
                    eval('self.x' + program[i] + '()')
                except:
                    pass
            i += 1

if __name__ == "__main__":
    Program(sys.argv[1])
