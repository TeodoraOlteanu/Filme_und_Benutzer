from Benutzer import benutzer, read_ben, write_ben
from Filme import filme, wertung, schauspieler, preis
from filmefkt import filmlist

def Menu():
    return(
        """
        1. Preis einer Bestellung
        2. Anzeigen alle Benutzern
        3. Anzeigen Ratings groesser als ein Wert
        4. Anzeigen Filme mit bestimmten Schauspielern
        5. Einfugen Benutzer
        6. Remove Benutzer
        7. Aktualisierung Nachname eines Benutzers
        8. Einfugen Film
        9. Aktualisierung des Preises eines Films
        10. Anzeigen Liste von Filme
        """
    )


def main():
    x = filmlist()
    filmliste = x.read_film()

    benutzerliste = read_ben()
    while True:
        print(Menu())
        a = int(input("Select option : "))
        if a == 1:
            nn = input("Geben Sie den Nachnamen des Benutzers ein: ")
            vn = input("Geben Sie den Vornamen des Benutzers ein: ")
            print("Der Preis der Bestellung ist: ", preis(nn, vn, benutzerliste, filmliste))
        elif a == 2:
            "in user2 schreibt man den benutzer, dessen Preis der Bestellung wissen will "
            for i in range(len(benutzerliste)):
                benutzerliste[i].anzeigenbenutzer()
        elif a == 3:
            w = int(input("Geben Sie den Wert ein: "))
            wertung(w, filmliste)
        elif a == 4:
            sch = input("Geben Sie den Schauspieler Film des Films ein: ")
            schauspieler(sch, filmliste)
        elif a == 5:
            nn = input("Geben Sie den Nachnamen des Benutzers ein: ")
            vn = input("Geben Sie den Vornamen des Benutzers ein: ")
            f1 = input("Geben Sie den ersten Film des Benutzers ein: ")
            f2 = input("Geben Sie den zweiten Film des Benutzers ein: ")
            b1 = benutzer(nn,vn,f1,f2)
            b1.insertbe(benutzerliste)
            write_ben(benutzerliste)
        elif a == 6:
            nn = input("Geben Sie den Nachnamen des Benutzers ein: ")
            vn = input("Geben Sie den Vornamen des Benutzers ein: ")
            b1 = benutzer(nn, vn, '', '')
            b1.loschen(benutzerliste)
            write_ben(benutzerliste)
        elif a == 7:
            nn = input("Geben Sie den Nachnamen des Benutzers ein: ")
            vn = input("Geben Sie den Vornamen des Benutzers ein: ")
            new = input("geben Sie den neuen Nachnamen des Benutzers ein: ")
            b1 = benutzer(nn, vn, '', '')
            b1.aktualisierenNachname(new, benutzerliste)
            write_ben(benutzerliste)
        elif a == 8:
            n = input("Geben Sie den Namen des Films ein: ")
            j = input("Geben Sie den Erscheinungsjahr des Films ein: ")
            w = input("Geben Sie die Wertung des Film des Films ein: ")
            sch = input("Geben Sie den Schauspieler Film des Films ein: ")
            pr = input("Geben Sie den Preis Film des Films ein: ")
            f1 = filme(n, j, w, sch, pr)
            f1.insertfilm(filmliste)
            filmliste = x.write_film()
        elif a == 9:
            n = input("Geben Sie den Namen des Films ein: ")
            new = input("Geben Sie den neuen Preis des Films ein: ")
            f1 = filme(n,'', '', '', '')
            f1.aktualisierenPreis(new, filmliste)
            filmliste= x.write_film()
        elif a == 10:
            for i in range(len(filmliste)):
                filmliste[i].anzeigenfilm()


main()


