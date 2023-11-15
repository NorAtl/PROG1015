def main():
    guests = ['James', 'Sarah', 'Clark', 'Arthur', 'Anne']
    # print the list in 'raw' format
    print(guests)

    # print the first element of the list
    print(guests[0])

    # print the fourth element in the list
    print(guests[3])

    # create an empty list
    students = []

    # adding elements to the end of the list
    students.append('Bruce')
    students.append('Tyler')
    students.append('Colin')
    students.append('Phil')

    # print the fourth element in the list
    print(students[3])
    # printing the last element
    print(students[-1])

    students.append('Greg')
     # print the fourth element in the list
    print(students[3])
    # printing the last element
    print(students[-1])

    students.append('Diana')
    print(students)

    # removing the element with value 'Diana' from the list
    students.remove('Diana')
    print(students)

    # removing the element on a specific index position from the array
    del students[1]
    print(students)

    # getting the element index which has the value 'Greg
    indexOfGreg = students.index('Greg') # = 3
    # remove an ement from the list with a specific index
    del students[indexOfGreg]
    print(students)

    students.append('Anton')

    numberOfStudents = len(students)

    print(numberOfStudents)
    
    for steps in range(numberOfStudents): #steps = [0,1, ..., numberOfStudents]
        print(students[steps])
        # print(students[1])
        # print(students[2])

    students.append('Brent')
    
    for student in students:
        print(student)

    
    print(students)

    # updating list element with index 2
    students[2] = 'Alexis'

    print(students)

if __name__ == "__main__":
    main()