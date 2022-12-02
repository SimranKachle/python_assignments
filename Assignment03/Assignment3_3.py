# Write a program which accept N numbers from user and store it into List.
# Return Minimum number from that List.

def Minimum(list):
    Min = list[0]
    for x in list:
        if x < Min:
            Min = x

    return Min


def main():
    list = []

    iSize = int(input("Enter Total Numbers you want: "))

    print("Enter the numbers in the list: ")
    for i in range(0, iSize, 1):
        Number = int(input())
        list.append(Number)

    print("The Numbers are: ", list)

    print("The maximum number is: ", Minimum(list))
    # print("The maximum number is: ", min(list))


if __name__ == "__main__":
    main()
