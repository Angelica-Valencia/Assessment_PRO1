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

            node = self._head

            new_player_node_head.set_next(node)
            node.set_previous(new_player_node_head)
            self._head = new_player_node_head

    def add_at_the_tail(self, player: Player):
        new_player_node = PlayerNode(player)
        if self.is_empty():
            self.add_head_tail_when_empty(new_player_node)
        else:

            node = self._tail

            new_player_node.set_previous(node)
            node.set_next(new_player_node)
            self._tail = new_player_node

    def delete_from_head(self):
        if self.is_empty():
            raise IndexError("The list is empty")

        removed_item = self._head.get_player()

        if self._head == self._tail:
            self._head, self._tail = None, None
            return removed_item
        else:
            new_head = self.get_head().get_next()
            new_head.set_previous(None)
            self._head = new_head
            return removed_item

    def delete_from_tail(self):

        if self.is_empty():
            raise IndexError("The list is empty")

        removed_item = self._tail.get_player()

        if self._head == self._tail:
            self._head, self._tail = None, None
            return removed_item
        else:
            new_tail = self.get_tail().get_previous()
            new_tail.set_next(None)
            self._tail = new_tail
            return removed_item

    def delete_by_key(self, key: str):
        if self.is_empty():
            raise IndexError("The list is empty")
        if self._head == self._tail:
            if self._head.get_player().uid == key:
                removed_item = self._head.get_player()
                self._head, self._tail = None, None
                return removed_item
            else:
                raise ValueError(f"The player with key {key} is not in the list.")
        else:

            node = self._head
            while node:
                if node.get_player().uid == key:
                    removed_item = node.get_player()

                    next_node = node.get_next()
                    previous_node = node.get_previous()

                    if node.get_player() == self.get_head().get_player():
                        node.get_next().set_previous(None)
                        self._head = node.get_next()
                    elif node.get_player() == self.get_tail().get_player():
                        node.get_previous().set_next(None)
                        self._tail = node.get_previous()
                    else:
                        next_node.set_previous(previous_node)
                        previous_node.set_next(next_node)

                    return removed_item

                node = node.get_next()
            raise ValueError(f"The player with key {key} is not in the list.")

    def display_list(self, forward=True) -> str:

        node_forward = self._head
        node_backward =self._tail

        list_text = ""

        if type(forward) is not bool:
            raise TypeError("The argument passed in not boolean (True, False).")

        if self.is_empty():
            return "[None]"
        else:
            while True:

                if forward:

                    list_text += f"{node_forward}\n"
                    node_forward = node_forward.get_next()

                else:
                    list_text += f"{node_backward}\n"
                    node_backward = node_backward.get_previous()

                if node_forward and node_backward:
                    pass
                else:
                    break
            return list_text


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

    my_list.add_at_the_tail(Player("897", "Carolina"))
    print("Head:", "\n")
    print(my_list.get_head(), "\n")
    print("Tail:", "\n")
    print(my_list.get_tail(), "\n")

    my_list.add_at_the_head(Player("732", "Alejandra"))
    print("Head:", "\n")
    print(my_list.get_head(), "\n")
    print("Tail:", "\n")
    print(my_list.get_tail(), "\n")

    # print(my_list.delete_from_head())
    # print(my_list.delete_from_head())
    # print(my_list.delete_from_head())
    # print(my_list.delete_from_head())
    # print(my_list.delete_from_head())

    print(my_list.delete_by_key("897"))
    print(my_list.delete_by_key("732"))
    print(my_list.delete_by_key("456"))
    # print(my_list.delete_by_key("678"))
    # print(my_list.delete_by_key("213"))

    print(my_list.display_list(True))
    print(my_list.display_list(False))

    another_list = PlayerList()
    #
    # print(another_list.display_list(True))
    # print(another_list.display_list(False))


    # print("Head:", "\n")
    # print(my_list.get_head(), "\n")
    # print("Tail:", "\n")
    # print(my_list.get_tail(), "\n")
    #
    # tail = my_list.get_tail()
    # head = my_list.get_head()


    # while True:
    #     print(f"Tail:\n{tail}")
    #     print(f"Head:\n{head}")
    #     tail = tail.get_previous()
    #     head = head.get_next()
    #     if tail:
    #         pass
    #     else:
    #         break

