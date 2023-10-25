#Don't forget to rename this file after copying the template
#for a new program!
# """
# Student Name:    
# Program Title:  
# Description:    
# """

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    purch = float(input("How much is the total of you purchase?"))
    if purch > 50:
        print('Your shipping is free!')
        print(f"Yout total is: ${purch:.2f}")
    elif purch <= 50:
        print('Please include $10 for shipping')
        totPurch = purch + 10
        print(f"Your total is: ${totPurch:.2f}")
    print('Have a nice day!')

            
        
            






    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()