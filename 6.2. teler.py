# Esiteks defineerida funktsioon nimega teleri_diagonaal, mis
#
# võtab argumendiks ühe arvu, mis tähistab kaugust diivanist teleri asukohani meetrites;
# arvutab selle põhjal teleri diagonaali tollides;
# tagastab teleri diagonaali tollides.
# Tagastatud teleri diagonaal peab olema ümardatud täisarvuni. Ümardamist peab sooritama funktsioon ise ja selleks tuleb kasutada funktsiooni round.
#
# Teiseks rakendada loodud funktsiooni programmis, kus
#
# kaugus diivanist telerini (meetrites) küsitakse kasutaja käest;
# väljastatakse teleri diagonaal (tollides) ekraanile.
# Oluline on, et teleri diagonaali arvutamise funktsioon ise ei küsiks kasutajalt midagi ja see funktsioon ise ka ei väljastaks tulemust ekraanile. Need tegevused peab tegema programmis väljaspool funktsiooni, funktsiooni töö on vaid arvutada.
#
# NB! Funktsiooni nimi peab olema täpselt see, mis on ülesandes ette antud.
#
# https://courses.cs.ut.ee/2017/eprogalused/spring/Main/Kontroll-funktsioon

def teleri_diagonaal(kaugus):
    diago = round(kaugus * 100 * 0.39 / 2.5)
    return diago


kaugus = float(input("Siseta kaugus: "))

print(teleri_diagonaal(kaugus))
