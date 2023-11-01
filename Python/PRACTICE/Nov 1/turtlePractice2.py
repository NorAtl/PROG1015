#Don't forget to rename this file after copying the template
#for a new program!
# """
# Student Name:    
# Program Title:  
# Description:    
# """

import turtle


def main():

    for square in range(4): #[0,1,2,3]
        turtle.forward(100)
        turtle.right(90)
        for square in range(4): #[0,1,2,3]
            turtle.forward(50)
            turtle.right(90)
#these lines will run 4x4=16 times
    turtle.done()



if __name__ == "__main__":
    main()