import csv  # import the csv module to read and write csv files

# define the function that will be used in the program to get inputs from the user.
def get_user_choice(options, category):  # 2 parameters, options and category (of options)
    while True:  # keeps running the loop until a valid choice is made
        try:
            choice = int(input(f"Enter choice (1-{len(options)} for {category}): "))
            if 1 <= choice <= len(options):
                chosen_option = options[choice - 1].upper()
                print(f"You chose: {chosen_option}")  # what to do when a valid option is chosen
                return chosen_option
        except ValueError:  # what to do when a valid option is not chosen.
            pass

def main():  # begin code for the main program
    file_name = "P2 - Aardvark/the_choices_file.csv"  # pointing to the file the program is referencing
    access_mode = "r"  # access the program in 'read' mode

    print("\nThe Itsy Bitsy Aardvark\n\n")

    with open(file_name, access_mode) as my_csv_file:  # opening the csv file as specified above
        csv_data = csv.reader(my_csv_file)  # uses the csv module to read the data
        lines = list(csv_data)  # creates the 'lines' list using csv_data

    
    categories = ["animal", "action", "adjective", "action", "noun", "action", "adverb"]
    choices = {}  # initialize the variable where the user's choices will be stored.

    # loop through the categories and get input for each one.
    for i in range(1, len(lines)):  
        category = categories[i - 1]
        options = lines[i][1:]

        # list the options for each category and prompt the user to enter a choice
        print(f"\nPlease choose a {category}:")

        for j in range(1, len(options) + 1):
            print(f"{j} {options[j - 1]}")

        # store the user's choices for each category
        chosen_option = get_user_choice(options, category)
        choices[category] = chosen_option

    # print the story with the user-chosen variables inserted
    print("\nYour Completed Story:\n")
    print(f"\tThe itsy bitsy {choices['animal']} {choices['action']} up the {choices['adjective']} spout.")
    print(f"\tDown came the rain and {choices['action']} the {choices['animal']} out.")
    print(f"\tOut came the {choices['noun']} and {choices['action']} up all the rain.")  
    print(f"\tSo the itsy bitsy {choices['animal']} went {choices['adverb']} insane.\n")

if __name__ == "__main__":
    main()

