# Party Guest List 
# Ask the user to enter the names of everyone attending to a party.
# Then return a list of the party guests in alphabetical order.

def main():

    file_name = 'Python/PRACTICE/Nov 20/PartyGuests.csv' # copy relative path # remember to use forward slashes
    access_mode = 'w'

    PartyGuests = open(file_name, access_mode)



    # create an empty guests list
    guests_name_list = []
    guests_age_list = []
    # initilize guest_name variable
    guest_name = ""
    guest_age = 0

    # create a loop to repeat name input until user enters 'done'
    while guest_name.lower() != 'done':
        # getting the guest name entered by the user
        guest_name = input("Enter the name of the guest (or 'done' to finish): ")
                
        #if statement to avoid adding 'done' to the list        
        if guest_name.lower() != 'done':
            # adding the current guest name to the list
            guests_name_list.append(guest_name)
            guest_age = input("Enter the age of the guest: ")
            guests_age_list.append(guest_age)


    # remove the last element in my list ('done')  - in case there's no if statement inside the loop
    # del guests_list[-1]


    # output the guests list
    PartyGuests.write("\nThe Guest list of your party is:\n")



    for guest_index in range(len(guests_name_list)):
        PartyGuests.write(f'{guests_name_list[guest_index]}, {guests_age_list[guest_index]}\n')

    PartyGuests.close


if __name__ == "__main__":
    main()