def Display(No):
    if (No > 1):
        No = No-1
        Display(No)
        print(No, end=" ")


def main():
    number = int(input("INPUT: "))
    Display(number)


if __name__ == "__main__":
    main()
