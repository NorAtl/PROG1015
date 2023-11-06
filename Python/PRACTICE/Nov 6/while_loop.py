def main():

    answer = 0
    correct_answer = 4

    while answer != correct_answer:
        answer = int(input('what is 2+2? '))
        if answer != correct_answer:
            print('Nope. Please try again!')
    print(f'YES! 2 + 2 = {answer}')



if __name__ == "__main__":
    main()