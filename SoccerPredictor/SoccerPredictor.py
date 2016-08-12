from openpyxl import load_workbook
 
teams = []

#This function will print the appropriate team choices, and return a list. The first element will be the index of the home team.
#The second element in the list will be the index of the away team
def printTeamOptions():
    result = []     #This will be the list that the function returns

    wb = load_workbook("Soccer Points Database.xlsx", data_only=True)
    sheet = wb["Sheet1"]

    for num in range(1, 21):        #putting all 20 team names into the list teams[]
        cell_num = "A"+str((num))
        teams.append(sheet[cell_num].value)

    for num in range (0, 20):       #printing the home team options
        print(str(num+1) + ". " + teams[num])
    print("Enter index: ")
    home = int(input()) - 1     #I subtract 1 because the printed index of the team is actually one more than the team's index in teams[]
                                #Example: Leicester City is shown as the 8th team but it has index 7
    print("You have chosen " + teams[home])
    result.append(home)
    
    for num in range(0, 20):        #printing the away team options
       if (num!=home):
           print(str(num+1) + ". " + teams[num])
    print("Enter index: ")
    away = int(input()) - 1     #I subtract 1 for the same reason as above
    result.append(away)  
    return result                 

def main():
    print("Enter index of home team: ")
    teamChoices = printTeamOptions()
    print(teamChoices)

if __name__ == '__main__':
    main()