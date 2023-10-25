#Don't forget to rename this file after copying the template
#for a new program!
# """
# Student Name:    Christopher Jones
# Program Title:  Erewhon Mobile Data Plans
# Description:    calculates mobile data usage cost
# """

def main():
#Enter Mb of data used
#if in bottom or top brracket enter flat rate
#If in one of the middle brackets, multiply data by rate to get charge

    print('Erewhon Mobile Data Plans')
    print('Data Usage Charge Calculator\n')

    dataUsed = int(input('Please enter the amount of data you used this month in Mb: '))

    if dataUsed <= 200:
        fee = 20
    elif dataUsed > 200 and dataUsed <= 500:
        fee = dataUsed * 0.105
    elif dataUsed > 500 and dataUsed <= 1000:
        fee = dataUsed * 0.110
    elif dataUsed > 1000:
        fee = 118

    print(f'\nThe total charge for your data usage is: ${fee:.2f}')


if __name__ == "__main__":
    main()