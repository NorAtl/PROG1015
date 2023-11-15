# Calculate the Average
# Write a program that calculates the average of a list of numbers.
# Ask the user to input the numbers and display the average to the user.

def main():
    print('\nWelcome to the Average Calculator\n')

    # create and initialize an empty list
    numbers = []# [] -> empty list

    # create an accumulator variable 
    sum_numbers = 0

    # get homw many number the usert is going to enter
    list_length = int(input("How many numbers would you like to enter? "))

    # check if number entered is greater than zero to avoid errors
    if list_length != 0:
        # loop to ask for user input (numbers)
        for step in range(list_length): #[0,1,...,list_length-1]        
            input_number = int(input("Enter a number: "))
            # adds the number entered by the user to the numbers list
            numbers.append(input_number)
            # adding each list element at a time to sum_numbers variable
            sum_numbers += input_number #sum_numbers = sum_numbers + input_number
        
        # calculate the average    
        # average = sum(numbers)/list_length #sum function returns the sum of all elements in the given list
        average = sum_numbers/len(numbers) # average = sum/list_length
        
        # output the average to the user
        print(f"The average is {average}")
    else:
        print('I cannot create this list. Enter a number greater than ZERO')   
    

if __name__ == "__main__":
    main()