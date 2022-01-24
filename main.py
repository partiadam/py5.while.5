'''
5. Feladat
Írj egy programot while ciklussal, amely a felhasználótól páros számot kér be. Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig, amíg végül páros számot nem ad meg a felhasználó.
'''

x = 0
while x <= 0:
    beker =  int(input('Páros szám: '))
    if beker %2 == 0:
        break
        