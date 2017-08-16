from random import randint

program = "000000000"

for i in range(randint(1,100000)):
    dec = randint(0, 331)
    hexa = hex(dec).split('x')[-1].upper()
    if len(hexa) == 2:
        hexa = '0' + hexa
    if len(hexa) == 1:
        hexa = '00' + hexa
    program += hexa

with open("000000.code","w+") as f:
    f.write(program)
