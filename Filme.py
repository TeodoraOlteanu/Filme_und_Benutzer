

class filme:
    def __init__(self, name, jahr, wertung, schauspieler, preis):
        self.__name = name
        self.__jahr = jahr
        self.__wertung = wertung
        self.__schauspieler = schauspieler
        self.__preis = preis
    #GETTERS

    @property
    def name(self):
        return self.__name

    @property
    def jahr(self):
        return self.__jahr

    @property
    def wertung(self):
        return self.__wertung

    @property
    def schauspieler(self):
        return self.__schauspieler

    @property
    def preis(self):
        return self.__preis

    #SETTERS

    @name.setter
    def name(self, n):
        self.__name = n

    @jahr.setter
    def jahr(self, value):
        self.__jahr = value

    @wertung.setter
    def wertung(self, value):
        self.__wertung = value

    @schauspieler.setter
    def schauspieler(self, value):
        self.__schauspieler = value

    @preis.setter
    def preis(self, value):
        self.__preis = value

    def anzeigenfilm(self):
        """ Die Funktion schreibt ein Film an
            :param slef - das Objekt das angezeigt werden soll
        """
        print(self.__name, self.__jahr, self.__wertung, self.__schauspieler, self.__preis)

    def insertfilm(self, list):
        """
        Die Funktion fugt ein Film in der Liste von Benutzern ein
        :param slef: das Objekt das eingefugt werden soll
        :param list; die Liste wo das neue Objekt liegen wird
        """
        list.append(self)
    def aktualisierenPreis(self, new, list):

        """
            Die Funktion verandert den Preis des Films mit dem string new
            :param slef: das Objekt das eingefugt werden soll
            :param new; der neue Preis des Films-Objekt
            :param list; die Liste wo das neue Objekt liegen wird
        """
        for i in range(len(list)):
            if self.__name == list[i].name:
                list[i].preis = new


def wertung(wert, liste):
    new = []
    for i in range(len(liste)):
        if int(liste[i].wertung) > wert:
            new.append(liste[i])
    for i in range(len(new)):
        print(new[i].name, new[i].jahr, new[i].wertung, new[i].schauspieler, new[i].preis)

def schauspieler(akt, liste):
    new = []
    for i in range(len(liste)):
        if liste[i].schauspieler == akt:
            new.append(liste[i])

    for i in range(len(new)):
        new[i].anzeigenfilm()
    assert(new[0].name == 'The Hobbit')

def preis(nn,vn, listbe, listfi):
    sum = 0
    for i in range(len(listbe)):
        if nn == listbe[i].nachname and vn == listbe[i].vorname:

            for j in range(len(listfi)):
                if listbe[i].film1 == listfi[j].name:
                    sum = sum + int(listfi[j].preis)

                if listbe[i].film2 == listfi[j].name:
                    sum = sum + int(listfi[j].preis)
    return sum