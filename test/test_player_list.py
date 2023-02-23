import unittest
from app.player_node import PlayerNode
from app.player import Player
from app.player_list import PlayerList


class TestPlayerList(unittest.TestCase):

    def setUp(self) -> None:
        self.player = Player("1702", "Isabel")
        self.player_2 = Player("1803", "Valeria")
        self.player_3 = Player("7734", "Leonardo")

        self.player_node_1 = PlayerNode(self.player)
        self.player_node_2 = PlayerNode(self.player_2)
        self.player_node_3 = PlayerNode(self.player_3)

        self.player_list = PlayerList()

    def test_checking_empty_list_when_created(self):
        self.assertEqual(self.player_list.is_empty(), True)

    def test_that_updates_the_head_of_the_list(self):
        self.player_list.add_at_the_head(self.player)
        self.assertEqual(self.player_list.is_empty(), False)

    def test_that_checks_the_first_player_added(self):
        self.player_list.add_at_the_head(self.player)
        self.assertEqual(self.player_list.get_head().get_key(), self.player_node_1.get_key())
        self.assertEqual(self.player_list.get_head().get_previous(), None)
        self.assertEqual(self.player_list.get_head().get_next(), None)

    def test_that_checks_player_added_when_list_is_not_empty(self):
        self.player_list.add_at_the_head(self.player)
        self.player_list.add_at_the_head(self.player_2)
        self.assertEqual(self.player_list.get_head().get_key(), self.player_node_2.get_key())
        self.assertEqual(self.player_list.get_head().get_previous(), None)
        self.assertEqual(self.player_list.get_head().get_next().get_key(), self.player_node_1.get_key())

    def test_that_checks_players_have_been_added_in_correct_order(self):

        players = [self.player_node_3, self.player_node_2, self.player_node_1]

        self.player_list.add_at_the_head(self.player)
        self.player_list.add_at_the_head(self.player_2)
        self.player_list.add_at_the_head(self.player_3)

        node = self.player_list.get_head()

        for player in players:
            self.assertEqual(node.get_key(), player.get_key())
            node = node.get_next()

    def test_the_tail_when_adding_at_the_head(self):

        players_nodes = [self.player_node_1, self.player_node_2, self.player_node_3]
        players = [self.player, self.player_2, self.player_3]

        for player in players:

            self.player_list.add_at_the_head(player)

            self.assertEqual(self.player_list.get_tail().get_key(), players_nodes[0].get_key())
            self.assertEqual(self.player_list.get_tail().get_next(), None)

            if self.player_list.get_tail() == self.player_list.get_head():
                self.assertEqual(self.player_list.get_tail().get_previous(), None)
            else:
                self.assertEqual(self.player_list.get_tail().get_previous().uid, players_nodes[1].get_key())
