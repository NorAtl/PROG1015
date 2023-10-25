"""
Student Name:  Delano Marques
Program Title:  Energy Calculator - BROKEN
Description:   Debugging practice
"""

def main(): #<-- Don't change this line!
    
    print("Energy Calculator")
    print("\nThis program will calculate how much you pay for electricity for")
    print("a particular device, based on the wattage of the device and how")
    print("many hours the device was in use.")
    print("\nCalculations are based on a cost of 12.65 cents per kiloWatt hour.")

    kwhPrice = 12.65
    avgDaysInAMonth = 30.42
    monthsInYear = 12

    deviceWattage = float(input("\nEnter the wattage of the device: ")) #check
    hoursUsedPerDay = float(input("Enter how many hours per day the device is in use: ")) #check

    costPerHour = ((deviceWattage / 1000) * kwhPrice) #BUG deviceWattage should be divided by 1000 not 100 #BUG does not need to be divided again
    costPerDay = hoursUsedPerDay * costPerHour #BUG hoursUsedPerDay must be multiplied by costPerHour
    costPerMonth = avgDaysInAMonth * costPerDay # BUG removed [* 60]: not needed
    kwhPerDay = (deviceWattage /1000) * hoursUsedPerDay #check

    print("\nElectrical cost for a device using {:.2f} watts for {} hour per day:".format(deviceWattage, hoursUsedPerDay)) #BUG replaced 2nd deviceWattage with hoursUsedPerDay
    print("\tCost Per Hour:\t${:.4f}".format(costPerHour / 100)) #BUG /100 to convert from cents to dollars #BUG changed .1f to.4f 
    print("\tCost Per Day:\t${:.4f}".format(costPerDay / 100)) #BUG /100 to convert from cents to dollars 
    print("\tCost Per Month:\t${:.4f}".format(costPerMonth /100)) #BUG /100 to convert from cents to dollars #BUG changed costPerDay to costPerMonth #BUG changed .5f to.4f 
    print("\tCost Per Year:\t${:.4f}".format(costPerMonth /100 * monthsInYear)) 
    print("\tkWh Per Day:\t{:.4f}".format(kwhPerDay)) #BUG changed .0f to.4f 
    

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()