class BankAccount:

    bank_name = "First National Bank "
    all_accounts = []


    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            self.balance = self.balance - 5
            print("Insufficinet funds")
        return self

    def display_account_info(self):
        print("Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
           self.balance += (self.balance * self.int_rate)
        return self
# ---------------------->
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdrawl(self, amount):
        if amount <= self.account.balance:
            self.account.balance -= amount
        else:
            return "Insuffiecient funds"
        return self

    

    def display_user_balance(self):
        print("User: {self.name}, Balance: ${self.account.balance}")
        return self

    def transfer_money(self, User, amount):
        if amount <= self.account.balance:
            User.account.balance += amount
            self.account.balance -= amount
        else:
            return "insufficinet funds"
        return self

    def example_method(self):
        paul.account.deposit(100)
        print(self.account.balance)

paul = User("friya", "friya@gmail.com")
dan  = User("daniel", "daniel@gmail.com")
phil = User("diya", "diya3@gmail.com")

print(paul.name, paul.email)
print(dan.name, dan.email)
print(phil.name, phil.email)

paul.make_deposit(100)
paul.make_withdrawl(45)
print(paul.account.balance)
paul.display_user_balance()


paul.make_deposit(100).make_deposit(347).make_deposit(289).make_withdrawl(450).display_user_balance()
dan.make_deposit(1000).make_deposit(543).make_withdrawl(3).display_user_balance()
phil.make_deposit(10000).make_withdrawl(2800).make_withdrawl(4000).make_withdrawl(347).display_user_balance()

paul.transfer_money(dan, 25)
paul.display_user_balance()
phil.display_user_balance()