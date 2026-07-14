def Gross_of_family():
    print("--------- Gross Salary of Family --------")

    family = {}

    while True:
        member = input("Enter Family Member Name: ")
        salary = float(input(f"Enter the Basic Salary of {member}: "))

        family[member] = salary

        ch = input("Do you want to add another member? (y/n): ")
        if ch.lower() != 'y':
            break

    da_percent = float(input("\nEnter DA Percentage: "))
    hra_percent = float(input("Enter HRA Percentage: "))

    total_basic = sum(family.values())

    da = (total_basic * da_percent) / 100
    hra = (total_basic * hra_percent) / 100

    gross_salary = total_basic + da + hra

    print("\n----------- Salary Details -----------")
    print("Total Basic Salary :", total_basic)
    print("DA Amount          :", da)
    print("HRA Amount         :", hra)
    print("Gross Salary       :", gross_salary)


Gross_of_family()