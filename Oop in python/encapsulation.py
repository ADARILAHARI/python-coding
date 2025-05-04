class BankAccount:
    def __init__(self):
        self.__balance = 0  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Test
acc = BankAccount()
acc.deposit(100)
print(acc.get_balance())  # Output: 100
