#Don't forget to rename this file after copying the template
#for a new program!
# """
# Student Name:    
# Program Title:  
# Description:    
# """

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    answer = int(input('Guess a number from 1-10: '))
    
    if answer == int('7'):
        print('Great guess. You are correct!')
    if answer > int('7'):
            print('Too high. Guess again!')
    if answer < int('7'):
            print('Too low. Guess again!')
    print('Thank you for playing!')
    

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()