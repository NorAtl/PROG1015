import time
def main():

    count = 0
    for steps in range(100):
        count += 1
        print(count)
        time.sleep(1) #number of seconds is in brackets
    print(f'the final count is {count}')


if __name__ == "__main__":
    main()