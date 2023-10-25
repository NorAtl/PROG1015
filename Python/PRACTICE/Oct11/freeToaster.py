#Don't forget to rename this file after copying the template
#for a new program!
# """
# Student Name:    
# Program Title:  
# Description:    
# """

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    free_toaster = False
    deposit = input("How much would you like to deposit?")
    if float(deposit) > 100:
        free_toaster = True
    if free_toaster:
        print("Enjoy your new toaster!")
    print("Have a nice day!")



    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()