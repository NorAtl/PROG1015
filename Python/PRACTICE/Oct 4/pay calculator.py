#Don't forget to rename this file after copying the template
#for a new program!
# """
# Student Name:    
# Program Title:  
# Description:    
# """

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

# Write a program that takes two pieces of input data 
#  a pay rate per hour and the number of hours worked – and output the total pay. 
# Any hours over 40 are paid at time and a half.


    print("Pay Calculator")
          
    hourlyRate = float(input("Enter your hourly wage: "))
    hoursWorked = float(input("Enter the number of hours you worked: "))

    if hoursWorked <= 40: 
        regHours = hoursWorked
        otHours = 0
    

    if hoursWorked > 40: 
        regHours = 40
        otHours = hoursWorked - 40

    regPay = regHours * hourlyRate
    otPay = otHours * hourlyRate * 1.5
    totPay = regPay + otPay

    print(f"Overtime hours worked: {otHours:.2f}")

    print(f"Your regular pay is: ${regPay:.2f}")
    print(f"Your overtime pay is: ${otPay:.2f}")
    print(f"Your total pay is: ${totPay:.2f}")

    


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()