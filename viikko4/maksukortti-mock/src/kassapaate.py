HINTA = 5


class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0

    def lataa(self, kortti, summa):
        if summa >= 0:
            kortti.lataa(summa)
        else:
            return f"Summa ei saa olla negatiivinen."

    def osta_lounas(self, kortti):
        if kortti.saldo >= HINTA:
            kortti.osta(HINTA)
            self.myytyja_lounaita = self.myytyja_lounaita + 1
        else:
            return f"Kortin saldo ei riitä."
