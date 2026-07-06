#Create ATM Managment System Where first 
#1.) Choose a Language
#  2.) after langugae we Have to use withdraw , Balance , Pin Change , help 
def withdrawmoney(account):
    print("Withdraw")
    amount=int(input("Enter the amout you want to withdraw :"))
    if(amount > atm_users[account]["balance"]):
        print("Insufficient Balance")
    else:
        atm_users[account]["balance"]-=amount
        print("Amount withdraw ",amount)
        print("Current Balance ",atm_users[account]["balance"])
def debitmoney(account):
    print("debit")
    amount=int(input("Enter the amout you want to withdraw :"))
    if(amount > atm_users[account]["balance"]):
        print("Insufficient Balance")
    else:
        atm_users[account]["balance"]+=amount
        print("Amount withdraw ",amount)
        print("Current Balance ",atm_users[account]["balance"])
def TasksinATM(account,pin):
    print("------Operation you Can Perform in the Account-----")
    print("1. Check balance")
    print("2. Withdraw Money")
    print("3. Debit Money")
    print("4. help")
    
    choice= int(input("Enter the Choice you want !!"))
    if(choice==1):
        print("your Balace:")
        print(atm_users[account]["balance"])
    elif(choice ==2):
        withdrawmoney(account)
    elif(choice ==3):
        debitmoney(account)  
    elif(choice ==4):
        print("How Can i Help you !!")
        print("Thanks for help if you Want to get the help contact 923xxxx3 and email 23432@gmail.com")
    else:
        print("Thanks for your Attention")
    choice =input("Enter the Choice")
    if(choice=='y'):
        TasksinATM(account,pin)
    else:
        print("Thankyou !!!")
def AtmManegment():
    print("----Welcome to ATM ----")
    account =input("Enter the ATM Number :")
    pin =input("Enter the ATM PIN :")
    
    for atmaccount in atm_users:
        if atmaccount == account:
            if atm_users[account]["pin"] == pin:
                print("You are verified.")
                TasksinATM(account, pin)
            else:
                print("Invalid PIN")
        else:
            print("Account is Not there !!!")
            break

atm_users = {
    "001": {
        "pin": "1234",
        "balance": 5000,
        "name": "Alex",
        "transactions":{
            "date":"",
            "amount":"",
            "type":""
        }
    },
    "002": {
        "pin": "2345",
        "balance": 12500,
        "name": "Sam"
    },
    "003": {
        "pin": "3456",
        "balance": 8000,
        "name": "Emma"
    },
    "004": {
        "pin": "4567",
        "balance": 15000,
        "name": "John"
    },
    "005": {
        "pin": "5678",
        "balance": 9200,
        "name": "Sophia"
    },
    "006": {
        "pin": "6789",
        "balance": 20000,
        "name": "Liam"
    },
    "007": {
        "pin": "7890",
        "balance": 3400,
        "name": "Olivia"
    },
    "008": {
        "pin": "8901",
        "balance": 7800,
        "name": "Noah"
    },
    "009": {
        "pin": "9012",
        "balance": 11200,
        "name": "Ava"
    },
    "010": {
        "pin": "1357",
        "balance": 6500,
        "name": "Ethan"
    },
    "011": {
        "pin": "2468",
        "balance": 4300,
        "name": "Mia"
    },
    "012": {
        "pin": "1593",
        "balance": 9900,
        "name": "James"
    },
    "013": {
        "pin": "7531",
        "balance": 17000,
        "name": "Charlotte"
    },
    "014": {
        "pin": "8642",
        "balance": 25000,
        "name": "Benjamin"
    },
    "015": {
        "pin": "4321",
        "balance": 6000,
        "name": "Amelia"
    }
}

AtmManegment()