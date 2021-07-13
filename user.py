class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    
    def make_withdrawal(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
        else:
            print("Insufficient funds for withdrawal! Current balance is:", self.account_balance)
        return self.account_balance

    def display_user_balance(self):
        print("Current balance for ", self.name, "is:", self.account_balance)
        return self.account_balance

    def transfer_money( self, person, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            person.account_balance += amount  
            print("Transfering ", amount, " from ", self.name, " to ", person.name)  
            print("Current balance for ", self.name, "is:", self.account_balance)
            print("Current balance for ", person.name, "is:", person.account_balance)
        else:
            print("Insufficient funds for transfer! Current balance is:", self.account_balance)
    
nate = User("Nate Langione", "nate@gmail.com")
john = User("John smith", "jsmith@gmail.com")
jane = User("Jane doe", "jdoe@gmail.com")


nate.make_deposit(100)
nate.make_deposit(10)
nate.make_deposit(45)
nate.make_withdrawal(50)
nate.display_user_balance()

john.make_deposit(25)
john.make_deposit(75)
john.make_withdrawal(57)
john.make_withdrawal(25)
john.display_user_balance()

jane.make_deposit(500)
jane.make_withdrawal(40)
jane.make_withdrawal(200)
jane.make_withdrawal(85)
jane.display_user_balance()

nate.transfer_money(jane, 50)