# Write a program which accept N numbers from user and store it into List.
# Return addition of all prime numbers from that List.
# Main python file accepts N numbers from user and pass each number to ChkPrime()
# function which is part of our user defined module named as MarvellousNum.
# Name of the function from main python file should be ListPrime().

from MarvellousNum import ChkPrime as ListPrime


def main():
    mylist = []

    iSize = int(input(" Enter Total Number of elements you want: "))

    print("Enter the numbers: ")

    for i in range(0, iSize, 1):
        Element = int(input())
        mylist.append(Element)

    print("The elements in list are: ", mylist)

    sum = 0

    for i in range(iSize):
        if(ListPrime(mylist[i])):
            sum = sum + mylist[i]

    print("The sum of prime numbers in list is: ", sum)


if __name__ == "__main__":
    main()
