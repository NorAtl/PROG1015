def main():#don't change this line
    # Your code should START here

    
    print("\tWelcome to Team win Percentage Calculator")
    
   
    teamName = (input("\nWhat is the team's name?"))    
    gamesWon = int(input("How many games did the team win?"))
    gamesLost = int(input("How many games did the team lose?"))

    gamesPlayed = gamesWon + gamesLost
    winPercent = gamesWon / gamesPlayed * 100

    print("(teamName)'s win percentage is {:.f}".format(winPercent))
       


    # Your code should END here

if __name__ == "__main__": #don't change this line
    main()                  #don't change this line