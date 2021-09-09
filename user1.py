class User: 
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
        # print('hello')

u1 = User("frita", "frita@comcast.com")
u2 = User("Cindy", "Cindy@gmail.com")
u3 = User("Albert", "albert@yahoocom")

u1.make_deposit(200).make_deposit(200).make_deposit(200).make_withdrawal(50).display_user_balance()
u2.make_deposit(300).make_deposit(300).make_withdrawal(100).make_withdrawal(100).display_user_balance()
u3.make_deposit(1000).make_withdrawal(300).make_withdrawal(300).make_withdrawal(300).display_user_balance()
u1.transfer_money(u3, 500).display_user_balance()
u2.display_user_balance()
u3.display_user_balance()