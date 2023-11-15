import time
def main():

    answer = 0  
    correct_answer = 11 

    while answer != correct_answer:
        answer = int(input("What is 2 + 2? "))

        if answer != correct_answer:
            print('Nope. Try again!')
            if answer == correct_answer - 1 or answer == correct_answer + 1:
                print('So close, keep trying...')
    
    print(f'YES! You got it! 2 + 2 = {answer}')

if __name__ == "__main__":
    main()