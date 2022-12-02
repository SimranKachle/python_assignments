# Write a program which contains one lambda function which accepts two parameters and return its multiplication. 

Multiplication = lambda No1,No2 : No1 * No2


def main():
    Number1 = int(input("Enter the First Number: "))
    Number2 = int(input("Enter the Second Number: "))
    Ret = Multiplication(Number1,Number2)
    print("The Multiplication Of Numbers is: ", Ret)


if __name__ == "__main__":
    main()
