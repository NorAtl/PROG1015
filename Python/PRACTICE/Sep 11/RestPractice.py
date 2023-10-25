
# Student Name:    
# Program Title:  
# Description:    
# """

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    percentage = int(input("percent of restaraunts that are pizzarias "))
    pizzarias = int(input("number of pizzarias in the US "))

    totalRestaurants = pizzarias / (percentage * .01)

    print("The total number of restaurants in the US is " + str(int(totalRestaurants)))




    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()