# Student Name:    Christopher Jones
# Program Title:  Variable Practice
# Description:    
# """

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    message = "Weekly incoMe cAlculator"
   
    #use 'float' instead of 'input'
    salary = float(input("what's your weekly salary?"))    
    bonus = float(input("What's your bonus?"))

    totalpay = salary + bonus
    

    print("The total weekly pay with bonus of  ${:.2f} is ${:.2f}".format(bonus,totalpay) + "!")



    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()