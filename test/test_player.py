import unittest
from app.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self) -> None: # This overrides the method setUp.
        self.player_1 = Player("123", "Juan")
        self.player_numeric_id = Player(456, "Carlos")
        self.player_boolean_name = Player(456, False)

    def test_that_uid_property_returns_the_value(self):

        self.assertEqual(self.player_1.uid, "123")

    def test_that_name_property_returns_the_value(self):

        self.assertEqual(self.player_1.name, "Juan")

    def test_that_uid_returns_a_string(self):

        self.assertEqual(self.player_numeric_id.uid, "456")

    def test_that_name_returns_a_string(self):

        self.assertEqual(self.player_boolean_name.name, "False")