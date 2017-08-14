from random import randint

program = ""

for i in range(10000):
    dec = randint(0, 33)
    hexa = hex(dec).split('x')[-1].upper()
    if len(hexa) == 1:
        hexa = '0' + hexa
    program += hexa

with open("000000.code","w+") as f:
    f.write(program)
