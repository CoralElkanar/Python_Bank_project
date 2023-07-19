from bank_accounts import *

# instance of the BankAccount class
Coral = BankAccount(1000, "Coral")
Rom = BankAccount(2000, "Rom")

Coral.getBalance()
Rom.getBalance()

Rom.deposit(500)

Coral.withdraw(10000)
Coral.withdraw(10) 

Coral.transfer(10000, Rom)
Coral.transfer(100, Rom)

Hod = InterestReawardAccount(1000, "Hod")

Hod.getBalance()

# depositing amount to an InterestRewardAccount will outcome with adding the amount + 5%
Hod.deposit(100)

# notice - the transfer function uses the withdraw function, and in that way we check both functions
Hod.transfer(100, Coral)

Sky = SavingsAccount(1000, "Sky")

Sky.getBalance()

Sky.deposit(100)

Sky.transfer(10000, Coral)
Sky.transfer(1000, Coral)