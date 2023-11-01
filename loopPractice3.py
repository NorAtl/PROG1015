#Don't forget to rename this file after copying the template
#for a new program!
# """
# Student Name:    
# Program Title:  
# Description:    
# """




def main():

    for steps in [1, 2, 3, 4, 5]:
        print(steps)

    my_list = ['hamburger', 'hotdog', 'pizza']
    for steps in my_list:
        print(steps)

    for number in [14,27,33,84,105]:
        output = number + 2
        print(output)

    foodList = ['steak', 'pizza', 'hotdog', 'hamburger']
    for food in foodList:
        print(f'I love {food}!')
        
    for counter in range(2, 8, 2):  #[2,4,6] it ends at the second parameter -1
        print(counter)



if __name__ == "__main__":
    main()