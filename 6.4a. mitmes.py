
# Väiksematel üritustel on külaliste ühekaupa tervitamine lihtne. Suurematel üritustel võib ühekaupa tervitamine olla juba kurnavam tegevus.
#
# Esmalt koostada funktsioon tervitus, mis
#
# võtab argumendiks tervituse järjekorranumbri arvuna, mis näitab mitmes tervitus on käsil;
# kuvab väljakutsel ekraanile täpselt sellisel kujul tervituse ja vastuse koos tervituse järjekorranumbriga (n tähistab tervituse järjekorranumbrit):
# Võõrustaja: "Tere!"
# Täna n. kord tervitada, mõtiskleb võõrustaja.
# Külaline: "Tere, suur tänu kutse eest!"
#
# Teiseks koostada programm, mis
#
# küsib kasutajalt külaliste arvu;
# rakendab tsükli abil vastav arv kordi funktsiooni tervitus, kus igal tsükli sammul tuleb funktsioon välja kutsuda ühe võrra suurema argumendiga kui eelmisel korral.
# Funktsiooni kirjelduses tsüklit pole. Küll aga funktsiooni ennast rakendatakse tsükli kehas.
#
# https://courses.cs.ut.ee/2017/eprogalused/spring/Main/Kontroll-funktsioon2

def tervitus(mitmes):
    print('Võõrustaja: "Tere!"')
    print('Täna ' + str(mitmes) + '. kord tervitada, mõtiskleb võõrustaja.')
    print('Külaline: "Tere, suur tänu kutse eest!"')
    return


i = int(input('Sisetage külaliste arv: '))
mitmes = 1

while mitmes <= i:
    tervitus(mitmes)
    mitmes = mitmes + 1
