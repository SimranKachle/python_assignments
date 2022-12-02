def Display(No):
    if (No > 0):
        print(No, end=" ")
        No = No-1
        Display(No)
        
        


def main():
    number = int(input("INPUT: "))
    Display(number)


if __name__ == "__main__":
    main()
