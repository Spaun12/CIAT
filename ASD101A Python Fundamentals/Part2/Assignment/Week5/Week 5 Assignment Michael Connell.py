#Week 5 Assignment Michael Connell
#Bank bones exercise
class Account:
    def __init__(self, balance=0):
        self.__balance = balance

    def _get_balance(self):
        return self.__balance

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
        interest = self._get_balance() * self.__interest_rate
        self.deposit(interest)
        
# Example usage of the classes
savings = SavingsAccount(1000)
savings.calculate_interest()
print(f"Savings account balance: {savings._get_balance():.2f}")  
# Expected output: Savings account balance: 1020.00 (1000 + 2% interest)

checking = CheckingAccount(500)
checking.deposit(100)
checking.withdraw(200)
print(f"Checking account balance: {checking.get_balance():.2f}")  
# Expected output: Checking account balance: 400.00

money_market = MoneyMarketAccount(2000)
money_market.calculate_interest()
print(f"Money market account balance: {money_market._get_balance():.2f}")  
# Expected output: Money market account balance: 2060.00 (2000 + 3% interest)