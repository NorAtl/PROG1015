

def main(): 

    guests = ['james', 'sarah', 'bill', 'frank','george']

    print(guests) # print the entire list in raw format
    print(guests[0]) # 0 refers to the first entry in the list
    print(guests[3]) # prints the fourth element
    print(guests[-1]) # this refers to the last entry in the list

    students = [] # creates an empty list
    students.append('bruce') #adds an element to the list
    students.append('charles')
    students.append('frank')
    students.append('phil')
    print(students) # prints raw format
    print(students[2])
    print(students[-1]) # prints phil
    students.append('greg')
    print(students[-1]) # now prints greg

    students.remove('frank') # removes the specified element frank
    del students[1] # another way to remove an element bruce
    print(students)

    students.append('chris')
    students.append('sally')
    students.append('liz')
    students.append('bobby')
    print(students)

    indexOfbruce = students.index('bruce') # getting the element index which has the value bruce
    del students[indexOfbruce]
    print(students)

    print(students[0])
    print(students[1])
    print(students[2])

    for steps in range(3):
        print(students[steps])

    print(students)
    for student in students:
        print(student)

    NumberOfStudents = len(students)
    print(NumberOfStudents)
    for steps in range(NumberOfStudents):
        print(students[steps])

    students[4] = 'chucky' # changes the element in the fifth position to chucky
    print(students)

    





if __name__ == "__main__":
    main()