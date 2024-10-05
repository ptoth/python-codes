file = open("orszagok.csv", "r")
lines = []
data = []
countries = []
country = {
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
    lines.append(line.rstrip("\n"))
file.close()

for row in lines:
    data = row.split(";")
    
    country['id'] = data[0]
    country['orszag'] = data[1]
    country['fovaros'] = data[2]
    country['foldr_hely'] = data[3]
    country['terulet'] = data[4]
    country['allamforma'] = data[5]
    country['nepesseg'] = data[6]
    country['nep_fovaros'] = data[7]
    country['autojel'] = data[8]
    country['country'] = data[9]
    country['capital'] = data[10]
    country['penznem'] = data[11]
    country['penzjel'] = data[12]
    country['valtopenz'] = data[13]
    country['telefon'] = data[14]
    country['gdp'] = data[15]
    country['kat'] = data[16]
    # append a copy to the list
    # NOTE: cause is the immutability of 
    countries.append(country.copy())
    
    # cleanup
    for key in country:
        country[key] = ""

################################################################################
# Tasks
################################################################################
# 1. Mi MADAGASZKÁR fővárosa?
for country in countries:
    if country['orszag'] == "MADAGASZKÁR":
        print("Madagaszkár fővárosa: "+country['fovaros']+"\n")

# 2. Melyik ország fővárosa OUAGADOUGOU?
for country in countries:
    if country['fovaros'] == "OUAGADOUGOU":
        print("OUAGADOUGOU ennek a fővárosa: "+country['orszag']+"\n")

# 3. Melyik ország autójele a TT?
for country in countries:
    if country['autojel'] == "TT":
        print("A 'TT' ennek az országnak az autójele: "+country['orszag']+"\n")

# 4. Melyik ország pénzének jele az SGD?
for country in countries:
    if country['penzjel'] == "SGD":
        print("Az 'SGD' ennek az országnak az pénzjele: "+country['orszag']+"\n")

# 5. Melyik ország nemzetközi telefon-hívószáma a 61?
for country in countries:
    if country['telefon'] == "61":
        print("Az '61' ennek az országnak az hívószáma: "+country['orszag']+"\n")

# 6. Mekkora területű Monaco?
for country in countries:
    if country['orszag'] == "MONACO":
        print("Monaco területe: "+country['terulet']+"\n")

# 7. Hányan laknak Máltán?
for country in countries:
    if country['orszag'] == "MÁLTA":
        print("Málta lakossága: "+str(int(country['nepesseg'])*1000)+" fő.\n")

# 8. Mennyi Japán népsűrűsége?
for country in countries:
    if country['orszag'] == "JAPÁN":
        print("Japán népsűrűsége: "+str(round(int(country['nepesseg'])*1000 / int(country['terulet']),2)) +" fő/km2\n")

# 9. Hány lakosa van a Földnek?
fold_lakossag = 0
for country in countries:
    fold_lakossag += int(country['nepesseg'])
print ("A Föld lakossága: "+str(fold_lakossag*1000)+" fő.\n")

# 10. Mennyi az országok területe összesen?
osszes_orszag_terulet = 0
for country in countries:
    osszes_orszag_terulet += float(country['terulet'].replace(',','.'))
print ("Az összes orszag területe: "+str(round(osszes_orszag_terulet,2))+" km2.\n")

# 11. Mennyi az országok átlagos népessége?
print ("Az orszagok átlagos népéssége : "+str(round(fold_lakossag / len(countries),2))+" fő.\n")

# 12. Mennyi az országok átlagos területe?
print ("Az orszagok átlagos területe : "+str(round(osszes_orszag_terulet / len(countries),2))+" km2.\n")

# 13. Mennyi a Föld népsűrűsége?
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