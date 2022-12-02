# Write a program which accept N numbers from user and store it into List.
# Accept one another number from user and return frequency of that number from List.


def Count(list, x):
    count = 0
    for element in list:
        if x == element:
            count = count+1
    return count


def main():
    list = []

    iSize = int(input("Enter total Numbers you want: "))

    print("Enter the numbers in the list: ")

    for i in range(0, iSize, 1):
        Number = int(input())
        list.append(Number)

    print("The numbers in List are : ", list)

    x = int(input("Element to search: "))
    print("The occurance of ", x, "is:", Count(list, x))

    # print("The occurance of ",x,"is",list.count(x))


if __name__ == "__main__":
    main()
