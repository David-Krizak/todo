class Zadatak:
    def __init__(self, naziv, opis="", prioritet="Srednji"):
        self.naziv = naziv
        self.opis = opis
        self.prioritet = prioritet
        self.zavrsen = False

    def oznaci_zavrsen(self):
        self.zavrsen = True

    def vrati_na_nezavrseno(self):
        self.zavrsen = False

    def uredi(self, naziv, opis, prioritet):
        self.naziv = naziv
        self.opis = opis
        self.prioritet = prioritet
