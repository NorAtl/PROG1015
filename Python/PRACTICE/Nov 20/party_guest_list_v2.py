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
    # initilize guest_age variable
    guest_age = 0

    # create a loop to repeat name input until user enters 'done'
    while guest_name.lower() != 'done':
        # getting the guest name entered by the user
        guest_name = input("Enter the name of the guest (or 'done' to finish): ")        
        
        #if statement to avoid adding 'done' to the list        
        if guest_name.lower() != 'done':
            # getting the guest age entered by the user
            guest_age = int(input("Enter guest's age: "))
            # adding the current guest name to the list
            guests_name_list.append(guest_name)
            # adding the current guest age to the list
            guests_age_list.append(guest_age)

    file_name = "demos/nov20/party_guests_list.csv"
    access_mode = 'w'

    # creating a file
    partyGuestsFile = open(file_name, access_mode)

    # for loop to go through list and add guests to file
    for guest_index in range(len(guests_name_list)): #range -> [0,1,..,guests_name_list length -1]
        partyGuestsFile.write(f"{guests_name_list[guest_index]}, {guests_age_list[guest_index]}\n")

    # close the file
    partyGuestsFile.close()

if __name__ == "__main__":
    main()