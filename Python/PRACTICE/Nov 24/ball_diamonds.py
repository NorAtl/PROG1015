import csv

def main():
    file_name = "Ottawa_Ball_Diamonds.csv"
    access_mode = "r"
    user_choice = ""
    valid_options = ['softball', 'baseball', 't-ball']
    is_valid_option = False

    with open(file_name, access_mode) as my_csv_file:
        csv_data = csv.reader(my_csv_file) # returns a csv reader object 
            
        while not is_valid_option:
            user_choice = input("What type of fields do you want to list (softball, baseball, or T-Ball)? ")
            if user_choice not in valid_options:
                print('Enter a valid field type (baseball, softball, or t-ball)')    
            else:
                is_valid_option = True
                for row in csv_data:      
                    if row[3].lower() == user_choice.lower():
                        print(f"Facility ID:{row[2]} \tField Name:{row[5]} ")

    # TODO: add fields count to the output
    # TODO: create a new list/file with the result
if __name__ == "__main__":
    main()