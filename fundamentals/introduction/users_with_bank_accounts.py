class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = [BankAccount(int_rate=.02, balance=10)]

    def make_deposit(self, amount, type):
        for account in self.accounts:
            if account.acct_type == type:
                account.deposit(amount)
                return self
        print(f"this user does not have a {type} account.  Transaction Cancelled")
        return self
    def make_withdrawl(self, amount, type):
        for account in self.accounts:
            if account.acct_type == type:
                account.withdraw(amount)
                return self
        print(f"this user does not have a {type} account.  Transaction Cancelled")
        return self
    def get_balance_info(self):
        for account in self.accounts:
            account.display_account_info()
        return self
    def open_checking_acct(self):
        self.accounts.append(BankAccount(int_rate=.005, balance=10, type = "Checking"))
        return self
    def transfer_money(self, amount, other_user):
        # start by withdrawing the money from the account being transferred out of
        # We will start by assuming this transfer will be savings to savings
        # False will be returned if there are insufficient funds to make the transer
        if self.make_withdrawl(amount, "Savings") == True:
        # target the other user by object name and make a deposit
            other_user.make_deposit(amount, "Savings")
        else:
            print("Insufficient Funds for this transfer.  Transaction Cancelled")
        return self



class BankAccount:
    bank_name = "First Bank of the Coding Dojo"
    all_accts = []

    def __init__(self, int_rate, balance, type = "Savings"):
        self.int_rate = int_rate
        self.balance = balance
        self.acct_type = type
        BankAccount.all_accts.append(self)

    @classmethod
    def all_balances(cls):
        for accounts in cls.all_accts:
            print(f"${accounts.balance} in this {accounts.acct_type} accounts")

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return True
        else:
            print("insufficient funds for this transaction")
            return False
    def display_account_info(self):
        print(f"Balance: ${self.balance} in {self.acct_type}")
        return self
    def yield_interest(self):
        new_balance = self.balance + (self.int_rate * self.balance)
        print(f"Balance plus Interest: {new_balance}")
        return self


userBart = User("Bart Simpson", "bsimpson@springfieldelem.org")
userHomer = User("Homer Simpson", "hsimpson47@springfieldnuke.com")

userBart.open_checking_acct()

userBart.make_deposit(200, "Savings")

userBart.make_deposit(100, "Checking")

print("Bart Balance Info Pre-Transfer")
userBart.get_balance_info()
print("Homer Balance Info Pre-Transfer")
userHomer.get_balance_info()

userBart.transfer_money(25, userHomer)

print("Bart Balance Info Post-Transfer")
userBart.get_balance_info()
print("Homer Balance Info Post-Transfer")
userHomer.get_balance_info()