# Kuupäevade esitamisel tekib enim probleeme, kui kuupäev kirjutatakse kujul „05.06.2005“ – sellisel puhul pole võimalik aru saada, kas on mõeldud 5. juunit või hoopis 6. maid. Eestis ja enamikes teistes riikides kirjutatakse kuupäev reeglina formaadis DD.MM.YYYY, kuid Ameerika Ühendriikides on levinum järjekord MM.DD.YYYY. (Huvi korral vt https://en.wikipedia.org/wiki/Date_format_by_country.) Segaduse vältimiseks tuleks kuu nimi välja kirjutada.
#
# Esmalt kirjutada funktsioon kuu_nimi, mis
#
# võtab argumendiks kuu järjekorranumbri;
# tagastab vastava kuu nime (väikeste tähtedega).
# Vihje: Seda funktsiooni saab kirjutada, kasutades vastuse andmisel if-lauseid, aga optimaalne lahendus oleks kasutada järjendit (siis ühtegi if-lauset vaja ei ole).
#
# Teiseks luua funktsioon kuupäev_sõnena, mis
#
# võtab argumendiks ühe sõnena esitatud kuupäeva formaadis “DD.MM.YYYY” (nt '24.02.1918');
# tagastab selle sama kuupäeva kujul <päev>. <kuu_nimi> <aasta>. a (nt '24. veebruar 1918. a'), kusjuures kuupäev_sõnena peab ühe toimingu delegeerima funktsioonile kuu_nimi. Abiks võib ka olla funktsioon split.
# Kolmandaks kirjutada programm, mis
#
# küsib kasutajalt kuupäeva kujul “DD.MM.YYYY”;
# väljastab ekraanile vastava kuupäeva sõnena kujul<päev>. <kuu_nimi> <aasta>. a.
#
# https://courses.cs.ut.ee/2017/eprogalused/spring/Main/Kontroll-funktsioon2

def kuu_nimi(kuu_number):
    kuu_nimed = ["jaanuar",
                 "veebruar",
                 "märts",
                 "aprill",
                 "mai",
                 "juuni",
                 "juuli",
                 "august",
                 "september",
                 "oktoober",
                 "november",
                 "detsember"]

    return kuu_nimed[kuu_number - 1]


def kuupäev_sõnena(kuupaev):
    kuupaev_elemendid = kuupaev.split(".")
    return kuupaev_elemendid[0] + ". " + kuu_nimi(int(kuupaev_elemendid[1])) + " " + kuupaev_elemendid[2] + ". a"


kuupäev = input("Sisesta kuupäev kujul DD.MM.YYYY: ")

print(kuupäev_sõnena(kuupäev))
