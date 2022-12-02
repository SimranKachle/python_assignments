# Write a program which accept number from user and return addition of
# digits in that number.

def digit_Sum(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10) 
        n = int(n/10)
    return sum 

# 51!=0 5!=0 0
#0+ 1 1+5
#int(5.1) 5 0
#6

def main():
    no = int(input("Enter the Number: "))
    x = digit_Sum(no)
    print("The Addition of digits is: ", x)


if __name__ == "__main__":
    main()
