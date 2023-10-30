outsideVariable = "I'm outside" #GLOBAL

def myFunction(in_value1, in_value2):
    myVariable = "I'm a variable inside a function" #LOCAL
    output = in_value1 + in_value2 #LOCAL
    print("myVariable: ", myVariable)
    print("output: ", output)    
    # print("mainVariable: ", mainVariable)    
    print("outsideVariable: ", outsideVariable)    

def main():
    myFunction("A","B")
    mainVariable = "I'm a variable inside the main function" #LOCAL
    print(mainVariable)


if __name__ == "__main__":
    main()