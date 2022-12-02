#  Write a program which contains one function named as ChkNum() which accept one
#  parameter as number. If number is even then it should display “Even number” otherwise  display “Odd number” on console.


def ChkNum(number):
    if number%2==0:
        print("Even Number")
    else:
         print("Odd Number")
        

def main():
    x=int(input("Enter the Number: "))
    ChkNum(x)


if __name__ == "__main__":
    main()
