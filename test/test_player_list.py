import unittest
from app.player_node import PlayerNode
from app.player import Player
from app.player_list import PlayerList

class TestPlayerList(unittest.TestCase):

    def setUp(self) -> None:
        self.player = Player("1702", "Isabel")
        self.player_2 = Player("1803", "Valeria")
        self.player_node = PlayerNode(self.player)
        self.player_list = PlayerList()

    def test_checking_empty_list_when_created(self):
        self.assertEqual(self.player_list.is_empty(), True)

    def test_that_updates_the_head_of_the_list(self):
        self.player_list.append(self.player)
        self.assertEqual(self.player_list.is_empty(), False)

    def test_that_checks_the_first_player_added_is_the_head(self):
        self.player_list.append(self.player)
        self.assertEqual(self.player_list.get_head(), self.player)

    def test_that_checks_the_tail_is_still_the_first_player_added(self):
        self.player_list.append(self.player)
        self.player_list.append(self.player_2)
        self.assertEqual(self.player_list.get_head(), self.player)
