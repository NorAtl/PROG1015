

import random

def main(): 

    correct_answer = random.randint(1,100)
    answer = 0
    count = 0

    while answer != correct_answer:
        count +=1
        answer = int(input('Guess a number between 1 and 100: ')) # this has to be inside the loop because variable has to change inside the loop
        if answer < correct_answer:
            print('Guess higher!')
        elif answer > correct_answer:
            print('Guess lower!')
            #elif answer == correct_answer:                                     
            
    print(f'Correct! It took {count} tries for you to guess correctly.' )
   

if __name__ == "__main__":
    main()