def main():#don't change this line
    # Your code should START here

    
    print("\n\n\tWelcome to Team win Percentage Calculator")
    
   
    teamName = (input("\nWhat is the team's name?"))    
    gamesWon = int(input("How many games did the team win?"))
    gamesLost = int(input("How many games did the team lose?"))

    gamesPlayed = gamesWon + gamesLost
    winPercent = gamesWon / gamesPlayed * 100

    #there are two formatting options below
    print ("\n*The win percentage for the {} is {:.2f}%".format(teamName,winPercent))
    print(f"\n\t*The win percentage for the {teamName} is {winPercent:.2f}%")
    


       


    # Your code should END here

if __name__ == "__main__": #don't change this line
    main()                  #don't change this line