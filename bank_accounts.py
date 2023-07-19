class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}") 
        # notice - .2f means we'll get 2 numbers after the dot for the decimal value of the balance of this account

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit of ${amount} to '{self.name}' completed.")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f} and cannot withdraw ${amount}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            # if we succedded to pass the viableTransaction exception it means we have enough money to withdraw.
            self.balance -= amount
            print(f"\nWithdraw of ${amount} from '{self.name}' account completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}") 

    def transfer(self, amount, account):
        try:
            print("\n*****************\n\nBeggining Transfer... 🚀")
            
            # check if there is enough money to withdraw from the account we perform this function on
            self.viableTransaction(amount)

            # withdraw the amount from this account
            self.withdraw(amount)

            # add the same amount to the account we're passing the money to
            account.deposit(amount)

            print("\nTransfer complete! ✅\n\n*****************")
        except BalanceException as error:
            print(f"\nTransfer from '{self.name}' to '{account.name}' of ${amount} interrupted ❌.{error}")

class InterestReawardAccount(BankAccount):
    # new class inherits everything from parent class BankAccount
    # override of the deposit function from the parent: any amount that gets deposited is rewarded with 5%
    def deposit(self, amount):
        self.balance += (amount * 1.05) 
        print(f"\nDeposit of ${amount} to '{self.name}' account completed")
        self.getBalance()

class SavingsAccount(InterestReawardAccount):
    # in order to add another property to the class we need to define the init method to the class again, and then use 'super' to inherit everything else from the parent class. 

    def __init__(self, initialAmount, accountName):
        def __init__(self, initialAmount, accountName):
            super().__init__(initialAmount, accountName)
            # we add a 'fee' parameter to this class, it will represent the fee [$] that will be added to any withdraw from the account
            self.fee = 5

        # override the withdraw function of the parent in order to add the fee
        def withdraw(self, amount):
            try:
                # check if there's enough money in the account (including the fee)
                self.viableTransaction(amount + self.fee)     
                self.balance -= (amount + self.fee)
                print(f"\nWithdraw of ${amount} and ${self.fee} completed.")
                self.getBalance()

            except BalanceException as error:
                print(f"\nWithdraw interrupted: {error}")