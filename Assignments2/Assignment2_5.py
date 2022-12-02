#Write a program which accept one number for user 
# and 
# check whether number is prime or not.

def prime(number):
    if number>1:
        for i in range (2,number):
            if (number%i)==0:
                print("This Number is Not Prime")
                break
        else:
            print("The number is Prime")
    
def main():
    no=int(input("Enter the Number: "))
    prime(no)
    
if __name__=="__main__":
    main()
    