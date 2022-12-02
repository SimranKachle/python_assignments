#Write a program which accept number from user and
#check whether that number is positive or negative or zero
def check_number(x):
    if x>0:
        print("Number is positive")
    elif x<0:
        print("Number is negative")
    else:
        print("The number is Zero")
        
def main():
    print("Enter the number: ")
    no = int(input())  
    check_number(no)
    
if __name__=="__main__":
    main()