from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.korin_hinta = 0
        self.tavaroiden_maara = 0
        self.kori = []

    def tavaroita_korissa(self):
        return self.tavaroiden_maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return self.korin_hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos = Ostos(lisattava)
        for tuotteet in self.kori:
            if tuotteet.tuotteen_nimi() == lisattava.nimi():
                tuotteet.muuta_lukumaaraa(1)
                self.tavaroiden_maara += 1
                self.korin_hinta += lisattava.hinta()
                return
        self.kori.append(ostos)
        self.tavaroiden_maara += 1
        self.korin_hinta += lisattava.hinta()

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for tuotteet in self.kori:
            if tuotteet.tuotteen_nimi() == poistettava.nimi():
                tuotteet.muuta_lukumaaraa(-1)
                self.tavaroiden_maara -= 1
                self.korin_hinta -= poistettava.hinta()
                if tuotteet.lukumaara() == 0:
                    self.kori.remove(tuotteet)
                return

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
