class BankAccount:

    def __init__(self, accountNumber, balance):
        self.__accountNumber = accountNumber
        self.__balance = balance

    def deposit(self, x):
        self.__balance = self.__balance + x
        return self.__balance

    def withdraw(self, y):
        self.__balance = self.__balance - y
        return self.__balance

bank = BankAccount(2, 230)
x = bank.deposit(5)
y = bank.withdraw(20)

print(x, y)