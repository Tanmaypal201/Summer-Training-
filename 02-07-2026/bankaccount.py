'''Create a BankAccount class with Account Holder Name, Account Number, Balance.
Methods: deposit(), withdraw(), display_balance().
Conditions: Deposit must be positive and withdrawal cannot exceed balance
'''
class account():
    act_num=0
    act_hold=""
    balance=0
    
    def __init__(self , act_num , act_hold , balance):
        self.act_num=act_num
        self.act_hold=act_hold
        self.balance=balance
    def get_account_details(self):
        print("-----ACCOUNT DETAILS OF YOURS------")
        print(f"This Account {self.act_hold} holds {self.act_num}")
        print(self.act_hold)
    def deposit(self, amount):
        self.balance=self.balance+amount
        print(f"{amount} is Deposit to your bank now the Current Balance {self.balance}")
    def withdraw(self, amount):
        if(self.balance < amount):
            print("Insufficient to Deduct")
            return
        self.balance=self.balance - amount
        print(f"{amount} is Withdraw to your bank now the Current Balance {self.balance}")
    def display_balance(self):
        print(f"Current Balance {self.balance}")
        
a1=account(78,"Tanmay",7000)
a1.get_account_details()
a1.deposit(5000)
a1.withdraw(1000)
a1.display_balance()