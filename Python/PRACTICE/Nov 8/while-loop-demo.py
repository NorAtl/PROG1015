import time
def main():

    count = 0

    while count < 100:
        print(count)
        # count = count + 1
        count += 1
        time.sleep(0.5)

    print(f"The final count is {count}.")

if __name__ == "__main__":
    main()