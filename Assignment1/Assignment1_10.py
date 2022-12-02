#Write a program which accept name from user and display 
# length of its name.

  
def main():
    print("Enter the name: ")
    name = (input())  
    print("The length is: ",len(name))
    
if __name__=="__main__":
    main()