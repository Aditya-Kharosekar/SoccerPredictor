from openpyxl import load_workbook
 
teams = []

#This function will print the appropriate team choices, and return a list. The first element will be the index of the home team.
#The second element will be the index of the away team
def getTeamSelections():
    indexResults = []

    wb = load_workbook("Soccer Points Database.xlsx", data_only=True)
    sheet = wb["Sheet1"]

    for num in range(1, 21):        #Reading from my excel database and putting all 20 team names into the list teams[]
        cell_num = "A"+str((num))
        teams.append(sheet[cell_num].value)

    for num in range (0, 20):       #printing the home team options
        print(str(num+1) + ". " + teams[num])
    print("Enter index: ")
    home = int(input()) - 1     #I subtract 1 because the printed index of the team is actually one more than the team's index in teams[]
                                #Example: Leicester City is shown as the 8th team but it has index 7
    print("You have chosen " + teams[home] + " as the home team")
    indexResults.append(home)
    
    print("Enter index of away team: ")
    for num in range(0, 20):        #printing the away team options
       if (num!=home):              #i.e if team hasn't already been selected as the home team
           print(str(num+1) + ". " + teams[num])
    print("Enter index: ")
    away = int(input()) - 1     #I subtract 1 for the same reason as above
    print("You have chosen " + teams[away] + " as the away team")
    indexResults.append(away)  
    return indexResults    

#Takes in list of index of home team and of away team. Reads excel database and returns a list. First element will be rating of home team.
#Second element will be rating of away team
def getTeamRatings(teamchoices):
    homeTeamIndex = teamchoices[0]
    awayTeamIndex = teamchoices[1]
    wb = load_workbook("Soccer Points Database.xlsx", data_only=True)
    sheet = wb["Sheet1"]

    home_cell_num = "E" + str(homeTeamIndex+1)      # I add 1 to get the correct team's rating. The index in teamChoices[] is 1 less than the
    away_cell_num = "E" + str(awayTeamIndex+1)      # row number in the excel sheet
    homeRating = sheet[home_cell_num].value;
    awayRating = sheet[away_cell_num].value
    return [homeRating, awayRating]
              

def main():
    print("Enter index of home team: ")
    teamChoices = getTeamSelections()
    print(teamChoices)
    teamRatings = getTeamRatings(teamChoices);
    print(teamRatings)


if __name__ == '__main__':
    main()