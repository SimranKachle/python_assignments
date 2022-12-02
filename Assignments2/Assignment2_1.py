# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

import Arithmetic


def main():
    no1 = int(input("Enter The Number: "))
    no2 = int(input("Enter The Number: "))

    a = Arithmetic.Add(no1, no2)
    print("The Addition of Number is: ", a)

    b = Arithmetic.Sub(no1, no2)
    print("The Subtraction of numbers is: ", b)

    c = Arithmetic.Mult(no1, no2)
    print("The Multiplication of numbers is: ", c)

    d = Arithmetic.Div(no1, no2)
    print("The Division of numbers is: ", d)


if __name__ == "__main__":
    main()
