from openpyxl import load_workbook
 
teams = []

#This function will print the appropriate team choices, and return a list. The first element will be the index of the home team.
#The second element in the list will be the index of the away team
def printTeamOptions():
    result = []     #This will be the list that the function returns

    wb = load_workbook("Soccer Points Database.xlsx", data_only=True)
    sheet = wb["Sheet1"]

    for num in range(0, 20):        #putting all 20 team names into the list teams[]
        cell_num = "A"+str((num+1))
        teams.append(sheet[cell_num].value)

    for num in range (0, 20):       #printing the home team options
        print(str(num+1) + ". " + teams[num])
    print("Enter index: ")
    home = int(input())
    result.append(home)
    
    for num in range(0, 20):        #printing the away team options
       if (num!=home):
           print(str(num+1) + ". " + teams[num])
    print("Enter index: ")
    away = int(input())
    result.append(away)  
    return result                 

def main():
    print("Enter index of home team: ")
    teamChoices = printTeamOptions()
    print(teamChoices)

if __name__ == '__main__':
    main()