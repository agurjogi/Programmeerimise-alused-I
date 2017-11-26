
# Esmalt koostada funktsioon banner, mis
#
# võtab argumendiks reklaamlause, mida soovitakse kuvada;
# tagastab reklaamlause, kus kõik tähed on suured tähed.
#
# Teiseks koostada programm, mis
#
# küsib kasutajalt, mitu korda soovitakse reklaamlauset kuvada;
# küsib kasutajalt, millist reklaamlauset soovib kasutada;
# rakendab tsükli abil kasutaja sisestatud arv kordi funktsiooni banner, kus igal tsükli sammul tuleb funktsioon välja kutsuda argumendiga, milleks on kasutaja sisestatud reklaamlause;
# väljastab loodud tsükli abil reklaamlause kasutaja sisestatud arv kordi.
# Funktsiooni kirjelduses ei ole tsüklit, vaid funktsiooni kasutatakse tsükli kehas.
#
# NB! Funktsiooni nimi peab olema täpselt see, mis on ülesandes ette antud.
#
# https://courses.cs.ut.ee/2017/eprogalused/spring/Main/Kontroll-funktsioon



def banner(sisu):
    a = sisu.upper()
    sisu = a

    return (sisu)


mitu = int(input("Mitu korda soovite reklaamlauset kuvada: "))
sisu = input('Sisestage reklaamlause: ')

while mitu > 0:
    banner(sisu)
    print(sisu.upper())
    mitu = mitu - 1
