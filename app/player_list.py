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
        new_player_node_head = PlayerNode(player)
        new_player_node_tail = PlayerNode(player)
        if self.is_empty():
            self.add_head_tail_when_empty(new_player_node_tail)
        else:

            # node = self._head

            # while node.get_previous():
            #     node = node.get_previous()

            # new_player_node.set_next(self._head.get_player())
            # node.set_previous(new_player_node)
            # self._head = node.get_previous()

            # self._head.set_previous(new_player_node.get_player())
            # previous_head = self._head
            # new_player_node.set_next(previous_head)
            # self._head = new_player_node

            node = self._head
            node_tail = self._tail

            new_player_node_head.set_next(node)
            node.set_previous(new_player_node_head)
            self._head = new_player_node_head

            # node_tail.set_previous(None)

            # while node_tail.get_previous():
            #     node_tail = node_tail.get_previous()
            # new_player_node_tail.set_next(node_tail)
            # node_tail.set_previous(new_player_node_tail)
            # self._tail = node_tail

    def add_at_the_tail(self, player: Player):
        new_player_node = PlayerNode(player)
        if self.is_empty():
            self.add_head_tail_when_empty(new_player_node)
        else:
            # self._tail.set_next(new_player_node.get_player())
            # previous_tail = self._tail
            # new_player_node.set_previous(previous_tail)
            # self._tail = new_player_node

            node = self._tail

            while node.get_next():
                node = node.get_next()

            # new_player_node.set_previous(self._tail.get_player())
            # node.set_next(new_player_node)
            # self._tail = node.get_next()

            new_player_node.set_previous(node)
            node.set_next(new_player_node)
            self._tail = new_player_node

            # self._tail.set_next(new_player_node.get_player())
            # previous_tail = self._tail
            # new_player_node.set_previous(previous_tail)
            # self._tail = new_player_node

if __name__ == "__main__":

    my_list = PlayerList()
    print(my_list.get_head(), my_list.is_empty(), "\n")

    my_list.add_at_the_head(Player("456", "Eliza"))
    print("Head:", "\n")
    print(my_list.get_head(), "\n")
    print("Tail:", "\n")
    print(my_list.get_tail(), "\n")

    my_list.add_at_the_head(Player("678", "Tania"))
    print("Head:", "\n")
    print(my_list.get_head(), "\n")
    print("Tail:", "\n")
    print(my_list.get_tail(), "\n")

    my_list.add_at_the_tail(Player("213", "Marce"))
    print("Head:", "\n")
    print(my_list.get_head(), "\n")
    print("Tail:", "\n")
    print(my_list.get_tail(), "\n")

    my_list.add_at_the_tail(Player("213", "Carolina"))
    print("Head:", "\n")
    print(my_list.get_head(), "\n")
    print("Tail:", "\n")
    print(my_list.get_tail(), "\n")

    my_list.add_at_the_head(Player("213", "Alejandra"))
    print("Head:", "\n")
    print(my_list.get_head(), "\n")
    print("Tail:", "\n")
    print(my_list.get_tail(), "\n")

    tail = my_list.get_tail()
    head = my_list.get_head()

    while True:
        print(f"Tail:\n{tail}")
        print(f"Head:\n{head}")
        tail = tail.get_previous()
        head = head.get_next()
        if tail:
            pass
        else:
            break

