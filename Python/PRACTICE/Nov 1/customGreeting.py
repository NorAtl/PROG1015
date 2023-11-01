#Don't forget to rename this file after copying the template
#for a new program!
# """
# Student Name:    
# Program Title:  
# Description:    
# """




def main():

    greetingNumber = int(input('How many people would you like to greet?'))

    for counter in range(greetingNumber):
        personName = input(f"What is the person {counter + 1} name?")
        print(f'Hello {personName}!')
  


if __name__ == "__main__":
    main()