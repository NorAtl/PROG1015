#Don't forget to rename this file after copying the template
#for a new program!
# """
# Student Name:    
# Program Title:  
# Description:    
# """ comment
#determine if an inputted year is a leap year
#leap year == divisible by 4 but not 100

    

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    print('\nLeap Year calculator\n')

    year = int(input('Please enter a year: '))

    if year/4 == int(year/4) and year/100 != int(year/100):
        print('This is a leap year.')
    else: 
        print('This is not a leap year.')


  



    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()