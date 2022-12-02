# Write a program which accept N numbers from user and store it into List.
# Return Maximum number from that List.

def Maximum(list):
    Max = list[0]
    for x in list:
        if x > Max:
            Max = x

    return Max


def main():
    list = []

    iSize = int(input("Enter Total Numbers you want: "))

    print("Enter the numbers in the list: ")
    for i in range(0, iSize, 1):
        Number = int(input())
        list.append(Number)

    print("The Numbers are: ", list)

    # print("The maximum element is: ",max(list))
    print("The maximum number is: ", Maximum(list))


if __name__ == "__main__":
    main()
