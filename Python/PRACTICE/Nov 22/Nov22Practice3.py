def main(): 

    try:
        file_name = "myfile?.txt"
        access_mode = "w"

        file_handle = open(file_name,access_mode)

        file_handle.write("Hi\n")
        file_handle.write("Bye/n")

        file_handle.close()

    except FileNotFoundError:
        print("File does not exist")

    except PermissionError:
        print("Cannot write to that folder")
    
    except OSError:
        print("File name is invalid")


if __name__ == "__main__":
    main()