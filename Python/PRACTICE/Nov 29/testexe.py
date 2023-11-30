

# to fancy up the output
import time 
def slow_print(message, delay=0.1):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()




def choose_option(options, category): # 2 parameters, options and category (of options)
    while True: # keeps running the loop until a valid choice is made
        try:
            choice = int(input(f"Enter choice (1-{len(options)}) for {category}: "))
            if 1 <= choice <= len(options):
                chosen_option = options[choice - 1].upper()
                print(f"You chose: {chosen_option}") # what to do when a valid option is chosen
                return chosen_option
        except ValueError:
            pass   # what to do when a valid option is not chosen.

 # begin code for the main program
def main():
    
    print("\nThe Itsy Bitsy Aardvark")

    # open the csv file the program is referencing in read mode
    with open("P2 - Aardvark/the_choices_file.csv", "r") as my_csv_file:
        # use the csv module to read the data and create the 'lines' list
        lines = list(csv.reader(my_csv_file))

    # make a list of the various categories
    categories = ["an animal name", "an action word", "an adjective", "another action word", "a noun", "yet another action word", "an adverb"]
    choices = {} # initialize the variable where the user's choices will be stored.
    
    counter = 1  # Initialize a counter variable

    # loop through the categories and get input for each one.
    for category in categories: #goes through each category in the categories list above
        options = lines[counter - 1][1:] # indexes the correct line and skips the first element in the line
        # print the available options the user can coose from
        print(f"\nPlease choose {category}:\n" + "\n".join(f"{j} {opt}" for j, opt in zip(range(1, len(options) + 1), options)))
        choices[category] = choose_option(options, category) # store the user's choices for each category
        counter += 1  # increases the counter by one

    # get a little fancy with printing the results by making the user wait
    time.sleep(1.5)
    print("\nWait for it...")
    time.sleep(1.5)
    print("\nKeep waiting...")
    time.sleep(1.5)
    print("\nIt's almost ready!")
    time.sleep(1.5)

    
    # print the story with the user-chosen variables inserted
    slow_print("\nHere's your Completed Story:\n")
    slow_print(f"\tThe itsy bitsy {choices['an animal name']} {choices['an action word']} up the {choices['an adjective']} spout.")
    slow_print(f"\tDown came the rain and {choices['another action word']} the {choices['an animal name']} out.")
    slow_print(f"\tOut came the {choices['a noun']} and {choices['yet another action word']} up all the rain.")
    slow_print(f"\tSo the itsy bitsy {choices['an animal name']} went {choices['an adverb']} insane.\n")

    print("Wasn't that fun?!?\n")
if __name__ == "__main__":
    main()
