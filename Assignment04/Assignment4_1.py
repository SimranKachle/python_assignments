# Write a program which contains one lambda function which accepts one parameter and return power of two.

# def Power(No):
#     return pow(No,2)

# Power = lambda No: pow(No, 2)
Power = lambda No: No**2

def main():
    Number = int(input("Enter the Number: "))
    Ret = Power(Number)
    print("The power of Number is: ", Ret)


if __name__ == "__main__":
    main()

