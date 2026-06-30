class SecureTransaction:
    def __init__(self, amount):
        self._amount = amount  # Protected attribute

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value <= 0:
            raise ValueError("Amount must be positive!")
        self._amount = value