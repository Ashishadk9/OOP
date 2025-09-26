class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Cannot set negative balance")
        self.__balance = value

acc = BankAccount(1000)
acc.balance = -500