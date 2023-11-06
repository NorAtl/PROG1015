

def main(): 

    import time
    count = 0

    while count < 10:
        print(count)
        count += 1 # count = count + 1
        time.sleep(0.5)

    print(f'The final count is {count}.')


if __name__ == "__main__":
    main()