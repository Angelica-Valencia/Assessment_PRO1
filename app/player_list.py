class PlayerList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        if self._head:
            return False
        else:
            return True
