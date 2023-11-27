def main():
    file_name = "message.txt"
    access_mode = "r"
    file_handle = open(file_name, access_mode)

    # read the file content
    # file_data = file_handle.read() #reads all at once - big string

    # read a single line from the file
    file_line_data = file_handle.readline()

    counter = 1

    #while you have content in file_line_data keep executing the block
    while file_line_data: 
        print(f"line {counter} - {file_line_data}",end="")
        file_line_data = file_handle.readline()
        counter += 1

    # file_handle.close()


if __name__ == "__main__":
    main()