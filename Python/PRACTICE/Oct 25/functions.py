#Don't forget to rename this file after copying the template
#for a new program!
# """
# Student Name:    
# Program Title:  
# Description:    
# """ comment

def printMessage():#function definition
    print('Hello World')
    return

def sayHello(in_name):
    print(f"Hello, {in_name}!")

def addNumbers(in_num1, in_num2):
    sum = in_num1 + in_num2
    return sum
    # return sum = in_num1 + in_num2
    

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    printMessage() #function call
    printMessage() #function call
    printMessage() #function call

    sayHello("John")

    sayHello("Jane")

    sayHello("Chris")

    name = input("What's your name? ")

    sayHello(name)

    total = addNumbers(3,6) #9

    print(total)
    
            
        
            






    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()