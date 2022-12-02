# Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers.
# List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which are even.
# Map function will calculate its square.
# Reduce will return addition of all that numbers.


def CheckEven(No): return No % 2 == 0


def Square(No): return pow(No, 2)


def Add(A, B): return A + B


def reduceX(Helper_Function, Data):
    Ans = 0
    for no in Data:
        Ans = Helper_Function(Ans, no)

    return Ans


def filterX(Helper_Function, Data):
    Result = []
    for no in Data:
        if (Helper_Function(no) == True):
            Result.append(no)

    return Result


def MapX(Helper_Function, Data):
    Result = []
    for no in Data:
        Value = Helper_Function(no)
        Result.append(Value)

    return Result


def main():
    print("Enter Total Numbers you want: ")
    iSize = int(input())

    Data_Input = []
    print("Enter the numbers: ")
    for i in range(0, iSize, 1):
        Value = int(input())
        Data_Input.append(Value)

    print("The Data is: ", Data_Input)

    Data_Filter = filterX(CheckEven, Data_Input)
    print("The List after Filter is: ", Data_Filter)

    Data_Map = MapX(Square, Data_Filter)
    print("The List after Map is: ", Data_Map)

    Data_Reduce = reduceX(Add, Data_Map)
    print("The List after Reduce is: ", Data_Reduce)
    # Output=reduceX(Add,map(Square,filter(CheckEven,Data_Input)))
    # print(Output)
if __name__ == "__main__":
    main()