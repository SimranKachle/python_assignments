# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
# Map function will increase each number by 10. Reduce will return product of all that numbers.


Filter1 = lambda No: (No >= 70) & (No <= 90)

Increase = lambda No: No + 10

Product = lambda No1,No2 : No1 * No2

def reduceX(Helper_Function,Data):
    Ans = 1
    for No in Data:
        Ans = Helper_Function(Ans,No)

    return Ans

def filterX(Helper_Function, Data):
    Result = []
    for No in Data:
        if(Helper_Function(No) == True):
            Result.append(No)
    
    return Result

def mapX(Helper_Function, Data):
    Result = []
    for No in Data:
        Value = Helper_Function(No)
        Result.append(Value)

    return Result    

def main():
    print("Enter number of elements you want to enter : ")
    iSize = int(input())

    Data_Input = []
    print("Please enter the data ")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is : ",Data_Input)
    
    Data_Filter = filterX(Filter1, Data_Input)

    print("List after filter is : ",Data_Filter)

    Data_Map = mapX(Increase, Data_Filter)

    print("List after map is : ",Data_Map)
    
    Output = reduceX(Product,Data_Map)

    print("Result after reduce is : ",Output)

if __name__ == "__main__":
    main()