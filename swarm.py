import sys
import math
import random

class Program:

    def __init__(self, filename):
        self.variable = []
        self.pointer = []
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
        self.pointer.append(-len(self.variable))

    # print all variables
    def x01(self):
        print self.variable

    # assign an integer value
    def x02(self):
        self.variable[-1] = 0

    # assign a float value
    def x03(self):
        self.variable[-1] = 0.0

    # assign a string value
    def x04(self):
        self.variable[-1] = ""

    # + 1
    def x05(self):
        self.variable[-1] = self.variable[-1] + 1 * (10 ** self.power_of_ten)

    # - 1
    def x06(self):
        self.variable[-1] = self.variable[-1] - 1 * (10 ** self.power_of_ten)

    # power of ten + 1
    def x07(self):
        self.power_of_ten = self.power_of_ten + 1

    # power of ten - 1
    def x08(self):
        self.power_of_ten = self.power_of_ten - 1

    # addition
    def x09(self):
        self.variable[-1] = self.variable[-1] + self.variable[-2]

    # subtraction
    def x0A(self):
        self.variable[-1] = self.variable[-1] - self.variable[-2]

    # multiplication
    def x0B(self):
        self.variable[-1] = self.variable[-1] * self.variable[-2]

    # division
    def x0C(self):
        self.variable[-1] = self.variable[-1] / self.variable[-2]

    # modulus
    def x0D(self):
        self.variable[-1] = self.variable[-1] % self.variable[-2]

    # exponent
    def x0E(self):
        self.variable[-1] = self.variable[-1] ** self.variable[-2]

    # floor division
    def x0F(self):
        self.variable[-1] = self.variable[-1] // self.variable[-2]

    # assign False
    def x10(self):
        self.variable[-1] = False

    # assign True
    def x11(self):
        self.variable[-1] = True

    # == (equal)
    def x12(self):
        self.variable[-1] = self.variable[-1] == self.variable[-2]

    # != (not equal)
    def x13(self):
        self.variable[-1] = self.variable[-1] != self.variable[-2]

    # > (greater than)
    def x14(self):
        self.variable[-1] = self.variable[-1] > self.variable[-2]

    # < (less than)
    def x15(self):
        self.variable[-1] = self.variable[-1] < self.variable[-2]

    # >= (greater than or equal)
    def x16(self):
        self.variable[-1] = self.variable[-1] >= self.variable[-2]

    # <= (less than or equal)
    def x17(self):
        self.variable[-1] = self.variable[-1] <= self.variable[-2]

    # increase the pointer
    def x18(self):
        the_pointer = self.pointer[self.variable[-1] % len(self.pointer)]
        the_pointer += 1
        sign = the_pointer / abs(the_pointer)
        self.pointer[self.variable[-1] % len(self.pointer)] = sign * (the_pointer % len(self.variable))

    # decrease the pointer
    def x19(self):
        the_pointer = self.pointer[self.variable[-1] % len(self.pointer)]
        the_pointer -= 1
        sign = the_pointer / abs(the_pointer)
        self.pointer[self.variable[-1] % len(self.pointer)] = sign * (the_pointer % len(self.variable))

    # assign an empty list
    def x1A(self):
        self.variable[-1] = []

    # assign an empty dictionary
    def x1B(self):
        self.variable[-1] = {}

    # if
    def x1C(self):
        if self.variable[-1]:
            return True
        else:
            return False

    # if not
    def x1D(self):
        if not self.variable[-1]:
            return True
        else:
            return False

    # end
    def x1E(self):
        pass

    # while
    def x1F(self):
        if self.variable[-1]:
            return True
        else:
            return False

    # unless
    def x20(self):
        if not self.variable[-1]:
            return True
        else:
            return False

    # break
    def x21(self):
        pass

    # abs
    def x22(self):
        self.variable[-1] = abs(self.variable[-1])

    # ceil
    def x23(self):
        self.variable[-1] = math.ceil(self.variable[-1])

    # cmp
    def x24(self):
        self.variable[-1] = cmp(self.variable[-1], self.variable[-2])

    # exp
    def x25(self):
        self.variable[-1] = math.exp(self.variable[-1])

    # fabs
    def x26(self):
        self.variable[-1] = math.fabs(self.variable[-1])

    # floor
    def x27(self):
        self.variable[-1] = math.floor(self.variable[-1])

    # log
    def x28(self):
        self.variable[-1] = math.log(self.variable[-1])

    # log10
    def x29(self):
        self.variable[-1] = math.log10(self.variable[-1])

    # max
    def x2A(self):
        self.variable[-1] = max(self.variable[-1])

    # min
    def x2B(self):
        self.variable[-1] = min(self.variable[-1])

    # modf
    def x2C(self):
        self.variable[-1] = math.modf(self.variable[-1])

    # pow
    def x2D(self):
        self.variable[-1] = math.pow(self.variable[-1], self.variable[-2])

    # round
    def x2E(self):
        self.variable[-1] = round(self.variable[-1], self.variable[-2])

    # sqrt
    def x2F(self):
        self.variable[-1] = math.sqrt(self.variable[-1])

    # choice
    def x30(self):
        self.variable[-1] = random.choice(self.variable[-1])

    # randrange
    def x31(self):
        self.variable[-1] = random.randrange(self.variable[-1], self.variable[-2], self.variable[-3])

    # random
    def x32(self):
        self.variable[-1] = random.random()

    # seed
    def x33(self):
        random.seed(self.variable[-1])

    # shuffle
    def x34(self):
        random.shuffle(self.variable[-1])

    # uniform
    def x35(self):
        self.variable[-1] = random.uniform(self.variable[-1], self.variable[-2])

    # acos
    def x36(self):
        self.variable[-1] = math.acos(self.variable[-1])

    # asin
    def x37(self):
        self.variable[-1] = math.asin(self.variable[-1])

    # atan
    def x38(self):
        self.variable[-1] = math.atan(self.variable[-1])

    # atan2
    def x39(self):
        self.variable[-1] = math.atan2(self.variable[-1], self.variable[-2])

    # cos
    def x3A(self):
        self.variable[-1] = math.cos(self.variable[-1])

    # hypot
    def x3B(self):
        self.variable[-1] = math.hypot(self.variable[-1], self.variable[-2])

    # sin
    def x3C(self):
        self.variable[-1] = math.sin(self.variable[-1])

    # tan
    def x3D(self):
        self.variable[-1] = math.tan(self.variable[-1])

    # degrees
    def x3E(self):
        self.variable[-1] = math.degrees(self.variable[-1])

    # radians
    def x3F(self):
        self.variable[-1] = math.radians(self.variable[-1])

    # assign pi
    def x40(self):
        self.variable[-1] = math.pi

    # assign e
    def x41(self):
        self.variable[-1] = math.e

    # letter a
    def x42(self):
        self.variable[-1] = 'a'

    # letter b
    def x43(self):
        self.variable[-1] = 'b'

    # letter c
    def x44(self):
        self.variable[-1] = 'c'

    # letter d
    def x45(self):
        self.variable[-1] = 'd'

    # letter e
    def x46(self):
        self.variable[-1] = 'e'

    # letter f
    def x47(self):
        self.variable[-1] = 'f'

    # letter g
    def x48(self):
        self.variable[-1] = 'g'

    # letter h
    def x49(self):
        self.variable[-1] = 'h'

    # letter i
    def x4A(self):
        self.variable[-1] = 'i'

    # letter j
    def x4B(self):
        self.variable[-1] = 'j'

    # letter k
    def x4C(self):
        self.variable[-1] = 'k'

    # letter l
    def x4D(self):
        self.variable[-1] = 'l'

    # letter m
    def x4E(self):
        self.variable[-1] = 'm'

    # letter n
    def x4F(self):
        self.variable[-1] = 'n'

    # letter o
    def x50(self):
        self.variable[-1] = 'o'

    # letter p
    def x51(self):
        self.variable[-1] = 'p'

    # letter q
    def x52(self):
        self.variable[-1] = 'q'

    # letter r
    def x53(self):
        self.variable[-1] = 'r'

    # letter s
    def x54(self):
        self.variable[-1] = 's'

    # letter t
    def x55(self):
        self.variable[-1] = 't'

    # letter u
    def x56(self):
        self.variable[-1] = 'u'

    # letter v
    def x57(self):
        self.variable[-1] = 'v'

    # letter w
    def x58(self):
        self.variable[-1] = 'w'

    # letter x
    def x59(self):
        self.variable[-1] = 'x'

    # letter y
    def x5A(self):
        self.variable[-1] = 'y'

    # letter z
    def x5B(self):
        self.variable[-1] = 'z'

    # letter A
    def x5C(self):
        self.variable[-1] = 'A'

    # letter B
    def x5D(self):
        self.variable[-1] = 'B'

    # letter C
    def x5E(self):
        self.variable[-1] = 'C'

    # letter D
    def x5F(self):
        self.variable[-1] = 'D'

    # letter E
    def x60(self):
        self.variable[-1] = 'E'

    # letter F
    def x61(self):
        self.variable[-1] = 'F'

    # letter G
    def x62(self):
        self.variable[-1] = 'G'

    # letter H
    def x63(self):
        self.variable[-1] = 'H'

    # letter I
    def x64(self):
        self.variable[-1] = 'I'

    # letter J
    def x65(self):
        self.variable[-1] = 'J'

    # letter K
    def x66(self):
        self.variable[-1] = 'K'

    # letter L
    def x67(self):
        self.variable[-1] = 'L'

    # letter M
    def x68(self):
        self.variable[-1] = 'M'

    # letter N
    def x69(self):
        self.variable[-1] = 'N'

    # letter O
    def x6A(self):
        self.variable[-1] = 'O'

    # letter P
    def x6B(self):
        self.variable[-1] = 'P'

    # letter Q
    def x6C(self):
        self.variable[-1] = 'Q'

    # letter R
    def x6D(self):
        self.variable[-1] = 'R'

    # letter S
    def x6E(self):
        self.variable[-1] = 'S'

    # letter T
    def x6F(self):
        self.variable[-1] = 'T'

    # letter U
    def x71(self):
        self.variable[-1] = 'U'

    # letter V
    def x72(self):
        self.variable[-1] = 'V'

    # letter W
    def x73(self):
        self.variable[-1] = 'W'

    # letter X
    def x74(self):
        self.variable[-1] = 'X'

    # letter Y
    def x75(self):
        self.variable[-1] = 'Y'

    # letter Z
    def x76(self):
        self.variable[-1] = 'Z'

    # character 0
    def x77(self):
        self.variable[-1] = '0'

    # character 1
    def x78(self):
        self.variable[-1] = '1'

    # character 2
    def x79(self):
        self.variable[-1] = '2'

    # character 3
    def x7A(self):
        self.variable[-1] = '3'

    # character 4
    def x7B(self):
        self.variable[-1] = '4'

    # character 5
    def x7C(self):
        self.variable[-1] = '5'

    # character 6
    def x7D(self):
        self.variable[-1] = '6'

    # character 7
    def x7E(self):
        self.variable[-1] = '7'

    # character 8
    def x7F(self):
        self.variable[-1] = '8'

    # character 9
    def x80(self):
        self.variable[-1] = '9'


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
