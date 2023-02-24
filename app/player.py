class Player:
    def __init__(self, id: str, name: str):
        self._id = id
        self._name = name

    @property
    def uid(self):
        return str(self._id)

    @property
    def name(self):
        return str(self._name)

    def __repr__(self):
        return f"Player({self._name!r}, {str(self._id)!r})"

if __name__ == "__main__":
    player1 = Player(123, "Angelica")
    print(player1)
