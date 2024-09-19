#create class name BAnkAccount
class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,initial_account,acct_name):
        self.balance=initial_account
        self.name=acct_name
        print(f"\n account= '{self.name}'created.\n balance={self.balance:.2f}$")

    def get_balance(self):
        print(f"\n Account '{self.name}' balance= ${self.balance:.2f}")

    def deposit(self,ammount):
        self.balance=self.balance+ammount
        print("\n deposit complete.")
        self.get_balance()

    def viable_transaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\n sorry account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self,amount):
        try:
            self.viable_transaction(amount)
            self.balance=self.balance+amount
            print("\n withdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\n withdraw interruped:{error}")

    def transfer(self,amount,account):
        try:
            print('\n**********\n\n Begining Transfer... ')
            self.viable_transaction(amount)
            self.withdraw(amount)
            self.deposit(amount)

        except BalanceException as error:
            print(f'\n withdraw interruped: {error}')
