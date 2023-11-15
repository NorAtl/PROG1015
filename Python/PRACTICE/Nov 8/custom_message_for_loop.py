def main():

    number_inputs = int(input("\nHow many names would you like to input? "))

    for student in range(number_inputs):#[0,1,2, .., number_inputs - 1]
        studentName = input(f"Enter student {student + 1} name: ")
        print(f"Hello, {studentName}!!!")



if __name__ == "__main__":
    main()