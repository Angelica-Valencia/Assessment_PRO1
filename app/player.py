from argon2 import PasswordHasher

class Player:
    def __init__(self, id: str, name: str):
        self._id = id
        self._name = name
        self._password_hasher = PasswordHasher()
        self._hashed_password = None

    @property
    def uid(self):
        return str(self._id)

    @property
    def name(self):
        return str(self._name)

    def add_password(self, password: str):

        self._hashed_password = self._password_hasher.hash(password)

    def verify_password(self, password: str) -> bool:

        try:
            return self._password_hasher.verify(self._hashed_password, password)
        except Exception as e:
            print(repr(e))
            return False

    def __repr__(self):
        return f"Player({self._name!r}, {str(self._id)!r})"


if __name__ == "__main__":
    player1 = Player(123, "Angelica")
    print(player1)
    player1.add_password("Thank God")
    print(player1.verify_password("Thank God"))
    print(player1.verify_password("Ooops"))
