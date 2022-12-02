# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user.
# Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. 
# Reduce will return Maximum number from that numbers. 
# (You can also use normal functions instead of lambda functions).
# from functools import reduce

def prime(No):
    for i in range(2,No):
        if (No%i)==0: 
            return False
    else:
        return True

    
def Mult(No):
    return No * 2

# Mult = lambda No : No * 2 

def Max(x,y):
    if x > y :
        return x
    else:
        return y

# Max= lambda x,y : x if x > y else y


def reduceX(Helper_Function,Data):
    Ans=0
    for no in Data:
        Ans = Helper_Function(Ans,no)
    
    return Ans


def filterX(Helper_Function, Data):
    Result = []
    for no in Data:
        if (Helper_Function(no) == True):
            Result.append(no)

    return Result

def mapX(Helper_function,Data):
    Result=[]
    for no in Data:
        Value=Helper_function(no)
        Result.append(Value)
    
    return Result
     
def main():
    print("Enter Total numbers: ")
    iSize=int(input())
    
    Data_Input=[]
    
    print("Enter the Numbers: ")
    for i in range(0,iSize,1):
        Value=int(input())
        Data_Input.append(Value)
    
    print("The numbers are: ",Data_Input)
    Data_Filter=list(filterX(prime,Data_Input))
    print("The List after Filter are: ",Data_Filter)
    
    Data_Map=list(mapX(Mult,Data_Filter))
    print("The List after Map are: ",Data_Map)
    
    Data_Reduce=reduceX(Max,Data_Map)
    print("The List after Reduce are: ",Data_Reduce)
    
    
    
if __name__=="__main__":
    main()