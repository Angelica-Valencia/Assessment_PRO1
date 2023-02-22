from app.player_node import PlayerNode
from app.player import Player


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        if self._head:
            return False
        else:
            return True

    def get_head(self):
        return self._head

    def add_at_the_head(self, player):
        new_player_node = PlayerNode(player)
        if self.is_empty():
            self._head = new_player_node
        else:
            self._head.set_previous(new_player_node.get_player())
            previous_head = self._head
            new_player_node.set_next(previous_head)
            self._head = new_player_node


    # def append(self, player):
    #     new_player_node = PlayerNode(player)
    #     if self.is_empty():
    #         self._head = new_player_node
    #         self._tail = new_player_node
    #     elif self._head == self._head:
    #         self._head.set_next(new_player_node)
    #         self._tail = new_player_node.
    #     else:
    #         node = self.

if __name__ == "__main__":

    my_list = PlayerList()
    print(my_list.get_head(), my_list.is_empty(), "\n")

    my_list.add_at_the_head(Player("123", "Lina"))
    print(my_list.get_head(), my_list.is_empty(), "\n")

    my_list.add_at_the_head(Player("456", "Eliza"))
    print(my_list.get_head(), my_list.is_empty(), "\n")

    my_list.add_at_the_head(Player("678", "Tania"))
    print(my_list.get_head(), my_list.is_empty(), "\n")

    my_list.add_at_the_head(Player("213", "Marce"))
    print(my_list.get_head(), my_list.is_empty(), "\n")