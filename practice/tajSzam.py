# 1. Olvasson be egy kilencjegyű TAJ-számot egy változóba!
# 673457015
inputText = input("Kérem, adjon meg egy TAJ számot: ")
tajSzamList = list(inputText)

# 2. A TAJ-szám kilencedik számjegyét,
# az ellenőrzőszámot írja a képernyőre, és tárolja el egy másik változóban!
tajUtolsoSzam = tajSzamList[8]
print("Az utolsó számjegy a:" +str(tajUtolsoSzam))

###
# A további feladatokban a TAJ-szám jegyeivel kell dolgoznia.
###
# 3. Az első nyolc számjegyet a helyzetének megfelelően,
#    ha páratlan pozíciójú, akkor hárommal,
#    ha páros, akkor héttel szorozza meg,
#    és a szorzatokat összegezze egy változóban!
#    Írja ki az így meghatározott összeg értékét!
tajSzamSzorzatSzum = 0

for index in range(0,8):
    if (index+1 % 2 == 0):
        tajSzamSzorzatSzum += int(tajSzamList[index]) * 7
    else:
        tajSzamSzorzatSzum += int(tajSzamList[index]) * 3
print("A számok szorzatának összege: "+ str(tajSzamSzorzatSzum))

# 4. Vizsgálja meg, hogy a szorzatok összege tízzel vett osztási maradéka
# azonos-e az ellenőrzőszámmal!
if (tajSzamSzorzatSzum % 10 == int(tajUtolsoSzam)):
    print ("A megadott TAJ szám utolsó számjegye: " + str(tajUtolsoSzam))
    print ("Az számított ellenőrzőszám értéke: " + str(tajSzamSzorzatSzum % 10))
    print ("Helyes a TAJ szám!")
else:
    print ("A megadott TAJ szám utolsó számjegye: " + str(tajUtolsoSzam))
    print ("Az számított ellenőrzőszám értéke: " + str(tajSzamSzorzatSzum % 10))
    print ("Hibás a TAJ szám!")
# Ha azonos, akkor a „Helyes a szám!”, különben „Hibás a szám!” szöveget írja a képernyőre!