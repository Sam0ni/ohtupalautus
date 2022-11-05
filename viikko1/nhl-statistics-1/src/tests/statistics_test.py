import unittest
from statistics import Statistics
from statistics import sort_by_points
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_sort_by_points(self):
        self.assertEqual(sort_by_points(Player("Kurri",   "EDM", 37, 53)),90)

    def test_search(self):
        self.assertEqual(self.statistics.search("Kurri").name, "Kurri")

    def test_search_ei_listassa(self):
        self.assertEqual(self.statistics.search("Litmanen"), None)

    def test_team(self):
        lista = self.statistics.team("EDM")
        self.assertEqual(len(lista), 3)

    def test_top(self):
        lista = self.statistics.top(2)
        self.assertEqual(lista[0].name, "Gretzky")
        self.assertEqual(lista[1].name, "Lemieux")