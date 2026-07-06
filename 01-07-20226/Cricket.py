# Create the Data Set for the Players of World Cup of 2001 and 2007 
def world_cup_2011():
    print("Enter the Choice you want :")
    print("1. Winner of World Cup 2011")
    print("2. Players of World Cup 2011")
    print("3. Team those Score Greater than 400")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(f"The Winner of World Cup 2011 is: {world_cup[2011]['winner'].capitalize()}")
    elif choice == 2:
        print("Enter the Choice of Team to See the Players of World Cup 2011:")
        team = input().lower()
        if team in world_cup[2011]["Teams"]:
            print(f"Players of {team.capitalize()}")
            for player in world_cup[2011]["Teams"][team]:
                print(player)
        else:
            print("Invalid Team Choice")
    elif choice == 3:
        print("Teams that Scored Greater Than 4000 runs in World Cup 2011:")
        sum =0 
        for i in world_cup[2011]["Teams"]:
            for player in world_cup[2011]["Teams"][i]:
                for key in player:
                    sum += player[key]
            if sum > 4000:
                print(f"{i.capitalize()} scored {sum} runs")
    elif choice == 4:
        print("Thank you for using the World Cup Players Information System.")
        return
    else:
        print("Invalid Choice")
        
    choice = input("Do you want to Continue? (yes/no): ").lower()
    if choice == "yes":
        world_cup_2011() 
    else:
        print("Thank you for using the World Cup Players Information System.")
    

def world_cup_2027():
    print("Enter the Choice you want :")
    print("1. Winner of World Cup 2027")
    print("2. Players of World Cup 2027")
    print("3. Team those Score Greater than 400")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(f"The Winner of World Cup 2027 is: {world_cup[2027]['winner'].capitalize()}")
    elif choice == 2:
        print("Enter the Choice of Team to See the Players of World Cup 2027:")
        team = input().lower()
        if team in world_cup[2027]["Teams"]:
            print(f"Players of {team.capitalize()}")
            for player in world_cup[2027]["Teams"][team]:
                print(player)
        else:
            print("Invalid Team Choice")
    elif choice == 3:
        print("Teams that Scored Greater Than 4000 runs in World Cup 2027:")
        sum =0 
        for i in world_cup[2027]["Teams"]:
            for player in world_cup[2027]["Teams"][i]:
                for key in player:
                    sum += player[key]
            if sum > 4000:
                print(f"{i.capitalize()} scored {sum} runs")
    elif choice == 4:
        print("Thank you for using the World Cup Players Information System.")
        return
    else:
        print("Invalid Choice")
        
    choice = input("Do you want to Continue? (yes/no): ").lower()
    if choice == "yes":
        world_cup_2027() 
    else:
        print("Thank you for using the World Cup Players Information System.")

        
def world_cup_players():
    print("------World Cup is Here Now make it----")
    print("1. 2011")
    print("2. 2027")
    choice = int(input("Enter the year of World Cup to See the Players: "))
    if(choice==1):
        world_cup_2011()
    elif(choice==2):
        world_cup_2027()
    else:
        print("Invalid Choice")
        return
        
world_cup={
    2011:{
        "Teams":{
            "india":(
                {"MS Dhoni":150},{"Virat Kohli":120},{"Sachin Tendulkar":100},{"Rohit Sharma":90},{"Yuvraj Singh":80},{"Suresh Raina":70},{"Harbhajan Singh":60},{"Zaheer Khan":50},{"Jadeja":40},{"Bhuvneshwar Kumar":30},{"Shikhar Dhawan":20}
                ),
            "australia":(
                {"Ricky Ponting":100},{"Michael Clarke":90},{"Mitchell Johnson":80},{"David Warner":70},{"Glenn Maxwell":60},{"Steve Smith":50},{"Pat Cummins":40},{"Josh Hazlewood":30},{"Nathan Lyon":20},{"Aaron Finch":10}
                ),
            "pakistan":(
                {"Shahid Afridi":100},{"Shoaib Malik":90},{"Mohammad Amir":80},{"Sarfaraz Ahmed":70},{"Babar Azam":60},{"Fakhar Zaman":50},{"Hasan Ali":40},{"Shaheen Afridi":30},{"Imad Wasim":20}
                ),
            "sri lanka":(
                {"Kumar Sangakkara":100},{"Mahela Jayawardene":90},{"Lasith Malinga":80},{"Angelo Mathews":70},{"Thisara Perera":60},{"Dimuth Karunaratne":50},{"Dinesh Chandimal":40},{"Niroshan Dickwella":30},{"Kusal Perera":20}
            ),
            "new zealand":(
                {"Kane Williamson":100},{"Ross Taylor":90},{"Trent Boult":80},{"Tim Southee":70},{"Martin Guptill":60},{"Colin de Grandhomme":50},{"Tom Latham":40},{"Henry Nicholls":30}
            ),
            "south africa":(
                {"AB de Villiers":100},{"Faf du Plessis":90},{"Hashim Amla":80},{"Dale Steyn":70},{"Quinton de Kock":60},{"JP Duminy":50},{"Imran Tahir":40},{"David Miller":30}
            ),
            "west indies":(
                {"Chris Gayle":100},{"Kieron Pollard":90},{"Dwayne Bravo":80},{"Andre Russell":70},{"Jason Holder":60},{"Shai Hope":50},{"Nicholas Pooran":40},{"Sunil Narine":30}
            ),
            "bangladesh":(
                {"Shakib Al Hasan":100},{"Tamim Iqbal":90},{"Mushfiqur Rahim":80},{"Mahmudullah":70},{"Mustafizur Rahman":60},{"Soumya Sarkar":50},{"Mosaddek Hossain":40},{"Mehidy Hasan Miraz":30}
            ),
        },
        "winner":"india",
    },
    2027:{
        "Teams":{
            "india":[
                {"MS Dhoni":100},{"Virat Kohli":90},{"Sachin Tendulkar":80},{"Rohit Sharma":70},{"Yuvraj Singh":60},{"Suresh Raina":50},{"Harbhajan Singh":40},{"Zaheer Khan":30},{"Jadeja":20},{"Bhuvneshwar Kumar":10},{"Shikhar Dhawan":5}
            ],
            "australia":[
                {"Ricky Ponting":100},{"Michael Clarke":90},{"Mitchell Johnson":80},{"David Warner":70},{"Glenn Maxwell":60},{"Steve Smith":50},{"Pat Cummins":40},{"Josh Hazlewood":30},{"Nathan Lyon":20},{"Aaron Finch":10}
            ],
            "pakistan":[
                {"Shahid Afridi":100},{"Shoaib Malik":90},{"Mohammad Amir":80},{"Sarfaraz Ahmed":70},{"Babar Azam":60},{"Fakhar Zaman":50},{"Hasan Ali":40},{"Shaheen Afridi":30},{"Imad Wasim":20}
            ],
            "sri lanka":[
                {"Kumar Sangakkara":100},{"Mahela Jayawardene":90},{"Lasith Malinga":80},{"Angelo Mathews":70},{"Thisara Perera":60},{"Dimuth Karunaratne":50},{"Dinesh Chandimal":40},{"Niroshan Dickwella":30},{"Kusal Perera":20}
            ],
            "new zealand":[
                {"Kane Williamson":100},{"Ross Taylor":90},{"Trent Boult":80},{"Tim Southee":70},{"Martin Guptill":60},{"Colin de Grandhomme":50},{"Tom Latham":40},{"Henry Nicholls":30}
            ],
            "south africa":[
                {"AB de Villiers":100},{"Faf du Plessis":90},{"Hashim Amla":80},{"Dale Steyn":70},{"Quinton de Kock":60},{"JP Duminy":50},{"Imran Tahir":40},{"David Miller":30}
            ],
            "west indies":[
                {"Chris Gayle":100},{"Kieron Pollard":90},{"Dwayne Bravo":80},{"Andre Russell":70},{"Jason Holder":60},{"Shai Hope":50},{"Nicholas Pooran":40},{"Sunil Narine":30}
            ],
            "bangladesh":[
                {"Shakib Al Hasan":100},{"Tamim Iqbal":90},{"Mushfiqur Rahim":80},{"Mahmudullah":70},{"Mustafizur Rahman":60},{"Soumya Sarkar":50},{"Mosaddek Hossain":40},{"Mehidy Hasan Miraz":30}
            ]
        },
        "winner":"Unpredicted",
    }
}
world_cup_players()