def factorial(No):
    
    if(No<=0):
        return 1
    else:
        return(No*factorial(No-1))
        


def main():
    Ret = int(input("Input: "))

    print("Result is: ",factorial(Ret))

if __name__=="__main__":
    main()