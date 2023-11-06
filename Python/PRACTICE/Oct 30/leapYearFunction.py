#Don't forget to rename this file after copying the template
#for a new program!
# """
# Student Name:    
# Program Title:  
# Description:    
# """ comment
#determine if an inputted year is a leap year
#leap year == divisible by 4 but not 100

def checkLeapYear(in_year):
    return(in_year % 4 == 0 and in_year % 100 != 0)or(in_year % 400 == 0)

# Another way to do it:
# def checkLeapYear(in_year):
#     isLeapYear = False
#     if(in_year % 4 == 0 and in_year % 100 != 0)or(in_year % 400 == 0):
#         isLeapYear = True
#     return isLeapYear

def main():

    print('\nLeap Year calculator\n')
    year = int(input('Please enter a year: '))

    if checkLeapYear(year):
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')

# Without using a function:
#    if year/4 == int(year/4) and year/100 != int(year/100):
#        print('This is a leap year.')
#    else: 
#        print('This is not a leap year.')
#
# Another way to write this is:
#   if (year % 4 == 0 and year % 100 !+ 0) or (year % 400 == 0):
#       print('This is a leap year.')
#    else: 
#        print('This is not a leap year.')
  
if __name__ == "__main__":
    main()