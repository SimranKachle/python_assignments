#Write a program which contains one function named as Add() which accepts two numbers 
#from user and return addition of that two numbers.

def Add(value1, value2):
    Ans = value1 + value2
    return Ans


def main():
    print("Enter First number: ")
    no1 = int(input())  # Local variable

    print("Enter second number: ")
    no2 = int(input())

    Sum = Add(no1, no2)
    print("Addition is: ", Sum)


if __name__ == "__main__":
    main()
