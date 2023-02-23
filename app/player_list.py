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

    def get_tail(self):
        return self._tail

    def add_head_tail_when_empty(self, node_player):
        self._head = node_player
        self._tail = node_player

    def add_at_the_head(self, player: Player):
        new_player_node = PlayerNode(player)
        if self.is_empty():
            self.add_head_tail_when_empty(new_player_node)
        else:
            self._head.set_previous(new_player_node.get_player())
            previous_head = self._head
            new_player_node.set_next(previous_head)
            self._head = new_player_node

    def add_at_the_tail(self, player: Player):
        new_player_node = PlayerNode(player)
        if self.is_empty():
            self.add_head_tail_when_empty(new_player_node)
        else:
            node = self._head

            while node.get_next():
                node = node.get_next()
            # mod_player_node = new_player_node.set_previous(node)
            node.set_next(new_player_node)


if __name__ == "__main__":

    my_list = PlayerList()
    print(my_list.get_head(), my_list.is_empty(), "\n")

    # my_list.add_at_the_head(Player("123", "Lina"))
    # print(my_list.get_head(), my_list.is_empty(), "\n")
    # print("Tail:", "\n")
    # print(my_list.get_tail(), "\n")
    #
    # my_list.add_at_the_head(Player("456", "Eliza"))
    # print(my_list.get_head(), my_list.is_empty(), "\n")
    # print("Tail:", "\n")
    # print(my_list.get_tail(), "\n")
    #
    # my_list.add_at_the_head(Player("678", "Tania"))
    # print(my_list.get_head(), my_list.is_empty(), "\n")
    # print("Tail:", "\n")
    # print(my_list.get_tail(), "\n")
    #
    # my_list.add_at_the_head(Player("213", "Marce"))
    # print(my_list.get_head(), my_list.is_empty(), "\n")
    # print("Tail:", "\n")
    # print(my_list.get_tail(), "\n")
    # print(my_list.get_tail().get_key(), "\n")

    my_list.add_at_the_tail(Player("123", "Lina"))
    print(my_list.get_head(), my_list.is_empty(), "\n")
    print("Tail:", "\n")
    print(my_list.get_tail(), "\n")

    my_list.add_at_the_tail(Player("456", "Eliza"))
    print(my_list.get_head(), my_list.is_empty(), "\n")
    print("Tail:", "\n")
    print(my_list.get_tail(), "\n")

    my_list.add_at_the_tail(Player("678", "Tania"))
    print(my_list.get_head(), my_list.is_empty(), "\n")
    print("Tail:", "\n")
    print(my_list.get_tail(), "\n")

    my_list.add_at_the_tail(Player("213", "Marce"))
    print(my_list.get_head(), my_list.is_empty(), "\n")
    print("Tail:", "\n")
    print(my_list.get_tail(), "\n")
    print(my_list.get_tail().get_key(), "\n")
