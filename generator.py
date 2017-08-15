from random import randint

program = ""

for i in range(randint(1,10000)):
    dec = randint(0, 259)
    hexa = hex(dec).split('x')[-1].upper()
    if len(hexa) == 1:
        hexa = '0' + hexa
    program += hexa

with open("000000.code","w+") as f:
    f.write(program)
