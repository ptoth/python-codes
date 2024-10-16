# 1,
# A mintának megfelelően kérjen be a felhasználótól egy legalább 5 jegyű egész
# számot! Az adatbekérés mindaddig folytatódjon, amíg a megadott szám
# számjegyeinek száma legalább 5 nem lesz!
inputNum = 0
while inputNum < 99999:
    inputStr = input("Adj meg egy egész számot: ")
    inputNum = int(inputStr)

# 2,
# Vizsgálja meg és a mintának megfelelően jelezze,
# hogy a megadott szám osztható-e öttel és tízzel egyidejűleg!
if (inputNum % 5 == 0 and inputNum % 10 == 0):
    print("A szám osztható öttel és tízzel is.")
elif inputNum % 5 == 0:
    print("A szám osztható öttel.")
else:
    print("A szám nem osztható sem öttel sem tízzel")

# 3, A minta szerint visszafelé olvasva jelenítse meg a megadott számot!
lista=list(str(inputNum))
print(lista[::-1])

# 4,
# Egy listába gyűjtse ki, és a mintának megfelelően emelkedő sorrendben jelenítse a
# páros számjegyeket!
eredmeny=[]
for szam in lista:
    if int(szam) % 2 == 0:
        eredmeny.append(szam)
eredmeny.sort()
print(eredmeny)

# 5,
# A minta szerint jelenítse meg az ismétlődő számjegyeket!
# Minden számjegy csak egyszer kerüljön kiírásra!
ismetlodo = []
for szamjegy in inputStr:
    if inputStr.count(szamjegy) > 1 and szamjegy not in ismetlodo:
        ismetlodo.append(szamjegy)
print(ismetlodo)
