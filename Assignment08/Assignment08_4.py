def Sum(No):
    if No<=1:
        return No
    else:
        return No+Sum(No-1)
    
def main():
    number = int(input("INPUT: "))
    print("The Sum is: ",Sum(number))


if __name__ == "__main__":
    main()