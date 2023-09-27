class BankAccount:
    bank_name = "First Bank of the Coding Dojo"
    all_accts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accts.append(self)

    @classmethod
    def all_balances(cls):
        for account in cls.all_accts:
            print(f"${account.balance} in this account")

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        new_balance = self.balance + (self.int_rate * self.balance)
        print(f"Balance plus Interest: {new_balance}")
        return self



acc1 = BankAccount(.05, 1500)

acc2 = BankAccount(.02, 500)

acc1.deposit(100).deposit(20).deposit(130).withdraw(10).yield_interest().display_account_info()

acc2.deposit(5000).deposit(500).withdraw(100).withdraw(750).withdraw(10).withdraw(20).yield_interest().display_account_info()

BankAccount.all_balances()