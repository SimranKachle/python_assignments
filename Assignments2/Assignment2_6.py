#Write a program which accept one number and display below pattern.

def pattern(x):
    for i in range(x,0,-1):
        for j in range(i):
            print("*", end=" ")
           
        print("\n")


def main():
    no=int(input("Enter number: "))
    pattern(no)



if __name__ == "__main__":
    main()
