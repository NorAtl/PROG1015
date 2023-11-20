
   
def main(): 

    
    file_name = "example.txt"
    
    try:     # Attempt to open the file for writing    
        f = open(file_name, "x")     
        f.close()     
        print(f"{file_name} created successfully.")
    except FileExistsError:     
    # If the file already exists, print a message    
        
        print(f"{file_name} already exists.")








    

if __name__ == "__main__":
    main()