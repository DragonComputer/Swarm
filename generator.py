from random import randint

program = "000000000"

for i in range(randint(1,10000)):
    dec = randint(0, 334)
    hexa = hex(dec).split('x')[-1].upper()
    if len(hexa) == 2:
        hexa = '0' + hexa
    if len(hexa) == 1:
        hexa = '00' + hexa
    program += hexa

program = "001"

with open("000000","w+") as f:
    f.write(program)
