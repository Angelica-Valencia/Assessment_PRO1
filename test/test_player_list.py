import unittest
from app.player_node import PlayerNode
from app.player import Player
from app.player_list import PlayerList


class TestPlayerList(unittest.TestCase):

    def setUp(self) -> None:

        self.players = [Player("1702", "Isabel"), Player("1803", "Valeria"), Player("7734", "Leonardo"), Player("0317", "Carlos")]
        self.player_nodes = []

        for player in self.players:
            self.player_nodes.append(PlayerNode(player))

        self.player_list = PlayerList()

    def test_checking_empty_list_when_created(self):
        self.assertEqual(self.player_list.is_empty(), True)

    def test_that_updates_the_head_of_the_list(self):
        self.player_list.add_at_the_head(self.players[0])
        self.assertEqual(self.player_list.is_empty(), False)

    def test_that_checks_the_first_player_added(self):
        self.player_list.add_at_the_head(self.players[0])
        self.assertEqual(self.player_list.get_head().get_key(), self.player_nodes[0].get_key())
        self.assertEqual(self.player_list.get_head().get_previous(), None)
        self.assertEqual(self.player_list.get_head().get_next(), None)
        self.assertEqual(self.player_list.get_head(), self.player_list.get_tail())

    def test_that_checks_player_added_when_list_is_not_empty(self):

        self.player_list.add_at_the_head(self.players[0])
        self.player_list.add_at_the_head(self.players[1])

        self.assertEqual(self.player_list.get_head().get_player(), self.player_nodes[1].get_player())
        self.assertEqual(self.player_list.get_head().get_previous(), None)
        self.assertEqual(self.player_list.get_head().get_next().get_player(), self.player_nodes[0].get_player())

    def test_that_checks_players_have_been_added_in_correct_order(self):

        for player in self.players:
            self.player_list.add_at_the_head(player)
            self.assertEqual(self.player_list.get_head().get_player(), player)

    def test_the_tail_when_adding_at_the_head(self):

        for player in self.players:

            self.player_list.add_at_the_head(player)

            self.assertEqual(self.player_list.get_tail().get_player(), self.player_nodes[0].get_player())
            self.assertEqual(self.player_list.get_tail().get_next(), None)

            if self.player_list.get_tail() == self.player_list.get_head():
                self.assertEqual(self.player_list.get_tail().get_previous(), None)
            else:
                self.assertEqual(self.player_list.get_tail().get_previous().get_player(), self.player_nodes[1].get_player())

    def test_the_head_when_adding_at_the_tail(self):

        for player in self.players:

            self.player_list.add_at_the_tail(player)

            self.assertEqual(self.player_list.get_head().get_player(), self.player_nodes[0].get_player())
            self.assertEqual(self.player_list.get_head().get_previous(), None)

            if self.player_list.get_tail() == self.player_list.get_head():
                self.assertEqual(self.player_list.get_head().get_next(), None)
            else:
                self.assertEqual(self.player_list.get_head().get_next().get_player(), self.player_nodes[1].get_player())

    def test_that_checks_all_the_nodes_from_the_head_to_tail(self):
        """
        head_order: [Player('Carlos', '0317') Player('Isabel', '1702'), Player('Valeria', '1803'), Player('Leonardo', '7734')]
        :return: None
        """
        head_order = [Player("0317", "Carlos"), Player("1702", "Isabel"), Player("1803", "Valeria"), Player("7734", "Leonardo")]
        order = [1, 2, 2, 1]
        count = 0

        for player in self.players:

            if order[count] == 1:
                self.player_list.add_at_the_head(player)
            else:
                self.player_list.add_at_the_tail(player)

            count += 1

        head = self.player_list.get_head()

        for player in head_order:
            self.assertEqual(str(head.get_player()), str(player))
            head = head.get_next()


    def test_that_checks_all_the_nodes_from_the_tail_to_head(self):
        """
        head_order: [ Player('Leonardo', '7734'), Player('Valeria', '1803'), Player('Isabel', '1702'), Player('Carlos', '0317')]
        :return: None
        """
        tail_order = [Player("7734", "Leonardo"), Player("1803", "Valeria"), Player("1702", "Isabel"), Player("0317", "Carlos")]
        order = [1, 2, 2, 1]
        count = 0

        for player in self.players:

            if order[count] == 1:
                self.player_list.add_at_the_head(player)
            else:
                self.player_list.add_at_the_tail(player)

            count += 1

        tail = self.player_list.get_tail()

        for player in tail_order:
            self.assertEqual(str(tail.get_player()), str(player))
            tail = tail.get_previous()


