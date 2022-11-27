KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("väärä kasvatuskoko")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.alkiot = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, alkio):
        if alkio in self.alkiot:
            return True
        else:
            return False

    def lisaa(self, alkio):

        if self.alkioiden_lkm == 0:
            self.alkiot[0] = alkio
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True

        elif not self.kuuluu(alkio):
            self.alkiot[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.alkiot) == 0:
                self.lisaa_tilaa_taulukkoon()

            return True

        else:
            return False

    def poista(self, alkio):
        if self.kuuluu(alkio):
            for indeksi in range(len(self.alkiot)):
                if self.alkiot[indeksi] == alkio:
                    self.alkiot.pop(indeksi)
                    self.alkiot.append(0)
                    self.alkioiden_lkm -= 1
                    return True
        else:
            return False

    def lisaa_tilaa_taulukkoon(self):
        for i in range(self.kasvatuskoko):
            self.alkiot.append(0)

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self.alkiot.copy()

        return taulu[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in a_taulu:
            joukko.lisaa(alkio)

        for alkio in b_taulu:
            joukko.lisaa(alkio)

        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in a_taulu:
            if alkio in b_taulu:
                joukko.lisaa(alkio)

        return joukko

    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in a_taulu:
            if alkio in b_taulu:
                continue
            else:
                joukko.lisaa(alkio)

        return joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            teksti = "{"
            for indeksi in range(self.alkioiden_lkm):
                teksti = teksti + str(self.alkiot[indeksi]) + ", "
            return teksti[:-2] + "}"
