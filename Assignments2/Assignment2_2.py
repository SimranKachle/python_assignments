# Write a program which accept number one number and display pattern below

def pattern(x):
    for i in range(x):
        for j in range(x):
            print("*", end=" ")
        print("\n")


def main():
    no=int(input("Enter number: "))
    pattern(no)


if __name__ == "__main__":
    main()
