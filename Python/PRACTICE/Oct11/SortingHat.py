#Don't forget to rename this file after copying the template
#for a new program!
# """
# Student Name:    
# Program Title:  
# Description:    
# """

import random
def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

#generate a random number between 1 and 2
    randomNumber = random.randint(1,4)

    if randomNumber == 1:
        print("You are assigned to Gryffindor")
    elif randomNumber == 2:
        print("You are assigned to Hufflepuff")
    elif randomNumber == 3:
        print("You are assigned to Ravenclaw")
    elif randomNumber == 4:
        print("You are assigned to Slytherin")
    
    print("Have a great day!")



    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()