#Write a program which accept one number and display below pattern.

def pattern(x):
    for i in range(x):
        j=1
        while j<=x:
            print(j, end=" ")
            j=j+1
        print("\n")

def main():
    no=int(input("Enter number: "))
    pattern(no)


if __name__ == "__main__":
    main()
