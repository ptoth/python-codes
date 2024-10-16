"""Module to execute some basic programming tasks on dict and list type"""

sorok = []
data = []
orszagok = []
orszag = {
    "id": "",
    "orszag": "",
    "fovaros": "",
    "foldr_hely": "",
    "terulet": "",
    "allamforma": "",
    "nepesseg": "",
    "nep_fovaros": "",
    "autojel": "",
    "country": "",
    "capital": "",
    "penznem": "",
    "penzjel": "",
    "valtopenz": "",
    "telefon": "",
    "gdp": "",
    "kat": "",
}

with open("orszagok.csv", "r", encoding="utf8") as file:
    for sor in file:
        # string.rstrip : cut givet pattern only from the right side
        sorok.append(sor.rstrip("\n"))
file.close()

for row in sorok:
    data = row.split(";")

    orszag["id"] = data[0]
    orszag["orszag"] = data[1]
    orszag["fovaros"] = data[2]
    orszag["foldr_hely"] = data[3]
    orszag["terulet"] = data[4]
    orszag["allamforma"] = data[5]
    orszag["nepesseg"] = data[6]
    orszag["nep_fovaros"] = data[7]
    orszag["autojel"] = data[8]
    orszag["country"] = data[9]
    orszag["capital"] = data[10]
    orszag["penznem"] = data[11]
    orszag["penzjel"] = data[12]
    orszag["valtopenz"] = data[13]
    orszag["telefon"] = data[14]
    orszag["gdp"] = data[15]
    orszag["kat"] = data[16]
    # append a copy to the list
    # NOTE: cause is the immutability of variable
    orszagok.append(orszag.copy())

    # cleanup
    for key in orszag:
        orszag[key] = ""

################################################################################
# Tasks
################################################################################
# 1. Mi MADAGASZKÁR fővárosa?
for orszag in orszagok:
    if orszag["orszag"] == "MADAGASZKÁR":
        print("Madagaszkár fővárosa: " + orszag["fovaros"] + "\n")

# 2. Melyik ország fővárosa OUAGADOUGOU?
for orszag in orszagok:
    if orszag["fovaros"] == "OUAGADOUGOU":
        print("OUAGADOUGOU ennek a fővárosa: " + orszag["orszag"] + "\n")

# 3. Melyik ország autójele a TT?
for orszag in orszagok:
    if orszag["autojel"] == "TT":
        print("A 'TT' ennek az országnak az autójele: " + orszag["orszag"] + "\n")

# 4. Melyik ország pénzének jele az SGD?
for orszag in orszagok:
    if orszag["penzjel"] == "SGD":
        print("Az 'SGD' ennek az országnak az pénzjele: " + orszag["orszag"] + "\n")

# 5. Melyik ország nemzetközi telefon-hívószáma a 61?
for orszag in orszagok:
    if orszag["telefon"] == "61":
        print("Az '61' ennek az országnak az hívószáma: " + orszag["orszag"] + "\n")

# 6. Mekkora területű Monaco?
for orszag in orszagok:
    if orszag["orszag"] == "MONACO":
        print("Monaco területe: " + orszag["terulet"] + "\n")

# 7. Hányan laknak Máltán?
for orszag in orszagok:
    if orszag["orszag"] == "MÁLTA":
        print("Málta lakossága: " + str(int(orszag["nepesseg"]) * 1000) + " fő.\n")

# 8. Mennyi Japán népsűrűsége?
for orszag in orszagok:
    if orszag["orszag"] == "JAPÁN":
        print(
            "Japán népsűrűsége: "
            + str(round(int(orszag["nepesseg"]) * 1000 / int(orszag["terulet"]), 2))
            + " fő/km2\n"
        )

# 9. Hány lakosa van a Földnek?
fold_lakossag = 0
for orszag in orszagok:
    fold_lakossag += int(orszag["nepesseg"])
print("A Föld lakossága: " + str(fold_lakossag * 1000) + " fő.\n")

# 10. Mennyi az országok területe összesen?
osszes_orszag_terulet = 0
for orszag in orszagok:
    osszes_orszag_terulet += float(orszag["terulet"].replace(",", "."))
print("Az összes orszag területe: " + str(round(osszes_orszag_terulet, 2)) + " km2.\n")

# 11. Mennyi az országok átlagos népessége?
print(
    "Az orszagok átlagos népéssége : "
    + str(round(fold_lakossag / len(orszagok), 2))
    + " fő.\n"
)

# 12. Mennyi az országok átlagos területe?
print(
    "Az orszagok átlagos területe : "
    + str(round(osszes_orszag_terulet / len(orszagok), 2))
    + " km2.\n"
)

# 13. Mennyi a Föld népsűrűsége?
print(
    "A Föld népsűrűsége: "
    + str(round(fold_lakossag / osszes_orszag_terulet, 2))
    + " fő/km2 \n"
)

# 14. Hány 1.000.000 km2-nél nagyobb területű ország van?
nagyobb_mint_1m = 0
for orszag in orszagok:
    if float(orszag["terulet"].replace(",", ".")) > 10000000:
        nagyobb_mint_1m += 1
print(
    "Összesen "
    + str(nagyobb_mint_1m)
    + " db ország van, aminek területe nagyobb, mint 1M km2.\n"
)

# 15. Hány 100 km2-nél kisebb területű ország van?
kisebb_mint_100km2 = 0
for orszag in orszagok:
    if float(orszag["terulet"].replace(",", ".")) < 100:
        kisebb_mint_100km2 += 1
print(
    "Összesen "
    + str(kisebb_mint_100km2)
    + " db ország van, aminek területe kisebb, mint 100 km2.\n"
)

# 16. Hány 20.000 főnél kevesebb lakosú ország van?
kevesebb_mint_20k_lako = 0
for orszag in orszagok:
    if float(orszag["nepesseg"].replace(",", ".")) < 20:
        kevesebb_mint_20k_lako += 1
print(
    "Összesen "
    + str(kevesebb_mint_20k_lako)
    + " db ország van, aminek népességge kisebb, mint 20000 fő.\n"
)

# 17. Hány országra igaz, hogy területe kisebb 100 km2-nél,
# vagy pedig a lakossága kevesebb 20.000 főnél?
kisebb_mint_100km2_vagy_kevesebb_mint_20k_lako = 0
for orszag in orszagok:
    if (float(orszag["nepesseg"].replace(",", ".")) > 20) or (
        float(orszag["terulet"].replace(",", ".")) < 100
    ):
        kisebb_mint_100km2_vagy_kevesebb_mint_20k_lako += 1
print(
    "Összesen "
    + str(kisebb_mint_100km2_vagy_kevesebb_mint_20k_lako)
    + " db ország van, aminek területe kisebb 100 km2-nél, vagy pedig a lakossága kevesebb 20.000 főnél.\n"
)
# 18. Hány ország területe 50.000 és 150.000 km2 közötti?
orszag_50_es_150_kozott = 0
for orszag in orszagok:
    if (float(orszag["terulet"].replace(",", ".")) > 50) or (
        float(orszag["terulet"].replace(",", ".")) < 150
    ):
        orszag_50_es_150_kozott += 1
print(
    "Összesen "
    + str(orszag_50_es_150_kozott)
    + " db ország van, aminek területe nagyobb 50000 km2-nél, és kisebb 1500000 km2-nél.\n"
)

# 19. Hány ország lakossága 8 és 12 millió közötti?
lakossag_8_es_12_millio_kozott = 0
for orszag in orszagok:
    if int(orszag["nepesseg"]) < 12000:
        lakossag_8_es_12_millio_kozott += 1
print(
    "Összesen "
    + str(lakossag_8_es_12_millio_kozott)
    + " db ország van, aminek lakossága 8 és 12 millió közötti.\n"
)

# 20. Mely fővárosok népesebbek 20 millió főnél?
fovaros_nepesebb_20_millio = 0
varosok = []
for orszag in orszagok:
    if int(orszag["nep_fovaros"]) > 20000:
        fovaros_nepesebb_20_millio += 1
        varosok.append(orszag["orszag"])
print(
    "Összesen "
    + str(fovaros_nepesebb_20_millio)
    + " db ország van, aminek lakossága 20 millió feletti.\n"
    + "Ezek a következőek: "
)
print(str(varosok) + "\n")

# 21. Mely országok népsűrűsége nagyobb 500 fő/km2-nél?
nepsuruseg_nagyobb_mint_500 = 0
temp_orszagok = []

for orszag in orszagok:
    temp_nepsuruseg = round(
        int(orszag["nepesseg"]) * 1000 / float(orszag["terulet"].replace(",", ".")), 2
    )
    if temp_nepsuruseg > 500:
        nepsuruseg_nagyobb_mint_500 += 1
        temp_orszagok.append(orszag["orszag"])
print(
    "Összesen "
    + str(nepsuruseg_nagyobb_mint_500)
    + " db ország van, aminek népsűrűsége nagyobb, mint 500 fő/km2.\n"
    + "Ezek a következőek: "
)
print(str(temp_orszagok) + "\n")

# 22. Hány ország államformája köztársaság?
koztarsasag_db = 0
for orszag in orszagok:
    if orszag["allamforma"] == "köztársaság":
        koztarsasag_db += 1
print(
    "Összesen "
    + str(koztarsasag_db)
    + " db ország van, aminek államformája köztársaság\n"
)

# 23. Mely országok pénzneme a kelet-karib dollár?
kelet_karib_dollar = 0
temp_orszagok = []

for orszag in orszagok:
    if orszag["penznem"] == "kelet-karib dollár":
        kelet_karib_dollar += 1
        temp_orszagok.append(orszag["orszag"])
print(
    "Összesen "
    + str(kelet_karib_dollar)
    + " db ország van, aminek a pénzneme kelet-karib dollár.\n"
    + "Ezek a következőek: "
)
print(str(temp_orszagok) + "\n")

# 24. Hány ország nevében van benne az "ORSZÁG" szó?
orszag_a_nevben = 0
for orszag in orszagok:
    if "ORSZÁG" in orszag["orszag"]:
        orszag_a_nevben += 1
print(
    "Összesen "
    + str(orszag_a_nevben)
    + ' db ország van, aminek a nevében szerepel az "ORSZÁG".\n'
)

# 25. Mely országokban korona a hivatalos fizetőeszköz?
korona_penznem = 0
temp_orszagok = []

for orszag in orszagok:
    if "korona" in orszag["penznem"]:
        korona_penznem += 1
        temp_orszagok.append(orszag["orszag"])
print(
    "Összesen "
    + str(korona_penznem)
    + " db ország van, aminek a pénzneme korona.\n"
    + "Ezek a következőek: "
)
print(str(temp_orszagok) + "\n")

# 26. Mennyi Európa területe?
europa_terulete = 0
for orszag in orszagok:
    if "Európa" in orszag["foldr_hely"]:
        europa_terulete += float(orszag["terulet"].replace(",", "."))

print("Európa területe:  " + str(round(europa_terulete,2)) + " km2\n")

# 27. Mennyi Európa lakossága?
europa_lakossaga = 0
for orszag in orszagok:
    if "Európa" in orszag["foldr_hely"]:
        europa_lakossaga += int(orszag["nepesseg"]) * 1000

print("Európa népessége:  " + str(europa_lakossaga) + " fő\n")

# 28. Mennyi Európa népsűrűsége?
europa_nepsurusege = europa_lakossaga / europa_terulete
print("Európa népsűrűsége:  " + str(round(europa_nepsurusege,2)) + " fő\n")

# 29. Hány ország van Afrikában?
afrikai_orszagok = 0
for orszag in orszagok:
    if "Afrika" in orszag["foldr_hely"]:
        afrikai_orszagok += 1
print("Afrikai országok száma:  " + str(afrikai_orszagok) + " db\n")

# 30. Mennyi Afrika lakossága?
afrika_lakossaga = 0
for orszag in orszagok:
    if "Afrika" in orszag["foldr_hely"]:
        afrika_lakossaga += int(orszag["nepesseg"]) * 1000

print("Afrika népessége:  " + str(afrika_lakossaga) + " fő\n")

# 31. Mennyi Afrika népsűrűsége?
afrika_terulete = 0
for orszag in orszagok:
    if "Afrika" in orszag["foldr_hely"]:
        afrika_terulete += float(orszag["terulet"].replace(",", "."))

afrika_nepsurusege = afrika_lakossaga / afrika_terulete
print("Afrika népsűrűsége:  " + str(round(europa_nepsurusege,2)) + " fő/km2\n")

# 32. Melyek a szigetországok?
szigetorszagok = 0
for orszag in orszagok:
    if "szigetország" in orszag["foldr_hely"]:
        szigetorszagok += 1
print("Szigetországok száma:  " + str(szigetorszagok) + " db\n")

# 33. Mely országok államformája hercegség, vagy királyság?
hercegseg_vagy_kiralysag = 0
temp_orszagok = []

for orszag in orszagok:
    if ("hercegség" in orszag["allamforma"]) or ("királyság" in orszag["allamforma"]):
        hercegseg_vagy_kiralysag += 1
        temp_orszagok.append(orszag["orszag"])
print(
    "Összesen "
    + str(hercegseg_vagy_kiralysag)
    + " db ország van, aminek államformája hercegség, vagy királyság.\n"
    + "Ezek a következőek: "
)
print(str(temp_orszagok) + "\n")

# 34. Hány országnak nincs autójelzése?
nincs_autojelzes = 0
temp_orszagok = []

for orszag in orszagok:
    if orszag["autojel"] == "":
        nincs_autojelzes += 1
        temp_orszagok.append(orszag["orszag"])
print(
    "Összesen "
    + str(hercegseg_vagy_kiralysag)
    + " db ország van, aminek nincs autójelzése.\n"
    + "Ezek a következőek: "
)
print(str(temp_orszagok) + "\n")

# 35. Mennyi a váltószáma az aprópénznek azokban az országokban, ahol nem 100?
valtopenz_nem_100 = 0
temp_orszagok = []

for orszag in orszagok:
    if ("100 " in orszag["valtopenz"]):
        valtopenz_nem_100 += 1
        temp_orszagok.append(orszag["orszag"])
print(
    "Összesen "
    + str(valtopenz_nem_100)
    + " db ország van, ahol nem 100 az aprópénz váltószáma.\n"
    + "Ezek a következőek: "
)
print(str(temp_orszagok) + "\n")

# 36. Hány ország területe kisebb Magyarországénál?

# 37. Melyik a legnagyobb területű ország, és mennyi a területe?

# 38. Melyik a legkisebb területű ország, és mennyi a területe?

# 39. Melyik a legnépesebb ország, és hány lakosa van?

# 40. Melyik a legkisebb népességű ország, és hány lakosa van?

# 41. Melyik a legsűrűbben lakott ország, és mennyi a népsűrűsége?

# 42. Melyik a legritkábban lakott ország, és mennyi a népsűrűsége?

# 43. Melyik a legnagyobb afrikai ország és mekkora?

# 44. Melyik a legkisebb amerikai ország és hányan lakják?

# 45. Melyik az első három legsűrűbben lakott "országméretű" ország (tehát nem város- vagy törpeállam)?

# 46. Melyik a világ hat legnépesebb fővárosa?

# 47. Melyik tíz ország egy főre jutó GDP-je a legnagyobb?

# 48. Melyik tíz ország össz-GDP-je a legnagyobb?

# 49. Melyik országban a legszegényebbek az emberek?

# 50. Melyik a 40. legkisebb területű ország?

# 51. Melyik a 15. legkisebb népsűrűségű ország?

# 52. Melyik a 61. legnagyobb népsűrűségű ország?

# 53. Melyik három ország területe hasonlít leginkább Magyaroszág méretéhez?

# 54. Az emberek hányadrésze él Ázsiában?

# 55. A szárazföldek mekkora hányadát foglalja el Oroszország?

# 56. Az emberek hány százaléka fizet euroval?

# 57. Hányszorosa a leggazdagabb ország egy főre jutó GDP-je a legszegényebb ország egy főre jutó GDP-jének?

# 58. A világ össz-GDP-jének hány százalékát adja az USA?

# 59. A világ össz-GDP-jének hány százalékát adja az euroövezet?

# 60. Melyek azok az átlagnál gazdagabb országok, amelyek nem az európai vagy az amerikai kontinensen találhatóak?

# 61. Milyen államformák léteznek Európában?

# 62. Hányféle államforma létezik a világon?

# 63. Hányféle fizetőeszközt használnak Európában az eurón kívül?

# 64. Mely pénznemeket használják több országban is?

# 65. Mely országok államformája egyedi?
