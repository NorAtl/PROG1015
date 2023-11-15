import turtle

def main():
    line_length = -1
    line_width = 5
    turtle.width(line_width)
    # Let them specify new lines over and over 
    # until they enter a line length of 0
    while line_length != 0:
        # have the user to enter a pen color
        pen_color = input("Enter a color: ")
        
        # have the user to enter a line length
        line_length = float(input("Enter the line length: "))
        
        # have the user to enter an angle.
        angle = float(input("Enter an angle: "))
        
        #Draw a line based on their specifications
        turtle.color(pen_color)
        turtle.forward(line_length)
        turtle.right(angle)

    turtle.done()
    
    


if __name__ == "__main__":
    main()