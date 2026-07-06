#Create a Student class with Name , Roll number , Marks 
#Methods here are get_data() , display_data() , calculate_parcentage()

class Student():
    name="unknown"
    roll=0
    subject={}
    
    def __init__(self, name , roll , subject):
        self.name=name
        self.roll=roll
        self.subject=subject
        
    def get_data(self):
        print("Getting the Data !! ")
        print(f"Name :{self.name} Roll :{self.roll}")
        for i in self.subject:
            print(f"subject :{i}", end="")
            print(f"Marks:{self.subject[i]}")
    def cal_percentage(self):
        print("Here is the percentage !! ")
        sum=0
        for i in self.subject:
            sum+=self.subject[i]
        percent=sum/(len(self.subject))
        print(percent,'%')
        
print("-----Here Go to the get the Student Data------")
name=input("Enter the Students Name:")
roll=int(input("Enter the Student roll number"))
subjects={}
i=0
while(True):
    i=i+1
    subject=input(f"Enter the Subject {i}:")
    marks=int(input(f"Enter the marks of {subject} :"))
    subjects[subject]=marks
    choice = input("Enter the Choice from y and n")
    if(choice!="y"):
        break

s1=Student(name,roll,subjects)
s1.get_data()
s1.cal_percentage()
                