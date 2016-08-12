from openpyxl import load_workbook
 
teams = []

#homeAway is a flag that tells the function if it is printing the home team options or the away team options. 1 if home team. 0 if away
#This matters because while printing the away team options, I don't want to show the already selected home team as an option
#Example: if team A is the home team, you should not be able to pick Team A again as the away team
#This function will print the appropriate team choices, and return the index of the team chosen
def printTeamOptions(homeAway):
    wb = load_workbook("Soccer Points Database.xlsx", data_only=True)
    sheet = wb["Sheet1"]
    for num in range(0, 20):
        cell_num = "A"+str((num+1))
        teams.append(sheet[cell_num].value)

def main():
    print("Enter home team: ")
    printTeamOptions(1) #So that it prints options for the home team
    print(teams)

if __name__ == '__main__':
    main()