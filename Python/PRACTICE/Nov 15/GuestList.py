



def main(): 

    print('\nWelcome to the Party Guest List Generator\n')

    # create empty list
    guestList = []

    # initialize guestName variable
    guestName = ''
    
    # create a loop to repeate until the user enters 'done'
    while guestName.lower() != 'done':
        # get the guest name entered by the user
        guestName = input('Enter the name of the guest (or "done" to finish): ')
        # add the current guest name to the list
        # if statement to avoid adding done to the list
        if guestName.lower() != 'done':
            guestList.append(guestName)

    # remove the last element in the list (done) instead of using the if statement above
    # del guestList[-1]

    # sort the guest list into alphabetical order
    guestList.sort()

    #output the guest list
    print('\nThe Guest List for your party is: \n')


    for guest in guestList:
        print(guest)







  



  

if __name__ == "__main__":
    main()