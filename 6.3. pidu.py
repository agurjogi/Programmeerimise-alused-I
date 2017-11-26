# Juubelile on kutsutud hulk inimesi, kellest osa on teatanud, et nad tulevad ja ülejäänute kohta ei ole midagi teada. Peo eelarve koosneb kahest osast: söök ja ruumi rent. Söögi peale arvestatakse iga osaleja kohta 10 eurot. Ruumi rent maksab sõltumata osalejate arvust 55 eurot. Planeerimiseks on vaja programmi, mis arvutab
#
# maksimaalse eelarve (arvestades, et kõik kutsutud inimesed tulevad kohale) ja
# minimaalse eelarve (arvestades, et kohale tulevad ainult need, kes on juba seda teatanud).
# Esmalt koostada funktsioon eelarve, mis
#
# võtab argumendiks külaliste arvu tähistava täisarvu;
# arvutab selle põhjal eelarve kogusumma;
# tagastab eelarve kogusumma. Näiteks argumendiga 5 tagastab funktsioon arvu 105.
# Teiseks koostada programm, mis
#
# küsib kasutajalt kutsutud inimeste arvu;
# küsib kasutajalt inimeste arvu, kes on juba tulemisest teatanud;
# arvutab ja väljastab ekraanile maksimaalse eelarve, kasutades koostatud funktsiooni eelarve;
# arvutab ja väljastab ekraanile minimaalse eelarve, kasutades koostatud funktsiooni eelarve.
#
# https://courses.cs.ut.ee/2017/eprogalused/spring/Main/Kontroll-funktsioon

def eelarve(guests):
    total = guests * 10 + 55
    return total


guests = int(input("Mitu inimest on kutsustud? "))
yes = int(input("Mitu inimest tuleb? "))

# max = eelarve(guests)
print("Maksimaalne eelarve: " + str(eelarve(guests)))
print("Minimaalne eelarve: " + str(eelarve(yes)))
