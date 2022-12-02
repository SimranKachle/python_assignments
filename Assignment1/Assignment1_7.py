#Write a program which contains one function that accept one number from user 
# and returns true if number is divisible by 5 otherwise return false.

def number(x):
    if (x%5==0):
        print("True")
    
    else:
        print("False")
        
def main():
    print("Enter the number: ")
    no = int(input())  
    number(no)
    
if __name__=="__main__":
    main()