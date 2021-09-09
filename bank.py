class BankAccount:
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        # BankAccount.all_accounts.append(self)


    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: {self.balance}")
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            self.balance = self.balance - 5
            print("Insufficinet funds")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
           self.balance += (self.balance * self.int_rate)
        return self
        
a = BankAccount()
a.deposit(1000).withdraw(500).yield_interest().display_account_info

a.display_account_info()
# a.display_account_info()


