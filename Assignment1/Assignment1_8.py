#Write a program which accept number from user and print that number of “*” on screen.
def number(x):
    
    for i in range(x):
        
            print("*",end=" ")
    
def main():
    print("Enter the number: ")
    x = int(input())  
    number(x)
    
if __name__=="__main__":
    main()