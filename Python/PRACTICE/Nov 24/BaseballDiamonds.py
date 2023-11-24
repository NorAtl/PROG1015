

import csv

def main(): 

    file_name = "Ottawa_Ball_Diamonds.csv"
    access_mode = "r"
        
    valid_option = ['softball', 'baseball','t-ball']
    is_valid_option = False


    with open(file_name, access_mode) as my_csv_file:
        csv_data = csv.reader(my_csv_file) # returns a csv reader object object

        while not is_valid_option:
            diamond_type = input("What type of field do you want to list? You can pick either 'softball', 'baseball', or 't-ball': ") 
            if diamond_type not in valid_option:
                print("Please enter 'softball', 'baseball', or 't-ball'")

            else:                 
                is_valid_option = True
                for row in csv_data:
                    if row[3].lower() == diamond_type.lower():
                        # print(f"All the {diamond_type} fields are:\n")
                        print(f"Facility ID: {row[2]}\tField Name: {row[6]}")
                

    

if __name__ == "__main__":
    main()