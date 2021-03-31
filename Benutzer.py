class benutzer:
    def __init__(self, nachname, vorname, film1, film2):
        self.__nachname = nachname
        self.__vorname = vorname
        self.__film1 = film1
        self.__film2 = film2

    #GETTERS
    @property
    def vorname(self):
        return self.__vorname

    @property
    def nachname(self):
        return self.__nachname

    @property
    def film1(self):
        return self.__film1

    @property
    def film2(self):
        return self.__film2

    #SETTERS

    @nachname.setter
    def nachname(self, nn):
        self.__nachname = nn

    @vorname.setter
    def vorname(self, vn):
        self.__vorname = vn

    @film1.setter
    def film1(self, film):
        self.__film1 = film

    @film2.setter
    def film2(self, film):
        self.__film2 = film

    def anzeigenbenutzer(self):
        """ Die Funktion schreibt ein benutzer an
            :param slef - das Objekt das angezeigt werden soll
        """
        print(self.__nachname, self.__vorname, self.__film1, self.__film2)

    def insertbe(self, list):
        """
        Die Funktion fugt ein Benutzer in der Liste von Benutzern ein
        :param slef: das Objekt das eingefugt werden soll
        :param list; die Liste wo das neue Objekt liegen wird
        """
        list.append(self)

    def loschen(self, list):
        """
            Die Funktion loscht ein Benutzer von der Liste
            :param slef: das Objekt das eingefugt werden soll
            :param list; die Liste wo das neue Objekt liegen wird
        """
        for i in range(len(list)):
            if self.__nachname == list[i].nachname:
                try:
                    list.pop(i)
                except:
                    print("The Element does not exist")

    def aktualisierenNachname(self, new, list):
        """
            Die Funktion verandert den Nachnamen des Benutzers mit dem string new
            :param slef: das Objekt das eingefugt werden soll
            :param new; der neue Nachname des Bentzers-Objekt
            :param list; die Liste wo das nneue Objekt liegen wird
        """
        for i in range(len(list)):
            if self.__nachname == list[i].nachname:
                list[i].nachname = new
        #assert list[0].nachname == new

    '''def suchenbe(self ,benutzerliste ,nn, vn):
        for i in range(len(benutzerliste)):
            if nn == benutzerliste[i].nachname and vn == benutzerliste[i].vorname:
                return i'''


def write_ben(benutzerlist):

    with open("benutzer.txt", "w") as f:
        for i in range(len(benutzerlist)):
            f.write(benutzerlist[i].nachname + ',' + benutzerlist[i].vorname + ',' + benutzerlist[i].film1 + ',' + benutzerlist[i].film2 + ',')
            f.write('\n')

def read_ben():
    benutzerliste = []
    try:
        with open('benutzer.txt', 'r') as f:
            for line in f:
                l = line.split(',')
                benutzerliste.append(benutzer(l[0], l[1], l[2], l[3]))
    except:
        print("Something went wrong with the reading from the file")
    assert benutzerliste[0].nachname == 'Pipota'
    return benutzerliste