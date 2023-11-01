#Don't forget to rename this file after copying the template
#for a new program!
# """
# Student Name:    
# Program Title:  
# Description:    
# """

import turtle


def main():

    numberofsides = 6

    for square in range(numberofsides):
        turtle.forward(100)
        turtle.right(360/numberofsides)
        for square in range(numberofsides): 
            turtle.forward(50)
            turtle.right(360/numberofsides)
    turtle.done()




if __name__ == "__main__":
    main()