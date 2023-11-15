import turtle
def main():
    for counter in range(5):#[0, 1, 2, 3, 4]
        print(counter)

    for counter in range(4, 13):#[4, 5, 6, 7, 8, 9, 10, 11]
        print(counter)

    for counter in range(10, 100, 5):#[10, 20, 30,...,90]
        print(counter)

    for counter in range(20, 2, -1):#[20,19, 18, ..., 3]
        print(counter)

    for number in [3, 5, 6, 8, 9]:
        print(number * 2)

    favorite_food_list = ["Pizza", "Shawarma", "Cheese", "Sushi", "Taco", "Steak"]

    for food in favorite_food_list:
        if food != "Taco":
            print(f"I'd love to have some {food}")

    for color in ["red", "blue", "green", "black"]:
        turtle.color(color)
        turtle.forward(100)
        turtle.right(90)
    
    turtle.done()

if __name__ == "__main__":
    main()