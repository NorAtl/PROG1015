


def main(): 

    file_name = 'myFile.txt'
    access_mode = 'w'   # will overwrite file
                        # if you want to append you have to use 'a' instead of 'w'

    # open file handle - will create a file if it does not exist
    myFile = open(file_name, access_mode)
    
    #writing to file
    myFile.write('Hi there!\n')
    myFile.write('How are you?\n')
    myFile.write("I'm fine. thank you!"\n)







    # close the file handle
    myFile.close()

if __name__ == "__main__":
    main()