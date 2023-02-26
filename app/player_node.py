from __future__ import annotations
from app.player import Player


class PlayerNode:
    def __init__(self, player: Player):
        self._player = player
        self._previous = None
        self._next = None
        self.key = self.get_key()

    def get_player(self):
        return self._player

    def get_previous(self):
        return self._previous

    def get_next(self):
        return self._next

    def set_previous(self, previous) -> PlayerNode:
        self._previous = previous

    def set_next(self, next_one):
        self._next = next_one

    def get_key(self):
        return self._player.uid

    def __repr__(self):
        next = self._next._player if self._next is not None else "None"
        prev = self._previous._player if self._previous is not None else "None"
        return f"PlayerNode(Previous:  {prev!r}, {self._player!r}, Next: {next!r})"
        # return f"PlayerNode({self._player!r}"
    # def __str__(self):
    #     return f"Player: {self._player}\nPrevious: {self._previous}\nNext: {self._next}"



if __name__ == "__main__":

    player_node = PlayerNode(Player("123", "Juan"))

    print(player_node)