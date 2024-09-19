from Bank_Account import *

Pavithran=BankAccount(100000,"Pavithran")
#get balance from pavithran account
ajay=BankAccount(1000,'ajay')

Pavithran.get_balance()
#deposit ammount 1000 in pavithran account
Pavithran.deposit(200000)



Pavithran.transfer(100000,'ajay')
