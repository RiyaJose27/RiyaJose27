class Bank:
        
    def __init__(self):
        self.balance = 0
        print("The account is created") 

    def user(self):
        self.name = (input("Enter the name :"))
        self.email = (input("Enter the email:"))
        print ("The name is  %s" % self.name)
        print ("The email  %s" % self.email)

    def deposit(self):
        amount = float(input("Enter the amount to be deposit: "))
        self.balance = self.balance + amount
        print ("Deposit is succesfsul and the balance in the account is %f" % self.balance)

    def withdraw(self):
            amount = float(input("Enter the amount to withdraw: "))
            if (self.balance >= amount):
                self.balance = self.balance - amount
                print ("The withdraw is successful and balance is %f" % self.balance)
            else:
                print ("Insufficient Balance")

acc = Bank()
acc.user()
acc.deposit()
acc.withdraw()


