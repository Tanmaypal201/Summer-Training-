'''Create an Employee class with Employee ID, Name, Basic Salary.
Methods to calculate HRA (20%), DA (10%), Gross Salary, and display details
'''
class Employee():
    
    empId=0
    name=""
    basicsal=0
    HRA=0
    DA=0
    
    def __init__(self, id ,name , sal):
        self.empId=id
        self.name=name
        self.basicsal=sal
        
    def cal_HRA(self):
        self.HRA=(self.basicsal*20)/100
        print(f"HRA : {self.HRA}")
    def cal_DA(self):
        self.DA=(self.basicsal*10)/100
        print(f"DA : {self.HRA}")
    def GrossSal(self):
        Grosssalary=self.HRA+self.DA+self.basicsal
        print(f"Gross Salary :{Grosssalary}")
    def getdetails(self):
        print("-----Here is the Details-----")
        print(f"Employee ID :{self.empId}")
        print(f"Name :{self.name}")
        print(f"Basic Salary :{self.basicsal}")
        print(f"HRA and DA :{self.HRA} & {self.DA}")

e1=Employee(1,"Tanmay",100000)

e1.cal_HRA()
e1.cal_DA()
e1.GrossSal()
e1.getdetails()