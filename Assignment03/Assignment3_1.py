# Write a program which accept N numbers from user and store it into List.
# Return addition of all elements from that List.


def main():
    list = []

    iSize = int(input("Enter total numbers in list:  "))

    print("Enter the numbers: ")
    for i in range(0, iSize, 1):
        Add = int(input())
        list.append(Add)

    print("The numbers are: ", list)

    Sum = 0
    for element in range(0, len(list)):
        Sum = Sum + list[element]

    print("The Addition of elements is: ", Sum)


if __name__ == "__main__":
    main()
