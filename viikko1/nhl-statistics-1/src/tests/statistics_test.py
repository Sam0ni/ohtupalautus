import unittest
from statistics import Statistics
from statistics import sort_by_points
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

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

    def test_top_points(self):
        lista = self.statistics.top(2, SortBy.POINTS)
        self.assertEqual(lista[0].name, "Gretzky")
        self.assertEqual(lista[1].name, "Lemieux")

    def test_top_goals(self):
        lista = self.statistics.top(2, SortBy.GOALS)
        self.assertEqual(lista[1].name, "Yzerman")
        self.assertEqual(lista[0].name, "Lemieux")
    
    def test_top_assists(self):
        lista = self.statistics.top(2, SortBy.ASSISTS)
        self.assertEqual(lista[0].name, "Gretzky")
        self.assertEqual(lista[1].name, "Yzerman")

