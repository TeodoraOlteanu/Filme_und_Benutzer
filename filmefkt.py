from Filme import filme

class filmlist:
    def __init__(self, filmliste = []):
        self.__filmliste = filmliste

    @property
    def filmliste(self):
        return self.__filmliste

    @filmliste.setter
    def filmliste(self, value):
        self.__filmliste = value

    def read_film(self):
        with open('filme.txt', 'r') as ff:
            for line in ff:
                l = line.split(',')
                self.filmliste.append(filme(l[0], l[1], l[2], l[3], l[4]))
            assert self.filmliste[5].preis == "10"
        return self.filmliste

    def write_film(self):

        with open("filme.txt", "w") as f:
            for i in range(len(self.filmliste)):
                f.write(self.filmliste[i].name + ',' + self.filmliste[i].jahr + ',' + self.filmliste[i].wertung + ',' +
                        self.filmliste[i].schauspieler + ',' + self.filmliste[i].preis + ',')
                f.write('\n')