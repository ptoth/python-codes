"""Module to execute some basic programming tasks on dict and list type"""

file = open("orszagok.csv", "r", encoding="UTF8")
sorok = []
data = []
orszagok = []
orszag = {
    "id":"",
    "orszag":"",
    "fovaros":"",
    "foldr_hely":"",
    "terulet":"",
    "allamforma":"",
    "nepesseg":"",
    "nep_fovaros":"",
    "autojel":"",
    "country":"",
    "capital":"",
    "penznem":"",
    "penzjel":"",
    "valtopenz":"",
    "telefon":"",
    "gdp":"",
    "kat":""
}

for line in file:
    # string.rstrip : cut givet pattern only from the right side
    sorok.append(line.rstrip("\n"))
file.close()

for row in lines:
    data = row.split(";")
    
    orszag['id'] = data[0]
    orszag['orszag'] = data[1]
    orszag['fovaros'] = data[2]
    orszag['foldr_hely'] = data[3]
    orszag['terulet'] = data[4]
    orszag['allamforma'] = data[5]
    orszag['nepesseg'] = data[6]
    orszag['nep_fovaros'] = data[7]
    orszag['autojel'] = data[8]
    orszag['country'] = data[9]
    orszag['capital'] = data[10]
    orszag['penznem'] = data[11]
    orszag['penzjel'] = data[12]
    orszag['valtopenz'] = data[13]
    orszag['telefon'] = data[14]
    orszag['gdp'] = data[15]
    orszag['kat'] = data[16]
    # append a copy to the list
    # NOTE: cause is the immutability of 
    orszagok.append(orszag.copy())
    
    # cleanup
    for key in orszag:
        orszag[key] = ""

################################################################################
# Tasks
################################################################################
# 1. Mi MADAGASZKÁR fővárosa?
for orszag in orszagok:
    if orszag['orszag'] == "MADAGASZKÁR":
        print("Madagaszkár fővárosa: "+orszag['fovaros']+"\n")

# 2. Melyik ország fővárosa OUAGADOUGOU?
for orszag in orszagok:
    if orszag['fovaros'] == "OUAGADOUGOU":
        print("OUAGADOUGOU ennek a fővárosa: "+orszag['orszag']+"\n")

# 3. Melyik ország autójele a TT?
for orszag in orszagok:
    if orszag['autojel'] == "TT":
        print("A 'TT' ennek az országnak az autójele: "+orszag['orszag']+"\n")

# 4. Melyik ország pénzének jele az SGD?
for orszag in orszagok:
    if orszag['penzjel'] == "SGD":
        print("Az 'SGD' ennek az országnak az pénzjele: "+orszag['orszag']+"\n")

# 5. Melyik ország nemzetközi telefon-hívószáma a 61?
for orszag in orszagok:
    if orszag['telefon'] == "61":
        print("Az '61' ennek az országnak az hívószáma: "+orszag['orszag']+"\n")

# 6. Mekkora területű Monaco?
for orszag in orszagok:
    if orszag['orszag'] == "MONACO":
        print("Monaco területe: "+orszag['terulet']+"\n")

# 7. Hányan laknak Máltán?
for orszag in orszagok:
    if orszag['orszag'] == "MÁLTA":
        print("Málta lakossága: "+str(int(orszag['nepesseg'])*1000)+" fő.\n")

# 8. Mennyi Japán népsűrűsége?
for orszag in orszagok:
    if orszag['orszag'] == "JAPÁN":
        print("Japán népsűrűsége: "+str(round(int(orszag['nepesseg'])*1000 / int(orszag['terulet']),2)) +" fő/km2\n")

# 9. Hány lakosa van a Földnek?
fold_lakossag = 0
for orszag in orszagok:
    fold_lakossag += int(orszag['nepesseg'])
print ("A Föld lakossága: "+str(fold_lakossag*1000)+" fő.\n")

# 10. Mennyi az országok területe összesen?
osszes_orszag_terulet = 0
for orszag in orszagok:
    osszes_orszag_terulet += float(orszag['terulet'].replace(',','.'))
print ("Az összes orszag területe: "+str(round(osszes_orszag_terulet,2))+" km2.\n")

# 11. Mennyi az országok átlagos népessége?
print ("Az orszagok átlagos népéssége : "+str(round(fold_lakossag / len(orszagok),2))+" fő.\n")

# 12. Mennyi az országok átlagos területe?
print ("Az orszagok átlagos területe : "+str(round(osszes_orszag_terulet / len(orszagok),2))+" km2.\n")

# 13. Mennyi a Föld népsűrűsége?
print ("A Föld népsűrűsége: "+ str(round(fold_lakossag / osszes_orszag_terulet,2)) +" \n")

# 14. Hány 1.000.000 km2-nél nagyobb területű ország van?

# 15. Hány 100 km2-nél kisebb területű ország van?
# 16. Hány 20.000 főnél kevesebb lakosú ország van?
# 17. Hány országra igaz, hogy területe kisebb 100 km2-nél, vagy pedig a lakossága kevesebb 20.000 főnél?
# 18. Hány ország területe 50.000 és 150.000 km2 közötti?
# 19. Hány ország lakossága 8 és 12 millió közötti?
# 20. Mely fővárosok népesebbek 20 millió főnél?
# 21. Mely országok népsűrűsége nagyobb 500 fő/km2-nél?
# 22. Hány ország államformája köztársaság?
# 23. Mely országok pénzneme a kelet-karib dollár?
# 24. Hány ország nevében van benne az "ORSZÁG" szó?
# 25. Mely országokban korona a hivatalos fizetőeszköz? 
# 26. Mennyi Európa területe?
# 27. Mennyi Európa lakossága?
# 28. Mennyi Európa népsűrűsége?
# 29. Hány ország van Afrikában?
# 30. Mennyi Afrika lakossága?
# 31. Mennyi Afrika népsűrűsége?
# 32. Melyek a szigetországok?
# 33. Mely országok államformája hercegség, vagy királyság? 34. Hány országnak nincs autójelzése?
# 35. Mennyi a váltószáma az aprópénznek azokban az országokban, ahol nem 100? 36. Hány ország területe kisebb Magyarországénál?
# 37. Melyik a legnagyobb területű ország, és mennyi a területe?
# 38. Melyik a legkisebb területű ország, és mennyi a területe?
# 39. Melyik a legnépesebb ország, és hány lakosa van?
# 40. Melyik a legkisebb népességű ország, és hány lakosa van?
# 41. Melyik a legsűrűbben lakott ország, és mennyi a népsűrűsége? 42. Melyik a legritkábban lakott ország, és mennyi a népsűrűsége? 43. Melyik a legnagyobb afrikai ország és mekkora?
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