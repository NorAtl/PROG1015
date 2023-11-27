def main(): 

    file_name = "P1 - TheATeam/ateam_Original.txt"
    access_mode = "r"

    myFile = open(file_name, access_mode)
    file_line_data = myFile.readline()

    counter = 1

    #while you have content in file_line_data keep executing the block
    while file_line_data: 
        print(f"{file_line_data}",end="")
        file_line_data = myFile.readline()
        counter += 1

    

    

if __name__ == "__main__":
    main()