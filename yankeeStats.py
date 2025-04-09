def main():
    # Create a list (call it players) that will consist of the following New York Yankess player's names:  'Mickey Mantle', 'Yogi Berra', 'Lou Gehrig', 'Babe Ruth', 'Joe DiMaggio'.
    players = ['Mickey Mantle', 'Yogi Berra', 'Lou Gehrig', 'Babe Ruth', 'Joe DiMaggio']
    
    # Create another list (call it homeRuns) that will consist of the following career home runs that the above New York Yankess names have obtained: 536, 358, 493, 659, 361
    homeRuns = [536, 358, 493, 659, 361]
    
    # Create a string variable (call it playerName) and assign to it the string 'aLeX RoDrIgUeZ'.
    playerName = 'aLeX RoDrIgUeZ'
    
    # Create an integer variable (call it playerHomeRuns) and assign to it the value 351.
    playerHomeRuns = 351
    
    # Create a string variable (call it filePlayers) and assign to it the string 'players.txt'.
    filePlayers = 'players.txt'
    
    # Create a string variable (call it fileHomeRuns) and assign to it the string 'homeruns.txt'.
    fileHomeRuns = 'homeruns.txt'
    
    # Print out the list for players and the list for homeRuns, respectively
    print("players:", players)
    print("homeRuns:", homeRuns)
    
    # Calculate the sum of total home runs from the list homeRuns.  Assign this to a variable called sumHomeRuns and then print it out
    sumHomeRuns = sum(homeRuns)
    print("\nTotal home runs:", format(sumHomeRuns, ","))
    
    # Calculate the average home runs and assign this to a variable called averageHomeRuns and then print it out
    averageHomeRuns = sumHomeRuns / len(homeRuns)
    print("Average home runs:", format(averageHomeRuns, ".2f"))
    
    # Determine who had the highest career home runs.  Assign their career home runs to a variable called maxHomeRuns and the player's name to a variable called maxHomeRunsName.  Print out both of these items, respectively
    maxHomeRuns = max(homeRuns)
    maxHomeRunsName = players[homeRuns.index(maxHomeRuns)]
    print("Max home runs:", maxHomeRuns, "made by:", maxHomeRunsName)
    
    # Determine who had the lowest career home runs.  Assign their career home runs to a variable called minHomeRuns and the player's name to a variable called minHomeRunsName.  Print out both of these items, respectively
    minHomeRuns = min(homeRuns)
    minHomeRunsName = players[homeRuns.index(minHomeRuns)]
    print("Min home runs:", minHomeRuns, "made by:", minHomeRunsName)
    
    # Add to the end of the appropriate lists the variable playerName and the variable playerHomeRuns, respectively.
    players.append(playerName)
    homeRuns.append(playerHomeRuns)
    
    # Print out the list for players and the list for homeRuns, respectively
    print("\nUpdated players:", players)
    print("Updated home runs:", homeRuns)
    
    # Extract out the very last player in the list players and assign it to the variable aPlayer.  Split the contents of the variable aPlayer and assign it to the variable fullName
    aPlayer = players[-1]
    fullName = aPlayer.split()
    
    # Using the variable fullName, convert the first name of this player to upper case and assign it to a variable called firstName.
    firstName = fullName[0].upper()
     
    # Again, using the variable fullName now convert the last name of this player to lower case and assign it to a variable called lastName
    lastName = fullName[1].lower()
    
    # Using both variables firstName and lastName update the list players so that the very last player's name shows this modification
    players[-1] = firstName + " " + lastName
    
    # Print out the list for players and the list for homeRuns, respectively. The last player's name should now have their first name all in upper case and their last name all in lower case
    print("\nplayers: ", players)
    print("home runs:", homeRuns)
    
    # At this point, now your main function should call two functions described
    writeToFiles(players, filePlayers, homeRuns, fileHomeRuns)
    goodBye()

# Call a function called writeToFiles() that will send four arguments to it: players, filePlayers, homeRuns, fileHomeRuns.  
# This function will not return anything.  This function will need to open the appropriate file so that all of the names from 
# the list players can be written to it and all of the home runs from the list homeRuns can be written to it.
def writeToFiles(players, filePlayers, homeRuns, fileHomeRuns):
    # Open the file for players
    with open(filePlayers, 'w') as f:
        # Write each player to the file
        for player in players:
            f.write(player + '\n')
    
    # Open the file for home runs
    with open(fileHomeRuns, 'w') as f:
        # Write each home run to the file
        for homeRun in homeRuns:
            f.write(str(homeRun) + '\n')

# Finally, the other function that will be called is goodBye() that will print out the last two lines of our program that we always end our program.
def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")

# Call the main function to start the program
main()