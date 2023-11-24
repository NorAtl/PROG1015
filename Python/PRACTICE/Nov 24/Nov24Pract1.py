def main(): 

    file_name = "message.txt"
    access_mode = "r"
    file_handle = open(file_name,access_mode)

    # read the file content
    # file_data = file_handle.read() # reads the file all at once in a big string

    # read a single line from a file
    file_line_data = file_handle.readline() 
    
    counter = 1

    # while you have data in file_line_data, keep executing the block
    while file_line_data: 
        print(f"line {counter} - {file_line_data}",end="")
        file_line_data = file_handle.readline() 
        counter += 1


    # file_handle.close() # you don't need this with while function
    

if __name__ == "__main__":
    main()