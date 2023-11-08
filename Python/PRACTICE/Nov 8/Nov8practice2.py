def main(): 

    
    myList = []
    myList.append(15)
    myList.append(25)
    myList.append(35)
    myList.append(45)
    print(myList)


    my2dList = []
    my2dList.append([11,21,31,41]) # each element of the list is a colimn
    print(my2dList)
    my2dList.append([12,22,32,42]) # each additional append creates a new row of columns
    my2dList.append([13,24,35,45])
    print(my2dList)
    print(my2dList[0])
    print(my2dList[0][2]) # the third column in the first row


    # print 2d-list using a loop
    for element in my2dList:
        print(element)

    for row in my2dList:
        print(row)
        for num in row:
            print(num)

    # for row in my2dList:
    #     for num in row:
    #         print(num, end=' ') # prints them in one line instead of starting a new line

    for row in my2dList:
        for num in row:
            print(num, end='\t')
        print() # new row - empty print after each row

    # print 2d-list using indexes
    for row_index in range(len(my2dList)): # row_index[0,..,my2dList length]
        for col_index in range(len(my2dList[row_index])):
            print(my2dList[row_index][col_index],end='\t')
        print() #new row

    















if __name__ == "__main__":
    main()