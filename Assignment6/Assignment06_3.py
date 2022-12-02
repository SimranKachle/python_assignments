# Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), Factors().
# ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors.
# Use this method in any another method as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.

class Numbers:
    def __init__(self, Data):
        self.Value = Data

    def Factors(self):
        x = self.Value
        list = []

        for i in range(1, x + 1):
            if x % i == 0:
                list.append(i)

        return list

    def Sumfactors(self):
        Sum = 0

        for i in range(1, int(self.Value)):
            if(self.Value % i == 0):
                Sum = Sum + i

        return Sum

    def CheckPerfect(self):
        Ans = self.Sumfactors()

        if(self.Value == Ans):
            return True
        else:
            return False

    def CheckPrime(self):
        i = 0
        Flag = True

        for i in range(2, int(self.Value/2)+1):
            if(self.Value % i == 0):
                Flag = False
                break

        return Flag
        # print("Value of i",i)


def main():
    print("Please enter the number: ")

    A = int(input())

    obj = Numbers(A)

    Ret = obj.CheckPrime()
    if(Ret == True):
        print("{} is a prime number".format(A))
    else:
        print("{} is not a prime number".format(A))

    Ret = obj.Factors()
    print("The factors are: ", Ret)

    Ret = obj.Sumfactors()
    print("The Sum of factors is: ", Ret)
    
    Ret = obj.CheckPerfect()
    if(Ret == True):
        print("{} is a perfect number".format(A))
    else:
        print("{} is not a perfect number".format(A))

    


if __name__ == "__main__":
    main()
