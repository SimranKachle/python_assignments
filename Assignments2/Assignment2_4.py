# Write a program which accept one number 
# from user and return addition of its factors.


def Factors_Add(x):
    i=1
    sum=0
    while x>i:#6 >2 2 1 3 
        if x%i==0:
            sum=sum+i
        i=i+1
    return sum


                    
def main():
    no=int(input("Enter the Number: "))
    print("The Addition of factors  is : ",Factors_Add(no))


if __name__ == "__main__":
    main()
