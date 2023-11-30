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
    file_name = "P2 - Aardvark/the_choices_file.csv"

    with open(file_name, "r") as my_csv_file:
        lines = list(csv.reader(my_csv_file))

    categories = ["animal", "action1", "adjective", "action2", "noun", "action3", "adverb"]

    choices = {}
    
    for i, category in enumerate(categories):
        options = lines[i][1:]
        print(f"\nPlease choose a {category}:\n" + "\n".join(f"{j} {opt}" for j, opt in enumerate(options, 1)))
        choices[category] = choose_option(options, category)

    print("\nYour Completed Story:\n")
    print(f"\tThe itsy bitsy {choices['animal']} {choices['action1']} up the {choices['adjective']} spout.")
    print(f"\tDown came the rain and {choices['action2']} the {choices['animal']} out.")
    print(f"\tOut came the {choices['noun']} and {choices['action3']} up all the rain.")
    print(f"\tSo the itsy bitsy {choices['animal']} went {choices['adverb']} insane.\n")

if __name__ == "__main__":
    main()
