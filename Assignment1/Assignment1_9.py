#Write a program which display first 10 even numbers on screen.

def number():
    x=20
    for i in range(1,x+1):
        if (i%2==0):
            print(i,end=" ")
            # i=i+1
    
def main():
    # print("Enter the number: ")
    # no = int(input())  
    number()
    
if __name__=="__main__":
    main()