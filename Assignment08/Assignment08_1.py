def Display(No):
    if (No > 0):
        No = No-1
        Display(No)
        print("*", end=" ")


def main():
    number = int(input("INPUT: "))
    Display(number)


if __name__ == "__main__":
    main()
