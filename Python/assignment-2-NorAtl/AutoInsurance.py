
# Student Name:   Christopher Jones 
# Program Title:  Auto Insurance
# Description:    Compute monthly insurance cost
# """ ready for grading

def main(): 

    print('\nAuto Insurance calculator\n')

    sex = input('Are you "male" or "female"? ').lower()

    if sex != 'male' and sex != 'female':
            
    



    age = float(input('Please enter your age in years: '))

    if age < 15:
        print('You are to young to be insured.')
        exit()
    elif age >= 70:
        print('You are too old to be insured.')
        exit()

    autoPrice = float(input('Please enter the purchase price of the vehicle in dollars: '))

    if sex == 'male':
        if age >= 15 and age < 25:
            insCost = autoPrice * .25 / 12
        elif age >= 25 and age < 40:
            insCost = autoPrice * .17 / 12
        elif age >= 40 and age < 70:
            insCost = autoPrice * .10 / 12      

    elif sex == 'female':
        if age >= 15 and age < 25:
            insCost = autoPrice * .20 / 12
        elif age >= 25 and age < 40:
            insCost = autoPrice * .15 / 12
        elif age >= 40 and age < 70:
            insCost = autoPrice * .10 / 12  

    

    print(f'\nYour monthly insurance cost will be ${insCost:.2f}\n')





if __name__ == "__main__":
    main()