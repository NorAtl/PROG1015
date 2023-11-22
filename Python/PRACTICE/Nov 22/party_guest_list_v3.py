# Party Guest List 
# Ask the user to enter the names of everyone attending to a party.
# Then return a list of the party guests in alphabetical order.

def main():
    # create an empty guests name list
    guests_name_list = []
    # create an empty guests age list
    guests_age_list = []

    # initilize guest_name variable
    guest_name = ""
    # initilize age numeric variable 
    guest_age = 0
    # initialize age string variable to hold user input
    guest_age_string =""

    # create a loop to repeat name input until user enters 'done'
    while guest_name.lower() != 'done':
        # getting the guest name entered by the user
        guest_name = input("Enter the name of the guest (or 'done' to finish): ")        
        
        #if statement to avoid adding 'done' to the list        
        if guest_name.lower() != 'done':            

            # adding the current guest name to the list
            guests_name_list.append(guest_name)
            
            while not guest_age_string.isdigit():
                # getting the guest age entered by the user
                guest_age_string = input("Enter guest's age: ")
                # catch exceptions
                try:
                    guest_age = int(guest_age_string)                
                    # adding the current guest age to the list
                    guests_age_list.append(guest_age)
                except ValueError:
                    print("Invalid age. Please enter a number.")
            
            # reset variable after a valid input
            guest_age_string = ""
            

    file_name = "party_guests_list?.csv"
    access_mode = 'w'

    try:
        # creating a file
        partyGuestsFile = open(file_name, access_mode)

        # for loop to go through list and add guests to file
        for guest_index in range(len(guests_name_list)): #range -> [0,1,..,guests_name_list length -1]
            partyGuestsFile.write(f"{guests_name_list[guest_index]}, {guests_age_list[guest_index]}\n")

        # close the file
        partyGuestsFile.close()
    except Exception as e:
        print(f"An error occured while writing to the file. \nError: {e}")
    else:
        print("Guests saved to the list file...")

if __name__ == "__main__":
    main()