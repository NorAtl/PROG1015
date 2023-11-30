import csv

def choose_option(options, category):
    while True:
        try:
            choice = int(input(f"Enter choice (1-{len(options)}) for {category}: "))
            if 1 <= choice <= len(options):
                chosen_option = options[choice - 1].upper()
                print(f"You chose: {chosen_option}")
                return chosen_option
        except ValueError:
            pass

def main():
    with open("P2 - Aardvark/the_choices_file.csv", "r") as my_csv_file:
        lines = list(csv.reader(my_csv_file))

    categories = ["an animal name", "an action word", "an adjective", "another action word", "a noun", "yet another action word", "an adverb"]
    choices = {}
    
    counter = 1  # Initialize a counter variable

    for category in categories:
        options = lines[counter - 1][1:]
        print(f"\nPlease choose {category}:\n" + "\n".join(f"{j} {opt}" for j, opt in zip(range(1, len(options) + 1), options)))
        choices[category] = choose_option(options, category)
        counter += 1  # Increment the counter

    print("\nYour Completed Story:\n")
    print(f"\tThe itsy bitsy {choices['an animal name']} {choices['an action word']} up the {choices['an adjective']} spout.")
    print(f"\tDown came the rain and {choices['another action word']} the {choices['an animal name']} out.")
    print(f"\tOut came the {choices['a noun']} and {choices['yet another action word']} up all the rain.")
    print(f"\tSo the itsy bitsy {choices['an animal name']} went {choices['an adverb']} insane.\n")

if __name__ == "__main__":
    main()
