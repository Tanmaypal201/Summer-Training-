def Gross_of_family():
    print("---------Gross of Family--------")
    dict={}
    while(True):
        member=input("Enter the Family Member Name :")
        salary=int(input(f"Enter the salary of {member} :"))
        dict[member]=salary
        ch=input("Enter the Choice of you want to add member who income is there then (y/n)")
        if(ch!="y"):
            print("Exit")
            break
    tax=int(input("Enter the Amount of Tax :"))
    sum=0
    for i in dict:
        sum+=dict[i]
    grossal=sum-(sum*tax)/100
    print("Gross Salary :",grossal)

Gross_of_family()