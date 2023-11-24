

import csv

def main(): 

    file_name = "guests.csv"
    access_mode = "r"
    
    with open(file_name, access_mode) as my_csv_file:
        csv_data = csv.reader(my_csv_file) # returns a csv reader object object
        # print(csv_data)
        print("Name\tAge")
        for row in csv_data:
            # print(row)
            # for item in row:
            #     print(item,end=" ")
            # print(" - ".join(row)) # join the content of row and separate it using a comma
            # print(f"Name: {row[0]}, Age: {row[1]}")
            print(f"{row[0]}\t{row[1]}")
            

    

if __name__ == "__main__":
    main()