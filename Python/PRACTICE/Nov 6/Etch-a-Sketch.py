
import turtle


def main(): 
    length = 1

    while length != 0:
        length = int(input('Please enter line length: '))
        if length == 0:
            print('Game Over')
        angle = int(input('Please enter how many dgrees you would like to turn to the right: '))
        turtle.right(angle)
        colour = input('Please enter a colour: ')
        turtle.color (colour)
        turtle.forward(length)

    turtle.done()
    


    
    
    
    
    
if __name__ == "__main__":
    main()