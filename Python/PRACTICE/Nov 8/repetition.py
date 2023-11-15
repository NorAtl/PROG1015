import turtle

def drawLine():
    turtle.forward(100)
    turtle.right(90)

def main():
    numberOfSides = int(input("\nEnter the number of sides: "))
    
    for steps in range(numberOfSides): #0,1,2,3
        turtle.forward(100)
        turtle.right(360/numberOfSides)
        for steps in range(numberOfSides): #0,1,2,3
            turtle.forward(50)
            turtle.right(360/numberOfSides)
    
    
    # for x in range(4):
    #     drawLine()

    # drawLine()
    # drawLine()
    # drawLine()
    # drawLine()

    # turtle.forward(100)
    # turtle.right(90)
    # turtle.forward(100)
    # turtle.right(90)
    # turtle.forward(100)
    # turtle.right(90)
    # turtle.forward(100)
    # turtle.right(90)



    turtle.done()
    

if __name__ == "__main__":
    main()