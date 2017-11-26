# Euromüntide seerias on kuus erineva nimiväärtusega senti: 1 sent, 2 senti, 5 senti, 10 senti, 20 senti, 50 senti. Sendid väärtustega 1, 2 ja 5 on pronksikarva (vasega kaetud teras), sendid väärtustega 10, 20 ja 50 on kullakarva (vasesulam, mis sisaldab alumiiniumi, tsinki ja tina, nn Nordic Gold).
#
# Peres on kombeks, et pronksikarva mündid panna hoiupõrsasse.
#
# Müntide andmed on failis kirjas nii, et iga mündi väärtus on eraldi real. Näiteks nii:
#
# 1
# 20
# 20
# 5
# 50
# 2
# 2
# 1
#
# Esmalt koostada funktsioon pronksikarva_summa, mis
#
# võtab argumendiks täisarvude järjendi;
# tagastab selles järjendis olevate arvude 1, 2 ja 5 summa.
# Teiseks koostada programm, mis
#
# küsib kasutajalt selle faili nime, milles asuvad sentide väärtused;
# moodustab täisarvujärjendi vastavast failist loetud väärtustest;
# rakendab funktsiooni pronksikarva_summa, andes argumendiks koostatud täisarvujärjendi;
# väljastab ekraanile tulemuseks saadud kõikide pronksikarva sentide summa.
#
# https://courses.cs.ut.ee/2017/eprogalused/spring/Main/Kontroll-funktsioon2

def pronksikarva_summa(fail):
    järjend = []
    fail = open(failinimi, encoding="UTF-8")
    for rida in fail:
        if int(rida) <= 5:
            järjend += [int(rida)]
    fail.close()
    summa = sum(järjend)
    return summa


failinimi = input("Sisestage failinimi: ")
print(pronksikarva_summa(failinimi))
