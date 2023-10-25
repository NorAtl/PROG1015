# Author: 
# Date: 
# Description: 

def main():
    
    print("\nWelcome to the Paint Shop!")
    print("*This program will help you calculate how many cans of paint that you will need to paint a rectangular room, based in its dimensions.\n")

    length = int(input("How long is your room in feet?"))
    width = int(input("How wide is your room in feet?"))
    height = int(input("How tall is your room in feet?"))

    totalWallArea = length * height * 2 + width * height * 2

    paintNeeded = totalWallArea / 150

    # print(f"\n\t*The win percentage for the {teamName} is {winPercent:.2f}%")
    print(f"\tThe total wall area of your room is {totalWallArea} square feet.")
    print(f"\n\t You will need {paintNeeded:.2f} gallon(s) of paint")
    
    print("\nHappy Painting!\n")


if __name__ == "__main__":
    main()
