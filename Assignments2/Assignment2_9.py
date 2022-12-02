# write a program in python which accept number from user and
# return number of digits in that number

def digit(no):
    count = 0
    while(no > 0):  # 51>0 #5>0
        count = count+1  # 0+1=1 1+1=2
        no = no//10  # 5 0
    return count


def main():
    number = int(input("Enter number: "))
    print("The Total number of digits in the number are:", digit(number))


if __name__ == "__main__":
    main()
