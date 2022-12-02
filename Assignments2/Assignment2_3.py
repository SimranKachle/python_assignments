#Write a program which accept one number from user and return its factorial.

def factorial(x):
    factorial=1
    while x>0:
        factorial =factorial * x
        x=x-1
    return factorial


def main():
    number=int(input("Enter the Number: "))
    print("The factotial is : ",factorial(number))


if __name__ == "__main__":
    main()
