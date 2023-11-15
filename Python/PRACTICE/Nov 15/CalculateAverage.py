


def main(): 

    print('\nWelcome to the average Calculator\n')

    #initialize an empty list
    numbers = []

    # create an accumulator variable
    sum_numbers = 0

    # ask how many numbers the user is going to enter
    list_length = int(input('How many numbers would you like to enter? '))

    # loop to ask for user input
    for step in range(list_length):
        input_number = int(input('Enter a number: '))
        # add the number entered by the user to the list
        numbers.append(input_number)
        # add each element to a total as they are entered
        sum_numbers += input_number   # sum_numbers = sum_numbers + input_number

    # calculate the average
    average = sum(numbers)/len(numbers)
        # average = sum_numbers/list_length 
        # sum_numbers/len(numbers)

    print(f'The average is: {average}')

    
  
if __name__ == "__main__":
    main()