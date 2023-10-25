
# Student Name:    Christopher jones
# Program Title:  Landscape Calculator
# Description:    calculates the cost of landscaping
# """

def main(): 
#inputs: address, plot length, plot width, type of grass, and number of trees.
    #base labour charge: $1000
    #if surface is > 5000 sqft, add $500
    #cost/sqft:
        #fescue $.05
        #bentgrass $.02
        #campus $.01
    #cost/tree = $100

    print('\nLandscape Calculator')

    address = float(input("Please enter the house number: "))
    length = float(input("Please enter the length of the property in feet: "))
    width = float(input("Please enter the width of the property in feet: "))
    area = length * width
    
    if area > 5000:
        print('*There is an added charge of $500 for properties over 500 sqft.')

    print('\nPlease choose from the following grass types: \n\tfescue at $.05/sqft, or \n\tbentgrass at $.02/sqft, or \n\tcampus at $.01/sqft\n')
    grass = str.lower(input('What type of grass would you like?: '))

    grassCost = 0
    if grass == 'fescue':
        grassCost = .05
    elif grass == 'bentgrass':
        grassCost = .02
    elif grass == 'campus':
        grassCost = .01
    else:
        print('You entered an invalid grass type. Please try again.')
        exit()

    if area > 5000:
        grassCostTot = area * grassCost + 500
    elif area <= 5000:
        grassCostTot = area * grassCost
    

    trees = int(input('Please enter the number of trees that you would like: '))

    treeCost = trees * 100

    totCost = 1000 + grassCostTot + treeCost

    print('\nHere is your final estimate: ')
    print('\tBase Labour Charge: $1000.00')
    print(f'\tGrass: ${grassCostTot:.2f}')
    print(f'\tTrees: ${treeCost:.2f}')
    print(f'Your total cost for house {address:.0f} is: ${totCost:.2f}\n')
    
       
if __name__ == "__main__":
    main()