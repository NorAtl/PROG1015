

import csv # import the csv module

def main():

    file_name = "P2 - Aardvark/the_choices_file.csv" # point the variable to the csv file
    access_mode = "r" # access mode 'read'

    print("\nThe Itsy Bitsy Aardvark\n\n") # print title
    
    with open(file_name, access_mode) as my_csv_file: # open the file which will be referenced by the my_csv_file variable
        csv_data = csv.reader(my_csv_file) # uses the csv module to read the data 
        lines = list(csv_data) # creates the 'lines' list using csv_data



    print("Please choose an animal:") 

    animalOptions = lines[0][1:] # defines the variable as referenceing the first line, second element
    
    for i in range(len(animalOptions)): 
        print(f"{i + 1} {animalOptions[i]}") # prints each element from the line on its own line. As each line is printed
                                             # it advances to the next line
    
    while True: # starting a 'while' loop
        try: #checking to see if the user-entered variable is valid
            animalChoice = int(input("Enter choice (1-5): "))
            if 1 <= animalChoice <= len(animalOptions):
                chosenAnimal = animalOptions[animalChoice - 1].upper()
                print(f"You chose: {chosenAnimal}") # do this if the entry is valid
                break  # Break out of the loop if a valid choice is made
        except ValueError:
            pass  # Do nothing if the input is not a valid integer



    print("\nPlease choose an action:")

    actionOptions = lines[1][1:] # defines the variable as referencing the second line, second element
    
    for i in range(len(actionOptions)):
        print(f"{i + 1} {actionOptions[i]}")

    while True:
        try:
            actionChoice = int(input("Enter choice (1-5): "))
            if 1 <= actionChoice <= len(actionOptions):
                chosenAction = actionOptions[actionChoice - 1].upper()
                print(f"You chose: {chosenAction}")
                break  
        except ValueError:
            pass  



    print("\nPlease choose an adjective:")

    adjOptions = lines[2][1:] # defines the variable as referencing the third line, second element
    
    for i in range(len(adjOptions)):
        print(f"{i + 1} {adjOptions[i]}")

    while True:
        try:
            adjChoice = int(input("Enter choice (1-5): "))
            if 1 <= adjChoice <= len(adjOptions):
                chosenAdj = adjOptions[adjChoice - 1].upper()
                print(f"You chose: {chosenAdj}")
                break  
        except ValueError:
            pass  

    

    print("\nPlease choose another action:")

    actionOptions2 = lines[3][1:] # defines the variable as referenceing the fourth line, second element
    
    for i in range(len(actionOptions2)):
        print(f"{i + 1} {actionOptions2[i]}")

    while True:
        try:
            actionChoice2 = int(input("Enter choice (1-5): "))
            if 1 <= actionChoice2 <= len(actionOptions2):
                chosenAction2 = actionOptions2[actionChoice2 - 1].upper()
                print(f"You chose: {chosenAction2}")
                break  
        except ValueError:
            pass  




    print("\nPlease choose a noun:")

    nounOptions = lines[4][1:] # defines the variable as referencing the fifth line, second element
    
    for i in range(len(nounOptions)):
        print(f"{i + 1} {nounOptions[i]}")

    
    while True:
        try:
            nounChoice = int(input("Enter choice (1-5): "))
            if 1 <= nounChoice <= len(nounOptions):
                chosenNoun = nounOptions[nounChoice - 1].upper()
                print(f"You chose: {nounChoice}")
                break  
        except ValueError:
            pass  



    print("\nPlease choose another action:")

    actionOptions3 = lines[5][1:] # defines the variable as referencing the sixth line, second element
    
    for i in range(len(actionOptions3)):
        print(f"{i + 1} {actionOptions3[i]}")

    while True:
        try:
            actionChoice3 = int(input("Enter choice (1-5): "))
            if 1 <= actionChoice3 <= len(actionOptions3):
                chosenAction3 = actionOptions3[actionChoice3 - 1].upper()
                print(f"You chose: {chosenAction3}")
                break  
        except ValueError:
            pass  



    print("\nPlease choose an adjective:")

    advOptions = lines[6][1:] # defines the variable as referencing the seventh line, second element
    
    for i in range(len(advOptions)):
        print(f"{i + 1} {advOptions[i]}")

    while True:
        try:
            advChoice = int(input("Enter choice (1-5): "))
            if 1 <= advChoice <= len(advOptions):
                chosenAdv = advOptions[advChoice - 1].upper()
                print(f"You chose: {chosenAdv}")
                break  
        except ValueError:
            pass  



    # print the story with the user chosen varibles inserted
    print("\nYour Completed Story:\n")
    print(f"\tThe itsy bitsy {chosenAnimal} {chosenAction} up the {chosenAdj} spout.")
    print(f"\tDown came the rain and {chosenAction2} the {chosenAnimal} out.")
    print((f"\tOut came the {chosenNoun} and {chosenAction3} up all the rain."))
    print(f"\tSo the itsy bitsy {chosenAnimal} went {chosenAdv} insane.\n")


if __name__ == "__main__":
    main()