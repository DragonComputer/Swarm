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

program += "000002FFD16700000005300015E14F16015612516016000001A16801F000161162FFF16316401E164165000000002FFD16700005300015E14F16015612516016000001A16801F00016116216316401E16416516800916000008600005800916000009600010200014C13711A16016014F160154150FFE"

with open("random.code","w+") as f:
    f.write(program)
