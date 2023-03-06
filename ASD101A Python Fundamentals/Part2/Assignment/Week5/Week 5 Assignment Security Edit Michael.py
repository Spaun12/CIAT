#Week 5 Assignment Security Edit Michael Connell
#Bank bones exercise
class Account:
    def __init__(self, balance=0):
        self.__balance = balance

    # Method to get the balance (child classes can use this to access the balance attribute)
    def _get_balance(self):
        return self.__balance

    # Method to set the balance (child classes can use this to modify the balance attribute)
    def _set_balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self.__interest_rate = 0.02

    def calculate_interest(self):
        # Use the _get_balance method to access the balance attribute
        interest = self._get_balance() * self.__interest_rate
        self.deposit(interest)

class CheckingAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

class MoneyMarketAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self.__interest_rate = 0.03

    def calculate_interest(self):
        # Use the _get_balance method to access the balance attribute
        interest = self._get_balance() * self.__interest_rate
        self.deposit(interest)

# Example usage of the classes
savings = SavingsAccount(1000)
savings.calculate_interest()
print(savings._get_balance())  
# Expected output: 1020 (1000 + 2% interest)

checking = CheckingAccount(500)
checking.deposit(100)
checking.withdraw(200)
print(checking.get_balance())  
# Expected output: 400

money_market = MoneyMarketAccount(2000)
money_market.calculate_interest()
print(money_market._get_balance())  
# Expected output: 2060 (2000 + 3% interest)