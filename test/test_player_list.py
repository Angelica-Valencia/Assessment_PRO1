import unittest
from app.player_node import PlayerNode
from app.player import Player
from app.player_list import PlayerList

class TestPlayerList(unittest.TestCase):

    def setUp(self) -> None:
        self.player = Player("1702", "Isabel")
        self.player_node = PlayerNode(self.player)
        self.player_list = PlayerList()

    def test_checking_empty_list_when_created(self):
        self.assertEqual(self.player_list.is_empty(), True)