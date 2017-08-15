import sys
import math
import random

class Program:

    def __init__(self, filename):
        self.variable = []
        self.power_of_ten = 0

        with open(filename) as f:
            program = ''.join(line.strip() for line in f)
            #print program
            program = [program[i:i + 3] for i in range(0, len(program), 3)]
            program = self.parse(program)
            #print program
            self.execute(program)

    # create a new variable
    def x000(self):
        self.variable.append(None)

    # print all variables
    def x001(self):
        print self.variable

    # assign an integer value
    def x002(self):
        self.variable[-1] = 0

    # assign a float value
    def x003(self):
        self.variable[-1] = 0.0

    # assign a string value
    def x004(self):
        self.variable[-1] = ""

    # + 1
    def x005(self):
        self.variable[-1] = self.variable[-1] + 1 * (10 ** self.power_of_ten)

    # - 1
    def x006(self):
        self.variable[-1] = self.variable[-1] - 1 * (10 ** self.power_of_ten)

    # power of ten + 1
    def x007(self):
        self.power_of_ten = self.power_of_ten + 1

    # power of ten - 1
    def x008(self):
        self.power_of_ten = self.power_of_ten - 1

    # addition
    def x009(self):
        self.variable[-1] = self.variable[-1] + self.variable[-2]

    # subtraction
    def x00A(self):
        self.variable[-1] = self.variable[-1] - self.variable[-2]

    # multiplication
    def x00B(self):
        self.variable[-1] = self.variable[-1] * self.variable[-2]

    # division
    def x00C(self):
        self.variable[-1] = self.variable[-1] / self.variable[-2]

    # modulus
    def x00D(self):
        self.variable[-1] = self.variable[-1] % self.variable[-2]

    # exponent
    def x00E(self):
        self.variable[-1] = self.variable[-1] ** self.variable[-2]

    # floor division
    def x00F(self):
        self.variable[-1] = self.variable[-1] // self.variable[-2]

    # assign False
    def x010(self):
        self.variable[-1] = False

    # assign True
    def x011(self):
        self.variable[-1] = True

    # == (equal)
    def x012(self):
        self.variable[-1] = self.variable[-1] == self.variable[-2]

    # != (not equal)
    def x013(self):
        self.variable[-1] = self.variable[-1] != self.variable[-2]

    # > (greater than)
    def x014(self):
        self.variable[-1] = self.variable[-1] > self.variable[-2]

    # < (less than)
    def x015(self):
        self.variable[-1] = self.variable[-1] < self.variable[-2]

    # >= (greater than or equal)
    def x016(self):
        self.variable[-1] = self.variable[-1] >= self.variable[-2]

    # <= (less than or equal)
    def x017(self):
        self.variable[-1] = self.variable[-1] <= self.variable[-2]

    # shift variables left
    def x018(self):
        self.variable = self.variable[1:] + [self.variable[0]]

    # shift variables right
    def x019(self):
        self.variable = [self.variable[-1]] + self.variable[:-1]

    # assign an empty list
    def x01A(self):
        self.variable[-1] = []

    # assign an empty dictionary
    def x01B(self):
        self.variable[-1] = {}

    # if
    def x01C(self):
        if self.variable[-1]:
            return True
        else:
            return False

    # if not
    def x01D(self):
        if not self.variable[-1]:
            return True
        else:
            return False

    # end
    def x01E(self):
        pass

    # while
    def x01F(self):
        if self.variable[-1]:
            return True
        else:
            return False

    # unless
    def x020(self):
        if not self.variable[-1]:
            return True
        else:
            return False

    # break
    def x021(self):
        pass

    # abs
    def x022(self):
        self.variable[-1] = abs(self.variable[-1])

    # ceil
    def x023(self):
        self.variable[-1] = math.ceil(self.variable[-1])

    # cmp
    def x024(self):
        self.variable[-1] = cmp(self.variable[-1], self.variable[-2])

    # exp
    def x025(self):
        self.variable[-1] = math.exp(self.variable[-1])

    # fabs
    def x026(self):
        self.variable[-1] = math.fabs(self.variable[-1])

    # floor
    def x027(self):
        self.variable[-1] = math.floor(self.variable[-1])

    # log
    def x028(self):
        self.variable[-1] = math.log(self.variable[-1])

    # log10
    def x029(self):
        self.variable[-1] = math.log10(self.variable[-1])

    # max
    def x02A(self):
        self.variable[-1] = max(self.variable[-1])

    # min
    def x02B(self):
        self.variable[-1] = min(self.variable[-1])

    # modf
    def x02C(self):
        self.variable[-1] = math.modf(self.variable[-1])

    # pow
    def x02D(self):
        self.variable[-1] = math.pow(self.variable[-1], self.variable[-2])

    # round
    def x02E(self):
        self.variable[-1] = round(self.variable[-1], self.variable[-2])

    # sqrt
    def x02F(self):
        self.variable[-1] = math.sqrt(self.variable[-1])

    # choice
    def x030(self):
        self.variable[-1] = random.choice(self.variable[-1])

    # randrange
    def x031(self):
        self.variable[-1] = random.randrange(self.variable[-1], self.variable[-2], self.variable[-3])

    # random
    def x032(self):
        self.variable[-1] = random.random()

    # seed
    def x033(self):
        random.seed(self.variable[-1])

    # shuffle
    def x034(self):
        random.shuffle(self.variable[-1])

    # uniform
    def x035(self):
        self.variable[-1] = random.uniform(self.variable[-1], self.variable[-2])

    # acos
    def x036(self):
        self.variable[-1] = math.acos(self.variable[-1])

    # asin
    def x037(self):
        self.variable[-1] = math.asin(self.variable[-1])

    # atan
    def x038(self):
        self.variable[-1] = math.atan(self.variable[-1])

    # atan2
    def x039(self):
        self.variable[-1] = math.atan2(self.variable[-1], self.variable[-2])

    # cos
    def x03A(self):
        self.variable[-1] = math.cos(self.variable[-1])

    # hypot
    def x03B(self):
        self.variable[-1] = math.hypot(self.variable[-1], self.variable[-2])

    # sin
    def x03C(self):
        self.variable[-1] = math.sin(self.variable[-1])

    # tan
    def x03D(self):
        self.variable[-1] = math.tan(self.variable[-1])

    # degrees
    def x03E(self):
        self.variable[-1] = math.degrees(self.variable[-1])

    # radians
    def x03F(self):
        self.variable[-1] = math.radians(self.variable[-1])

    # assign pi
    def x040(self):
        self.variable[-1] = math.pi

    # assign e
    def x041(self):
        self.variable[-1] = math.e

    # letter a
    def x042(self):
        self.variable[-1] = 'a'

    # letter b
    def x043(self):
        self.variable[-1] = 'b'

    # letter c
    def x044(self):
        self.variable[-1] = 'c'

    # letter d
    def x045(self):
        self.variable[-1] = 'd'

    # letter e
    def x046(self):
        self.variable[-1] = 'e'

    # letter f
    def x047(self):
        self.variable[-1] = 'f'

    # letter g
    def x048(self):
        self.variable[-1] = 'g'

    # letter h
    def x049(self):
        self.variable[-1] = 'h'

    # letter i
    def x04A(self):
        self.variable[-1] = 'i'

    # letter j
    def x04B(self):
        self.variable[-1] = 'j'

    # letter k
    def x04C(self):
        self.variable[-1] = 'k'

    # letter l
    def x04D(self):
        self.variable[-1] = 'l'

    # letter m
    def x04E(self):
        self.variable[-1] = 'm'

    # letter n
    def x04F(self):
        self.variable[-1] = 'n'

    # letter o
    def x050(self):
        self.variable[-1] = 'o'

    # letter p
    def x051(self):
        self.variable[-1] = 'p'

    # letter q
    def x052(self):
        self.variable[-1] = 'q'

    # letter r
    def x053(self):
        self.variable[-1] = 'r'

    # letter s
    def x054(self):
        self.variable[-1] = 's'

    # letter t
    def x055(self):
        self.variable[-1] = 't'

    # letter u
    def x056(self):
        self.variable[-1] = 'u'

    # letter v
    def x057(self):
        self.variable[-1] = 'v'

    # letter w
    def x058(self):
        self.variable[-1] = 'w'

    # letter x
    def x059(self):
        self.variable[-1] = 'x'

    # letter y
    def x05A(self):
        self.variable[-1] = 'y'

    # letter z
    def x05B(self):
        self.variable[-1] = 'z'

    # letter A
    def x05C(self):
        self.variable[-1] = 'A'

    # letter B
    def x05D(self):
        self.variable[-1] = 'B'

    # letter C
    def x05E(self):
        self.variable[-1] = 'C'

    # letter D
    def x05F(self):
        self.variable[-1] = 'D'

    # letter E
    def x060(self):
        self.variable[-1] = 'E'

    # letter F
    def x061(self):
        self.variable[-1] = 'F'

    # letter G
    def x062(self):
        self.variable[-1] = 'G'

    # letter H
    def x063(self):
        self.variable[-1] = 'H'

    # letter I
    def x064(self):
        self.variable[-1] = 'I'

    # letter J
    def x065(self):
        self.variable[-1] = 'J'

    # letter K
    def x066(self):
        self.variable[-1] = 'K'

    # letter L
    def x067(self):
        self.variable[-1] = 'L'

    # letter M
    def x068(self):
        self.variable[-1] = 'M'

    # letter N
    def x069(self):
        self.variable[-1] = 'N'

    # letter O
    def x06A(self):
        self.variable[-1] = 'O'

    # letter P
    def x06B(self):
        self.variable[-1] = 'P'

    # letter Q
    def x06C(self):
        self.variable[-1] = 'Q'

    # letter R
    def x06D(self):
        self.variable[-1] = 'R'

    # letter S
    def x06E(self):
        self.variable[-1] = 'S'

    # letter T
    def x06F(self):
        self.variable[-1] = 'T'

    # letter U
    def x071(self):
        self.variable[-1] = 'U'

    # letter V
    def x072(self):
        self.variable[-1] = 'V'

    # letter W
    def x073(self):
        self.variable[-1] = 'W'

    # letter X
    def x074(self):
        self.variable[-1] = 'X'

    # letter Y
    def x075(self):
        self.variable[-1] = 'Y'

    # letter Z
    def x076(self):
        self.variable[-1] = 'Z'

    # character 0
    def x077(self):
        self.variable[-1] = '0'

    # character 1
    def x078(self):
        self.variable[-1] = '1'

    # character 2
    def x079(self):
        self.variable[-1] = '2'

    # character 3
    def x07A(self):
        self.variable[-1] = '3'

    # character 4
    def x07B(self):
        self.variable[-1] = '4'

    # character 5
    def x07C(self):
        self.variable[-1] = '5'

    # character 6
    def x07D(self):
        self.variable[-1] = '6'

    # character 7
    def x07E(self):
        self.variable[-1] = '7'

    # character 8
    def x07F(self):
        self.variable[-1] = '8'

    # character 9
    def x080(self):
        self.variable[-1] = '9'

    # character "
    def x081(self):
        self.variable[-1] = '"'

    # character !
    def x082(self):
        self.variable[-1] = '!'

    # character '
    def x083(self):
        self.variable[-1] = "'"

    # character ^
    def x084(self):
        self.variable[-1] = '^'

    # character #
    def x085(self):
        self.variable[-1] = '#'

    # character +
    def x086(self):
        self.variable[-1] = '+'

    # character $
    def x087(self):
        self.variable[-1] = '$'

    # character %
    def x088(self):
        self.variable[-1] = '%'

    # character &
    def x089(self):
        self.variable[-1] = '&'

    # character /
    def x08A(self):
        self.variable[-1] = '/'

    # character {
    def x08B(self):
        self.variable[-1] = '{'

    # character (
    def x08C(self):
        self.variable[-1] = '('

    # character [
    def x08D(self):
        self.variable[-1] = '['

    # character )
    def x08E(self):
        self.variable[-1] = ')'

    # character ]
    def x08F(self):
        self.variable[-1] = ']'

    # character =
    def x090(self):
        self.variable[-1] = '='

    # character }
    def x091(self):
        self.variable[-1] = '}'

    # character ?
    def x092(self):
        self.variable[-1] = '?'

    # character *
    def x093(self):
        self.variable[-1] = '*'

    # character \
    def x094(self):
        self.variable[-1] = '\\'

    # character -
    def x095(self):
        self.variable[-1] = '-'

    # character _
    def x096(self):
        self.variable[-1] = '_'

    # character \t
    def x097(self):
        self.variable[-1] = '\t'

    # character \n
    def x098(self):
        self.variable[-1] = '\n'

    # character \r
    def x099(self):
        self.variable[-1] = '\r'

    # character @
    def x09A(self):
        self.variable[-1] = '@'

    # character ~
    def x09B(self):
        self.variable[-1] = '~'

    # character `
    def x09C(self):
        self.variable[-1] = '`'

    # character ,
    def x09D(self):
        self.variable[-1] = ','

    # character ;
    def x09E(self):
        self.variable[-1] = ';'

    # character <
    def x09F(self):
        self.variable[-1] = '<'

    # character >
    def x100(self):
        self.variable[-1] = '>'

    # character |
    def x101(self):
        self.variable[-1] = '|'

    # character .
    def x102(self):
        self.variable[-1] = '.'

    # character :
    def x103(self):
        self.variable[-1] = ':'

    # capitalize
    def x104(self):
        self.variable[-1] = self.variable[-1].capitalize()

    # string center
    def x105(self):
        self.variable[-1] = self.variable[-1].center(self.variable[-2], self.variable[-3])

    # string/list count
    def x106(self):
        self.variable[-1] = self.variable[-1].count(self.variable[-2])

    # string startswith
    def x107(self):
        self.variable[-1] = self.variable[-1].startswith(self.variable[-2])

    # string endswith
    def x108(self):
        self.variable[-1] = self.variable[-1].endswith(self.variable[-2])

    # string expandtabs
    def x109(self):
        self.variable[-1] = self.variable[-1].expandtabs(self.variable[-2])

    # string find
    def x10A(self):
        self.variable[-1] = self.variable[-1].find(self.variable[-2])

    # string/list index
    def x10B(self):
        self.variable[-1] = self.variable[-1].index(self.variable[-2])

    # string isalnum
    def x10C(self):
        self.variable[-1] = self.variable[-1].isalnum()

    # string isalpha
    def x10D(self):
        self.variable[-1] = self.variable[-1].isalpha()

    # string isdigit
    def x10E(self):
        self.variable[-1] = self.variable[-1].isdigit()

    # string islower
    def x10F(self):
        self.variable[-1] = self.variable[-1].islower()

    # string isnumeric
    def x110(self):
        self.variable[-1] = self.variable[-1].isnumeric()

    # string isspace
    def x111(self):
        self.variable[-1] = self.variable[-1].isspace()

    # string istitle
    def x112(self):
        self.variable[-1] = self.variable[-1].istitle()

    # string isupper
    def x113(self):
        self.variable[-1] = self.variable[-1].isupper()

    # string join
    def x114(self):
        self.variable[-1] = self.variable[-2].join(self.variable[-1])

    # length
    def x115(self):
        self.variable[-1] = len(self.variable[-1])

    # string left justify
    def x116(self):
        self.variable[-1] = self.variable[-1].ljust(self.variable[-2], self.variable[-3])

    # string lower
    def x117(self):
        self.variable[-1] = self.variable[-1].lower()

    # string upper
    def x118(self):
        self.variable[-1] = self.variable[-1].upper()

    # string left strip
    def x119(self):
        self.variable[-1] = self.variable[-1].lstrip(self.variable[-2])

    # string replace
    def x11A(self):
        self.variable[-1] = self.variable[-1].replace(self.variable[-2], self.variable[-3])

    # string right justify
    def x11B(self):
        self.variable[-1] = self.variable[-1].rjust(self.variable[-2], self.variable[-3])

    # string right strip
    def x11C(self):
        self.variable[-1] = self.variable[-1].rstrip(self.variable[-2])

    # string split
    def x11D(self):
        self.variable[-1] = self.variable[-1].split(self.variable[-2])

    # string splitlines
    def x11E(self):
        self.variable[-1] = self.variable[-1].splitlines()

    # string strip
    def x11F(self):
        self.variable[-1] = self.variable[-1].strip(self.variable[-2])

    # string swapcase
    def x120(self):
        self.variable[-1] = self.variable[-1].swapcase()

    # string title
    def x121(self):
        self.variable[-1] = self.variable[-1].title()

    # string zero fill
    def x122(self):
        self.variable[-1] = self.variable[-1].zfill(self.variable[-2])

    # string isdecimal
    def x123(self):
        self.variable[-1] = self.variable[-1].isdecimal()

    # list index
    def x124(self):
        self.variable[-1] = self.variable[-1][self.variable[-2]]

    # list slice
    def x125(self):
        self.variable[-1] = self.variable[-1][self.variable[-2]:self.variable[-3]]

    # list index assign
    def x126(self):
        self.variable[-1][self.variable[-2]] = self.variable[-3]

    # delete list element
    def x127(self):
        del self.variable[-1][self.variable[-2]]

    # list append
    def x128(self):
        self.variable[-1].append(self.variable[-2])

    # list extend
    def x129(self):
        self.variable[-1].extend(self.variable[-2])

    # list insert
    def x12A(self):
        self.variable[-1].insert(self.variable[-2])

    # list pop
    def x12B(self):
        self.variable[-1] = self.variable[-2].pop(self.variable[-3])

    # list remove
    def x12C(self):
        self.variable[-1].remove(self.variable[-2])

    # list reverse
    def x12D(self):
        self.variable[-1].reverse()

    # list sort
    def x12E(self):
        self.variable[-1].sort()

    # lift shift left
    def x12F(self):
        self.variable[-1] = self.variable[-1][1:] + [self.variable[-1][0]]

    # lift shift right
    def x130(self):
        self.variable[-1] = [self.variable[-1][-1]] + self.variable[-1][:-1]


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
