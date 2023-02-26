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

    def test_that_checks_empty_list_when_created(self):
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

    def test_error_raised_when_deleting_in_an_empty_list(self):

        with self.assertRaises(IndexError):
            self.player_list.delete_from_tail()

        with self.assertRaises(IndexError):
            self.player_list.delete_from_head()

    def test_that_checks_remaining_players_deleted_from_tail(self):
        """
        Order when all the players have been added at the head:
        head_order: [Player('Carlos', '0317'), Player('Leonardo', '7734'), Player('Valeria', '1803'), Player('Isabel', '1702')]
        :return: None
        """

        count = 0
        remaining_players = 0

        for player in self.players:
            self.player_list.add_at_the_head(player)
            count += 1

        for lap in range(count):
            self.player_list.delete_from_tail()

            node = self.player_list.get_tail()

            while node:
                remaining_players += 1
                node = node.get_previous()

            self.assertEqual(count - lap - 1, remaining_players)
            remaining_players = 0

    def test_that_checks_remaining_players_deleted_from_head(self):
        """
        Order when all the players have been added at the head:
        head_order: [Player('Carlos', '0317'), Player('Leonardo', '7734'), Player('Valeria', '1803'), Player('Isabel', '1702')]
        :return: None
        """

        count = 0
        remaining_players = 0

        for player in self.players:
            self.player_list.add_at_the_head(player)
            count += 1

        for lap in range(count):
            self.player_list.delete_from_head()

            node = self.player_list.get_head()

            while node:
                remaining_players += 1
                node = node.get_next()

            self.assertEqual(count - lap - 1, remaining_players)
            remaining_players = 0

    def test_that_checks_the_last_remaining_node_deleting_from_head(self):
        """
        Order when all the players have been added at the head:
        head_order: [Player('Carlos', '0317'), Player('Leonardo', '7734'), Player('Valeria', '1803'), Player('Isabel', '1702')]
        :return: None
        """

        count = 0

        for player in self.players:
            self.player_list.add_at_the_head(player)
            count += 1

        for lap in range(count - 1):
            self.player_list.delete_from_head()

        self.assertEqual(self.player_list.get_head().get_player(), self.players[0])  # Player('Isabel', '1702')
        self.assertEqual(self.player_list.get_head().get_previous(), None)
        self.assertEqual(self.player_list.get_head().get_next(), None)
        self.assertEqual(self.player_list.get_head(), self.player_list.get_tail())

    def test_that_checks_the_last_remaining_node_deleting_from_tail(self):
        """
        Order when all the players have been added at the head:
        head_order: [Player('Carlos', '0317'), Player('Leonardo', '7734'), Player('Valeria', '1803'), Player('Isabel', '1702')]
        :return: None
        """

        count = 0

        for player in self.players:
            self.player_list.add_at_the_head(player)
            count += 1

        for lap in range(count - 1):
            self.player_list.delete_from_tail()

        self.assertEqual(self.player_list.get_head().get_player(), self.players[3])  # Player('Carlos', '0317')
        self.assertEqual(self.player_list.get_head().get_previous(), None)
        self.assertEqual(self.player_list.get_head().get_next(), None)
        self.assertEqual(self.player_list.get_head(), self.player_list.get_tail())

    def test_that_checks_that_list_is_empty_when_removing_the_last_node(self):
        """
        Order when all the players have been added at the head:
        head_order: [Player('Carlos', '0317'), Player('Leonardo', '7734'), Player('Valeria', '1803'), Player('Isabel', '1702')]
        :return: None
        """

        count = 0

        for player in self.players:
            self.player_list.add_at_the_head(player)
            count += 1

        for lap in range(count):
            self.player_list.delete_from_tail()

        self.assertEqual(self.player_list.get_head(), self.player_list.get_tail())
        self.assertEqual(self.player_list.get_head(), None)


    def test_that_checks_all_the_nodes_from_the_head_to_tail_after_removing(self):
        """
        head_order: [Player('Carlos', '0317'), Player('Leonardo', '7734'), Player('Valeria', '1803'), Player('Isabel', '1702')]
        :return: None

        Case 1_Delete from head:

        head_order = [Player('Leonardo', '7734'), Player('Valeria', '1803'), Player('Isabel', '1702')]

        Case 2_Deelete from tail

        head_order = [Player('Leonardo', '7734'), Player('Valeria', '1803')]

        Case 3_Delete from tail

        head_order = [Player('Leonardo', '7734')]

        Case 4_Delete from head

        head_order = [None]
        """
        head_order = [str(Player("0317", "Carlos")), str(Player("7734", "Leonardo")),
                      str(Player("1803", "Valeria")), str(Player("1702", "Isabel"))]
        order = [1, 2, 2, 1]
        count = 0

        for player in self.players:
            self.player_list.add_at_the_head(player)

        while count < len(head_order):

            if order[count] == 1:
                removed_item = self.player_list.delete_from_head()
            else:
                removed_item = self.player_list.delete_from_tail()

            node = self.player_list.get_head()
            head_order.remove(str(removed_item))

            for player in head_order:
                if len(head_order) == 0:
                    self.assertEqual(node, player)
                else:
                    self.assertEqual(str(node.get_player()), str(player))
                    node = node.get_next()

            count += 1

    def test_error_raised_when_deleting_in_an_empty_list_by_key(self):

        with self.assertRaises(IndexError):
            self.player_list.delete_by_key("1702")

    def test_value_error_raised_when_deleting_by_a_key_that_is_not_in_the_list(self):

        for player in self.players:
            self.player_list.add_at_the_head(player)

        with self.assertRaises(ValueError):
            self.player_list.delete_by_key("1234")

    def test_that_checks_the_whole_list_after_deleting_by_key(self):
        """
        head_order: [Player('Carlos', '0317'), Player('Leonardo', '7734'), Player('Valeria', '1803'), Player('Isabel', '1702')]
        :return: None
        """
        head_order = [str(Player("0317", "Carlos")), str(Player("7734", "Leonardo")),
                      str(Player("1803", "Valeria")), str(Player("1702", "Isabel"))]
        key_order = ["7734", "1803", "0317", "1702"]
        count = 0

        for player in self.players:
            self.player_list.add_at_the_head(player)

        while count < len(key_order):

            removed_item = self.player_list.delete_by_key(key_order[count])

            node = self.player_list.get_head()

            head_order.remove(str(removed_item))

            for player in head_order:
                if len(head_order) == 0:
                    self.assertEqual(node, None)
                else:
                    self.assertEqual(str(node.get_player()), str(player))
                    node = node.get_next()

            count += 1

    def test_type_error_raised_when_passing_not_boolean_arg_display_list_method(self):

        with self.assertRaises(TypeError):
            self.player_list.display_list("True")

    def test_that_displays_an_empty_list_when_empty(self):
        self.assertEqual(self.player_list.display_list(True), "[None]")
        self.assertEqual(self.player_list.display_list(False), "[None]")








